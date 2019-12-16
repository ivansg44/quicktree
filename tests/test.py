import os
import unittest

from quicktree import helpers


class TestQuickTreeStruct(unittest.TestCase):
    @staticmethod
    def _get_test_dir_path(dir_name):
        tests_path = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(tests_path, "test_dirs", dir_name)

    def test_empty(self):
        test_dir_path = self._get_test_dir_path("empty")
        actual_struct = helpers.get_quicktree_struct(test_dir_path)
        expected_struct = {
            "dirs": {},
            "files": []
        }
        self.assertDictEqual(expected_struct, actual_struct)

    def test_one_file(self):
        test_dir_path = self._get_test_dir_path("one_file")
        actual_struct = helpers.get_quicktree_struct(test_dir_path)
        expected_struct = {
            "dirs": {},
            "files": ["spam"]
        }

        self.assertDictEqual(expected_struct, actual_struct)

    def test_multi_files(self):
        test_dir_path = self._get_test_dir_path("multi_files")
        actual_struct = helpers.get_quicktree_struct(test_dir_path)
        expected_struct = {
            "dirs": {},
            "files": ["spam", "ham", "eggs"]
        }
        self.assertDictEqual(expected_struct, actual_struct)

    def test_one_dir(self):
        test_dir_path = self._get_test_dir_path("one_dir")
        actual_struct = helpers.get_quicktree_struct(test_dir_path)
        expected_struct = {
            "dirs": {
                "foo": os.path.join(test_dir_path, "foo")
            },
            "files": []
        }
        self.assertDictEqual(expected_struct, actual_struct)

    def test_multi_dirs(self):
        test_dir_path = self._get_test_dir_path("multi_dirs")
        actual_struct = helpers.get_quicktree_struct(test_dir_path)
        expected_struct = {
            "dirs": {
                "foo": os.path.join(test_dir_path, "foo"),
                "bar": os.path.join(test_dir_path, "bar")
            },
            "files": []
        }
        self.assertDictEqual(expected_struct, actual_struct)

    def test_one_file_one_dir(self):
        test_dir_path = self._get_test_dir_path("one_file_one_dir")
        actual_struct = helpers.get_quicktree_struct(test_dir_path)
        expected_struct = {
            "dirs": {
                "foo": os.path.join(test_dir_path, "foo")
            },
            "files": ["spam"]
        }
        self.assertDictEqual(expected_struct, actual_struct)

    def test_multi_files_one_dir(self):
        test_dir_path = self._get_test_dir_path("multi_files_one_dir")
        actual_struct = helpers.get_quicktree_struct(test_dir_path)
        expected_struct = {
            "dirs": {
                "foo": os.path.join(test_dir_path, "foo")
            },
            "files": ["spam", "ham", "eggs"]
        }
        self.assertDictEqual(expected_struct, actual_struct)

    def test_one_file_multi_dirs(self):
        test_dir_path = self._get_test_dir_path("one_file_multi_dirs")
        actual_struct = helpers.get_quicktree_struct(test_dir_path)
        expected_struct = {
            "dirs": {
                "foo": os.path.join(test_dir_path, "foo"),
                "bar": os.path.join(test_dir_path, "bar")
            },
            "files": ["spam"]
        }
        self.assertDictEqual(expected_struct, actual_struct)

    def test_multi_files_multi_dirs(self):
        test_dir_path = self._get_test_dir_path("multi_files_multi_dirs")
        actual_struct = helpers.get_quicktree_struct(test_dir_path)
        expected_struct = {
            "dirs": {
                "foo": os.path.join(test_dir_path, "foo"),
                "bar": os.path.join(test_dir_path, "bar")
            },
            "files": ["spam", "ham", "eggs"]
        }
        self.assertDictEqual(expected_struct, actual_struct)


if __name__ == "__main__":
    unittest.main()
