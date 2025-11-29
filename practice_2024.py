from dataclasses import dataclass


@dataclass
class FileData:
    left_list: list[int]
    right_list: list[int]


DEFAULT_FILENAME = "input_practice.txt"


def read_lists(file_name: str = DEFAULT_FILENAME) -> FileData:
    """
    Read a given list file and return a FileData object

    :param file_name: the file name to read from
    :return: a FileData object containing the two lists in the file
    """
    pass


def do_part_1(input_file_name: str = DEFAULT_FILENAME) -> int:
    """
    Do the calculations for part 1 of the puzzle

    :param input_file_name: the input file to complete
    :return: the similarity score of the input file
    """
    pass
