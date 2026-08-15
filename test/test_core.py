import os
import tempfile
import unittest
from types import SimpleNamespace
from typing import cast
from unittest.mock import Mock

from cpanel_api import Result
from cpanel.core import CPanelEndpoint, CPanelError


class TestUploadFile(unittest.TestCase):

	def setUp(self) -> None:
		self.temporary_directory = tempfile.TemporaryDirectory()
		self.addCleanup(self.temporary_directory.cleanup)
		self.filename = os.path.join(self.temporary_directory.name, "upload.txt")
		with open(self.filename, "w") as stream:
			stream.write("test upload")

		self.response = Mock(status_code = 200)
		self.client = Mock(
			base_url = "https://example.test:2083",
			auth = "cpanel user:token",
			timeout = 30,
			verify = True,
		)
		self.client.session.post.return_value = self.response
		self.endpoint = CPanelEndpoint(self.client)


	def test_successful_response_returns_ok(self) -> None:
		self.response.json.return_value = SimpleNamespace(status = 1, errors = None)

		self.assertEqual(self.endpoint.upload_file("/remote", self.filename), "OK")


	def test_invalid_json_raises_bad_response(self) -> None:
		self.response.json.side_effect = ValueError

		with self.assertRaisesRegex(CPanelError, "^Bad response$"):
			self.endpoint.upload_file("/remote", self.filename)


	def test_unauthorized_response_raises_unauthorized(self) -> None:
		self.response.status_code = 401

		with self.assertRaisesRegex(CPanelError, "^Unauthorized$"):
			self.endpoint.upload_file("/remote", self.filename)
		self.response.json.assert_not_called()


	def test_other_http_error_is_not_parsed_as_json(self) -> None:
		self.response.status_code = 503

		with self.assertRaisesRegex(CPanelError, "^HTTP 503 response$"):
			self.endpoint.upload_file("/remote", self.filename)
		self.response.json.assert_not_called()


class TestSafeResponses(unittest.TestCase):

	def setUp(self) -> None:
		self.endpoint = CPanelEndpoint(Mock())


	def response(self, status: int, errors: object) -> Result:
		return cast(Result, SimpleNamespace(status = status, errors = errors))


	def test_success_accepts_empty_error_list(self) -> None:
		result = self.endpoint.safely(self.response(1, []), lambda: "OK")
		self.assertEqual(result, "OK")


	def test_success_accepts_no_error_string(self) -> None:
		result = self.endpoint.safely(self.response(1, "No errors occurred"), lambda: "OK")
		self.assertEqual(result, "OK")


	def test_success_with_reported_error_raises(self) -> None:
		with self.assertRaisesRegex(CPanelError, "^quota exceeded$"):
			self.endpoint.safely(self.response(1, ["quota exceeded"]), lambda: "OK")


	def test_failed_response_with_empty_errors_is_stable(self) -> None:
		with self.assertRaisesRegex(CPanelError, "^cPanel API request failed$"):
			self.endpoint.safely(self.response(0, []), lambda: "OK")


	def test_failed_response_accepts_string_error(self) -> None:
		with self.assertRaisesRegex(CPanelError, "^permission denied$"):
			self.endpoint.safely(self.response(0, "permission denied"), lambda: "OK")


	def test_malformed_error_shape_is_stable(self) -> None:
		with self.assertRaisesRegex(CPanelError, r"^malformed error response \(dict\)$"):
			self.endpoint.safely(self.response(0, {"message": "secret"}), lambda: "OK")


if __name__ == "__main__":
	unittest.main()
