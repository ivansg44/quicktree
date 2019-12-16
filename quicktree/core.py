#!/usr/bin/env python3

import os

from quicktree import helpers


def main():
    quicktree_struct = helpers.get_quicktree_struct(os.getcwd())


if __name__ == "__main__":
    main()
