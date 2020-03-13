#!/usr/bin/env python3

import os

from quicktree import helpers


def main():
    quicktree_struct = helpers.get_quicktree_struct(os.getcwd())
    quicktree_dirs_map = helpers.map_quicktree_dirs(quicktree_struct)


if __name__ == "__main__":
    main()
