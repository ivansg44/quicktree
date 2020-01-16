import os
import unittest

from quicktree import helpers


class TestQuickTreeStruct(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Remove ``.gitkeep`` files.

        This makes directories that are meant to be empty truly empty.
        """
        for root, _, files in os.walk(cls._get_test_dir_path("")):
            for file in files:
                if file == ".gitkeep":
                    os.remove(os.path.join(root, file))

    @classmethod
    def tearDownClass(cls):
        """Add ``.gitkeep`` files.

        This makes empty directories trackable.
        """
        for root, dirs, files in os.walk(cls._get_test_dir_path("")):
            # Empty directory
            if not dirs and not files:
                with open(os.path.join(root, ".gitkeep"), "w") as _:
                    pass

    @staticmethod
    def _get_test_dir_path(dir_name):
        tests_path = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(tests_path, "test_dirs", dir_name)

    def test_empty(self):
        test_dir_path = self._get_test_dir_path("test_empty")
        actual_struct = helpers.get_quicktree_struct(test_dir_path)
        expected_struct = {
            "dirs": {},
            "files": set()
        }
        self.assertDictEqual(expected_struct, actual_struct)

    def test_one_file(self):
        test_dir_path = self._get_test_dir_path("test_one_file")
        actual_struct = helpers.get_quicktree_struct(test_dir_path)
        expected_struct = {
            "dirs": {},
            "files": {"spam"}
        }

        self.assertDictEqual(expected_struct, actual_struct)

    def test_multi_files(self):
        test_dir_path = self._get_test_dir_path("test_multi_files")
        actual_struct = helpers.get_quicktree_struct(test_dir_path)
        expected_struct = {
            "dirs": {},
            "files": {"spam", "ham", "eggs"}
        }
        self.assertDictEqual(expected_struct, actual_struct)

    def test_one_dir(self):
        test_dir_path = self._get_test_dir_path("test_one_dir")
        actual_struct = helpers.get_quicktree_struct(test_dir_path)
        expected_struct = {
            "dirs": {
                "foo": os.path.join(test_dir_path, "foo")
            },
            "files": set()
        }
        self.assertDictEqual(expected_struct, actual_struct)

    def test_multi_dirs(self):
        test_dir_path = self._get_test_dir_path("test_multi_dirs")
        actual_struct = helpers.get_quicktree_struct(test_dir_path)
        expected_struct = {
            "dirs": {
                "foo": os.path.join(test_dir_path, "foo"),
                "bar": os.path.join(test_dir_path, "bar")
            },
            "files": set()
        }
        self.assertDictEqual(expected_struct, actual_struct)

    def test_one_file_one_dir(self):
        test_dir_path = self._get_test_dir_path("test_one_file_one_dir")
        actual_struct = helpers.get_quicktree_struct(test_dir_path)
        expected_struct = {
            "dirs": {
                "foo": os.path.join(test_dir_path, "foo")
            },
            "files": {"spam"}
        }
        self.assertDictEqual(expected_struct, actual_struct)

    def test_multi_files_one_dir(self):
        test_dir_path = self._get_test_dir_path("test_multi_files_one_dir")
        actual_struct = helpers.get_quicktree_struct(test_dir_path)
        expected_struct = {
            "dirs": {
                "foo": os.path.join(test_dir_path, "foo")
            },
            "files": {"spam", "ham", "eggs"}
        }
        self.assertDictEqual(expected_struct, actual_struct)

    def test_one_file_multi_dirs(self):
        test_dir_path = self._get_test_dir_path("test_one_file_multi_dirs")
        actual_struct = helpers.get_quicktree_struct(test_dir_path)
        expected_struct = {
            "dirs": {
                "foo": os.path.join(test_dir_path, "foo"),
                "bar": os.path.join(test_dir_path, "bar")
            },
            "files": {"spam"}
        }
        self.assertDictEqual(expected_struct, actual_struct)

    def test_multi_files_multi_dirs(self):
        test_dir_path = self._get_test_dir_path("test_multi_files_multi_dirs")
        actual_struct = helpers.get_quicktree_struct(test_dir_path)
        expected_struct = {
            "dirs": {
                "foo": os.path.join(test_dir_path, "foo"),
                "bar": os.path.join(test_dir_path, "bar")
            },
            "files": {"spam", "ham", "eggs"}
        }
        self.assertDictEqual(expected_struct, actual_struct)


if __name__ == "__main__":
    unittest.main()
