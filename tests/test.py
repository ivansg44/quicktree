import os
import unittest

from quicktree import helpers


class TestGetQuickTreeStruct(unittest.TestCase):
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


class TestMapQuickTreeDirs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        TestGetQuickTreeStruct.setUpClass()

    @classmethod
    def tearDownClass(cls):
        TestGetQuickTreeStruct.tearDownClass()

    @staticmethod
    def _get_test_dir_path(dir_name):
        return TestGetQuickTreeStruct._get_test_dir_path(dir_name)

    @staticmethod
    def _get_empty_map():
        return {
            "0": [], "1": [], "2": [], "3": [], "4": [], "5": [], "6": [],
            "7": [], "8": [], "9": [], "a": [], "b": [], "c": [], "d": [],
            "e": [], "f": [], "g": [], "h": [], "i": [], "j": [], "k": [],
            "l": [], "m": [], "n": [], "o": [], "p": [], "q": [], "r": [],
            "s": [], "t": [], "u": [], "v": [], "w": [], "x": [], "y": [],
            "z": []
        }

    @staticmethod
    def _get_alpha_num_order():
        return ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b",
                "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    def test_empty(self):
        test_dir_path = self._get_test_dir_path("test_empty")
        struct = helpers.get_quicktree_struct(test_dir_path)
        actual_map = helpers.map_quicktree_dirs(struct)
        expected_map = self._get_empty_map()
        self.assertDictEqual(expected_map, actual_map)

    def test_one_file(self):
        test_dir_path = self._get_test_dir_path("test_one_file")
        struct = helpers.get_quicktree_struct(test_dir_path)
        actual_map = helpers.map_quicktree_dirs(struct)
        expected_map = self._get_empty_map()
        self.assertDictEqual(expected_map, actual_map)

    def test_multi_files(self):
        test_dir_path = self._get_test_dir_path("test_multi_files")
        struct = helpers.get_quicktree_struct(test_dir_path)
        actual_map = helpers.map_quicktree_dirs(struct)
        expected_map = self._get_empty_map()
        self.assertDictEqual(expected_map, actual_map)

    def test_one_dir(self):
        test_dir_path = self._get_test_dir_path("test_one_dir")
        struct = helpers.get_quicktree_struct(test_dir_path)
        actual_map = helpers.map_quicktree_dirs(struct)
        expected_map = self._get_empty_map()
        expected_map["0"] += ["foo"]
        self.assertDictEqual(expected_map, actual_map)

    def test_multi_dirs(self):
        test_dir_path = self._get_test_dir_path("test_multi_dirs")
        struct = helpers.get_quicktree_struct(test_dir_path)
        actual_map = helpers.map_quicktree_dirs(struct)
        expected_map = self._get_empty_map()
        expected_map["0"] += ["bar"]
        expected_map["1"] += ["foo"]
        self.assertDictEqual(expected_map, actual_map)

    def test_one_file_one_dir(self):
        test_dir_path = self._get_test_dir_path("test_one_file_one_dir")
        struct = helpers.get_quicktree_struct(test_dir_path)
        actual_map = helpers.map_quicktree_dirs(struct)
        expected_map = self._get_empty_map()
        expected_map["0"] += ["foo"]
        self.assertDictEqual(expected_map, actual_map)

    def test_multi_files_one_dir(self):
        test_dir_path = self._get_test_dir_path("test_multi_files_one_dir")
        struct = helpers.get_quicktree_struct(test_dir_path)
        actual_map = helpers.map_quicktree_dirs(struct)
        expected_map = self._get_empty_map()
        expected_map["0"] += ["foo"]
        self.assertDictEqual(expected_map, actual_map)

    def test_one_file_multi_dirs(self):
        test_dir_path = self._get_test_dir_path("test_one_file_multi_dirs")
        struct = helpers.get_quicktree_struct(test_dir_path)
        actual_map = helpers.map_quicktree_dirs(struct)
        expected_map = self._get_empty_map()
        expected_map["0"] += ["bar"]
        expected_map["1"] += ["foo"]
        self.assertDictEqual(expected_map, actual_map)

    def test_multi_files_multi_dirs(self):
        test_dir_path = self._get_test_dir_path("test_multi_files_multi_dirs")
        struct = helpers.get_quicktree_struct(test_dir_path)
        actual_map = helpers.map_quicktree_dirs(struct)
        expected_map = self._get_empty_map()
        expected_map["0"] += ["bar"]
        expected_map["1"] += ["foo"]
        self.assertDictEqual(expected_map, actual_map)

    def test_36_dirs(self):
        test_dir_path = self._get_test_dir_path("test_36_dirs")
        struct = helpers.get_quicktree_struct(test_dir_path)
        actual_map = helpers.map_quicktree_dirs(struct)
        expected_map = self._get_empty_map()

        alpha_num_order = self._get_alpha_num_order()
        sorted_dirs = sorted(range(36), key=str)
        for i in range(len(alpha_num_order)):
            expected_map[alpha_num_order[i]] += [str(sorted_dirs[i])]

        self.assertDictEqual(expected_map, actual_map)

    def test_37_dirs(self):
        test_dir_path = self._get_test_dir_path("test_37_dirs")
        struct = helpers.get_quicktree_struct(test_dir_path)
        actual_map = helpers.map_quicktree_dirs(struct)
        expected_map = self._get_empty_map()

        alpha_num_order = self._get_alpha_num_order()
        sorted_dirs = sorted(range(37), key=str)
        for i in range(len(alpha_num_order)):
            expected_map[alpha_num_order[i]] += [str(sorted_dirs[i])]
        expected_map["0"] += ["9"]

        self.assertDictEqual(expected_map, actual_map)

    def test_73_dirs(self):
        test_dir_path = self._get_test_dir_path("test_73_dirs")
        struct = helpers.get_quicktree_struct(test_dir_path)
        actual_map = helpers.map_quicktree_dirs(struct)
        expected_map = self._get_empty_map()

        alpha_num_order = self._get_alpha_num_order()
        sorted_dirs = sorted(range(73), key=str)
        for i in range(len(alpha_num_order)):
            expected_map[alpha_num_order[i]] += [str(sorted_dirs[i])]
            expected_map[alpha_num_order[i]] += [str(sorted_dirs[i+36])]
        expected_map["0"] += ["9"]

        self.assertDictEqual(expected_map, actual_map)


