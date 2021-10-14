# -*- cofding: utf-8 -*.

import sys, time
from typing import Protocol
from tqdm import tqdm


__version__ = "0.3.0"
__all__ = ("main", "lowercased", "uppercased")


class StringConvertible(Protocol):
    def __str__(self) -> str:
        ...


def lowercased(obj: StringConvertible) -> str:
    """
    Return the string representation in lowercased form.
    """
    return str(obj).lower()


def uppercased(obj: StringConvertible) -> str:
    """
    Return the string representation in uppercase form.
    """
    return str(obj).upper()


__all__ = ("main",)


def main() -> None:

    if len(sys.argv) != 2:
        print("The first argument must be natural number e.g. 3")
        sys.exit(1)

    for i in tqdm(range(int(sys.argv[1]))):
        time.sleep(0.1)

    print("It works!")
