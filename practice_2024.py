from dataclasses import dataclass
import string


@dataclass
class FileData:
    left_list: list[int]
    right_list: list[int]

    @property
    def similarity_score(self) -> int:
        """
        Return the similarity score of the file

        :return: the similarity score
        """
        sorted_left_list = sorted(self.left_list)
        sorted_right_list = sorted(self.right_list)
        total_score = 0
        for left_val, right_val in zip(sorted_left_list, sorted_right_list):
            total_score += abs(left_val - right_val)
        return total_score


DEFAULT_FILENAME = "input_practice.txt"


def read_lists(file_name: str = DEFAULT_FILENAME) -> FileData:
    """
    Read a given list file and return a FileData object

    :param file_name: the file name to read from
    :return: a FileData object containing the two lists in the file
    """
    left_list: list[int] = []
    right_list: list[int] = []

    with open(file_name) as f:
        for line in f.readlines():
            line_values = extract_values_from_line(line)
            left_list.append(line_values[0])
            right_list.append(line_values[1])

    return FileData(left_list, right_list)


def extract_values_from_line(line: str) -> tuple[int, int]:
    """
    Extracts two values with whitespace in between

    :param line: the line to extract values from
    :return: a tuple containing both values
    """
    line = line.rstrip()

    left_value = ""
    ix = 0
    while ix < len(line) and line[ix] not in string.whitespace:
        left_value += line[ix]
        ix += 1

    right_value = ""
    ix = len(line) - 1
    while ix > -1 and line[ix] not in string.whitespace:
        right_value = line[ix] + right_value
        ix -= 1

    return int(left_value), int(right_value)


def do_part_1(input_file_name: str = DEFAULT_FILENAME) -> int:
    """
    Do the calculations for part 1 of the puzzle

    :param input_file_name: the input file to complete
    :return: the similarity score of the input file
    """
    file_data = read_lists(input_file_name)

    return file_data.similarity_score
