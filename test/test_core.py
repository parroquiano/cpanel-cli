import os
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import Mock

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


if __name__ == "__main__":
	unittest.main()
