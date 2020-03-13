import os
from typing import NamedTuple


QuickTreeStruct_ =\
    NamedTuple("QuickTreeStruct", [("dirs", dict), ("files", set)])


class QuickTreeStruct(QuickTreeStruct_):
    """Underlying data structure for trees displayed in stdout.

    Meant to contain information on all directories and files found in
    some root directory.

    Has the following structure:

    ``{``
        ``dirs: {``
            name of directory ``:`` path to directory
        | ``},``
        | ``files: set(`` file names ``)``
    ``}``
    """
    pass


def get_quicktree_struct(root):
    """Get a ``quicktree`` struct for a specified root directory.

    :param str root: Path to some directory
    :return: ``QuickTreeStruct`` for ``root``
    :rtype: QuickTreeStruct
    """
    for _, dirs, files in os.walk(root):
        return {
            "dirs": {d: os.path.join(root, d) for d in dirs},
            "files": set(files)
        }


def map_quicktree_dirs(struct):
    """Maps ``struct.dirs`` to alphanumeric keys.

    ``struct.dirs`` is mapped in alphanumeric order. Keys are selected
    for assignment in alphanumeric order as well, and are looped over.

    :param QuickTreeStruct struct:
    :return: ``struct.dirs`` mapped to alphanumeric keys
    :rtype: dict[str, list[str]]
    """
    ret_keys = [
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d",
        "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
        "s", "t", "u", "v", "w", "x", "y", "z"
    ]
    ret = {x: [] for x in ret_keys}

    sorted_dirs_list = sorted(struct["dirs"])
    for i in range(len(sorted_dirs_list)):
        ret_key = ret_keys[i % len(ret_keys)]
        ret[ret_key] += [sorted_dirs_list[i]]

    return ret
