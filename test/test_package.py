import glob
import os
import tarfile
import unittest
import zipfile


class TestPackageContents(unittest.TestCase):

	@classmethod
	def setUpClass(cls) -> None:
		dist_dir = os.environ.get('CPANEL_DIST_DIR', 'dist')
		wheels = glob.glob(os.path.join(dist_dir, '*.whl'))
		sdists = glob.glob(os.path.join(dist_dir, '*.tar.gz'))
		if not wheels or not sdists:
			raise unittest.SkipTest('build wheel and source distribution before artifact checks')
		cls.wheel = wheels[0]
		cls.sdist = sdists[0]


	def test_wheel_contains_runtime_modules_and_help(self) -> None:
		with zipfile.ZipFile(self.wheel) as archive:
			names = set(archive.namelist())
		for expected in (
			'cpanel/caller/features.py',
			'cpanel/caller/mail_filters.py',
			'cpanel/USAGE',
			'cpanel/REFERENCE',
		):
			self.assertIn(expected, names)


	def test_sdist_contains_project_sources_and_documentation(self) -> None:
		with tarfile.open(self.sdist, 'r:gz') as archive:
			names = archive.getnames()
		for expected_suffix in (
			'/UAPI.md',
			'/cpanel/caller/features.py',
			'/test/test_core.py',
			'/doc/index.rst',
			'/doc/_static/cpanel-cli-salmon.png',
		):
			self.assertTrue(
				any(name.endswith(expected_suffix) for name in names),
				'{} missing from source distribution'.format(expected_suffix),
			)


if __name__ == '__main__':
	unittest.main()
