import pytest
from practice_2024 import (
    do_part_1,
    do_part_2,
    generate_file_data,
    extract_values_from_line,
    FileData,
)


class Test2024Day1:
    @pytest.mark.parametrize(
        "file_name,expected_answer",
        [("simple_input_practice.txt", 11), ("input_practice.txt", 1530215)],
    )
    def test_basic_answer_part_1(self, file_name, expected_answer):
        """
        Tests that running the part 1 function gets me the right answer
        """
        assert do_part_1(file_name) == expected_answer

    @pytest.mark.parametrize(
        "file_name,expected_answer",
        [("simple_input_practice.txt", 31), ("input_practice.txt", 26800609)],
    )
    def test_basic_answer_part_2(self, file_name, expected_answer):
        """
        Tests that running the part 2 function gets me the right answer
        """
        assert do_part_2(file_name) == expected_answer

    def test_read_file(self):
        """
        Tests that reading the data from a test file gives the correct FileData object
        """
        file_data = generate_file_data("simple_input_practice.txt")
        assert file_data.left_list == [3, 4, 2, 1, 3, 3]
        assert file_data.right_list == [4, 3, 5, 3, 9, 3]

    def test_extract_values_from_line(self):
        """
        Tests that the correct values are extracted from a given line
        """
        assert extract_values_from_line("80784   47731") == (80784, 47731)


class TestFileData:
    """
    Tests the FileData class
    """

    @pytest.mark.parametrize(
        "list1,list2,expected_distance",
        [
            ([1, 2, 3], [3, 2, 1], 0),
            ([1, 2, 3], [1, 2, 3], 0),
            ([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3], 11),
        ],
    )
    def test_total_distance(self, list1, list2, expected_distance):
        """
        Tests that the total_distance function generates the correct value
        """
        file_data = FileData(list1, list2)
        assert file_data.total_distance == expected_distance

    @pytest.mark.parametrize(
        "list1,list2,expected_score",
        [
            ([1, 2, 3], [3, 2, 1], 6),
            ([1, 2, 3], [1, 2, 3], 6),
            ([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3], 31),
        ],
    )
    def test_similarity_score(self, list1, list2, expected_score):
        """
        Tests that the similarity_score function generates the correct value
        """
        file_data = FileData(list1, list2)
        assert file_data.similarity_score == expected_score