class TestGetOutputStr(unittest.TestCase):
    @staticmethod
    def _get_test_dir_path(dir_name):
        return TestGetQuickTreeStruct._get_test_dir_path(dir_name)

    @staticmethod
    def _get_alpha_num_order():
        return ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b",
                "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    def test_empty(self):
        test_dir_path = self._get_test_dir_path("test_empty")
        struct = helpers.get_quicktree_struct(test_dir_path)
        map = helpers.map_quicktree_dirs(struct)
        actual_output_str = helpers.get_output_str(struct, map)
        expected_output_str = "Current Directory\n" \
                              "\n" \
                              "Subdirectories\n" \
                              "\n"
        self.assertEqual(expected_output_str, actual_output_str)

    def test_one_file(self):
        test_dir_path = self._get_test_dir_path("test_one_file")
        struct = helpers.get_quicktree_struct(test_dir_path)
        map = helpers.map_quicktree_dirs(struct)
        actual_output_str = helpers.get_output_str(struct, map)
        expected_output_str = "Current Directory\n" \
                              "spam\n" \
                              "Subdirectories\n" \
                              "\n"
        self.assertEqual(expected_output_str, actual_output_str)

    def test_multi_files(self):
        test_dir_path = self._get_test_dir_path("test_multi_files")
        struct = helpers.get_quicktree_struct(test_dir_path)
        map = helpers.map_quicktree_dirs(struct)
        actual_output_str = helpers.get_output_str(struct, map)
        expected_output_str = "Current Directory\n" \
                              "eggs ham spam\n" \
                              "Subdirectories\n" \
                              "\n"
        self.assertEqual(expected_output_str, actual_output_str)

    def test_one_dir(self):
        test_dir_path = self._get_test_dir_path("test_one_dir")
        struct = helpers.get_quicktree_struct(test_dir_path)
        map = helpers.map_quicktree_dirs(struct)
        actual_output_str = helpers.get_output_str(struct, map)
        expected_output_str = "Current Directory\n" \
                              "\n" \
                              "Subdirectories\n" \
                              "0: foo\n"
        self.assertEqual(expected_output_str, actual_output_str)

    def test_multi_dirs(self):
        test_dir_path = self._get_test_dir_path("test_multi_dirs")
        struct = helpers.get_quicktree_struct(test_dir_path)
        map = helpers.map_quicktree_dirs(struct)
        actual_output_str = helpers.get_output_str(struct, map)
        expected_output_str = "Current Directory\n" \
                              "\n" \
                              "Subdirectories\n" \
                              "0: bar 1: foo\n"
        self.assertEqual(expected_output_str, actual_output_str)

    def test_one_file_one_dir(self):
        test_dir_path = self._get_test_dir_path("test_one_file_one_dir")
        struct = helpers.get_quicktree_struct(test_dir_path)
        map = helpers.map_quicktree_dirs(struct)
        actual_output_str = helpers.get_output_str(struct, map)
        expected_output_str = "Current Directory\n" \
                              "spam\n" \
                              "Subdirectories\n" \
                              "0: foo\n"
        self.assertEqual(expected_output_str, actual_output_str)

    def test_multi_files_one_dir(self):
        test_dir_path = self._get_test_dir_path("test_multi_files_one_dir")
        struct = helpers.get_quicktree_struct(test_dir_path)
        map = helpers.map_quicktree_dirs(struct)
        actual_output_str = helpers.get_output_str(struct, map)
        expected_output_str = "Current Directory\n" \
                              "eggs ham spam\n" \
                              "Subdirectories\n" \
                              "0: foo\n"
        self.assertEqual(expected_output_str, actual_output_str)

    def test_one_file_multi_dirs(self):
        test_dir_path = self._get_test_dir_path("test_one_file_multi_dirs")
        struct = helpers.get_quicktree_struct(test_dir_path)
        map = helpers.map_quicktree_dirs(struct)
        actual_output_str = helpers.get_output_str(struct, map)
        expected_output_str = "Current Directory\n" \
                              "spam\n" \
                              "Subdirectories\n" \
                              "0: foo 1: bar\n"
        self.assertEqual(expected_output_str, actual_output_str)

    def test_multi_files_multi_dirs(self):
        test_dir_path = self._get_test_dir_path("test_multi_files_multi_dirs")
        struct = helpers.get_quicktree_struct(test_dir_path)
        map = helpers.map_quicktree_dirs(struct)
        actual_output_str = helpers.get_output_str(struct, map)
        expected_output_str = "Current Directory\n" \
                              "eggs ham spam\n" \
                              "Subdirectories\n" \
                              "0: foo 1: bar\n"
        self.assertEqual(expected_output_str, actual_output_str)

    def test_36_dirs(self):
        test_dir_path = self._get_test_dir_path("test_36_dirs")
        struct = helpers.get_quicktree_struct(test_dir_path)
        map = helpers.map_quicktree_dirs(struct)
        actual_output_str = helpers.get_output_str(struct, map)
        expected_output_str = "Current Directory\n" \
                              "eggs ham spam\n" \
                              "Subdirectories\n"

        alpha_num_order = self._get_alpha_num_order()
        sorted_dirs = sorted(range(36), key=str)
        for i in range(len(alpha_num_order)):
            expected_output_str += alpha_num_order[i] + ": "
            expected_output_str += str(sorted_dirs[i]) + " "
        expected_output_str = expected_output_str[:-1]

        self.assertEqual(expected_output_str, actual_output_str)

    def test_37_dirs(self):
        test_dir_path = self._get_test_dir_path("test_37_dirs")
        struct = helpers.get_quicktree_struct(test_dir_path)
        map = helpers.map_quicktree_dirs(struct)
        actual_output_str = helpers.get_output_str(struct, map)
        expected_output_str = "Current Directory\n" \
                              "eggs ham spam\n" \
                              "Subdirectories\n"

        alpha_num_order = self._get_alpha_num_order()
        sorted_dirs = sorted(range(37), key=str)
        for i in range(len(alpha_num_order)):
            expected_output_str += alpha_num_order[i] + ": "
            expected_output_str += str(sorted_dirs[i]) + " "
        expected_output_str += "...\n"

        self.assertEqual(expected_output_str, actual_output_str)

    def test_73_dirs(self):
        test_dir_path = self._get_test_dir_path("test_73_dirs")
        struct = helpers.get_quicktree_struct(test_dir_path)
        map = helpers.map_quicktree_dirs(struct)
        actual_output_str = helpers.get_output_str(struct, map)
        expected_output_str = "Current Directory\n" \
                              "eggs ham spam\n" \
                              "Subdirectories\n"

        alpha_num_order = self._get_alpha_num_order()
        sorted_dirs = sorted(range(73), key=str)
        for i in range(len(alpha_num_order)):
            expected_output_str += alpha_num_order[i] + ": "
            expected_output_str += str(sorted_dirs[i]) + " "
        expected_output_str += "...\n"

        self.assertEqual(expected_output_str, actual_output_str)


if __name__ == "__main__":
    unittest.main()
