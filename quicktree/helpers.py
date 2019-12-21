import os
from typing import NamedTuple


class QuickTreeStruct(NamedTuple):
    """Underlying data structure for trees displayed in stdout.

    Meant to contain information on all directories and files found in
    some root directory.

    Has the following structure:

    ``{``
        ``dirs: {``
            name of directory ``:`` path to directory
        | ``},``
        | ``files: set(`` file names ``)``
        }
    ``}``
    """
    dirs: dict
    files: set


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
