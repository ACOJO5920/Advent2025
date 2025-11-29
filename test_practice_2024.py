import pytest
from practice_2024 import do_part_1, read_lists, extract_values_from_line, FileData


class Test2024Day1:
    def test_basic_answer(self):
        """
        Tests that running the part 1 function gets me the right answer
        """
        assert do_part_1("input_practice.txt") == 26800609

    def test_read_file(self):
        """
        Tests that reading the data from a test file gives the correct FileData object
        """
        file_data = read_lists("simple_input_practice.txt")
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

    @pytest.mark.parametrize("list1,list2,expected_score", [([1, 2, 3], [3, 2, 1], 0)])
    def test_similarity_score(self, list1, list2, expected_score):
        """
        Tests that the similarity score function generates the correct value
        """
        file_data = FileData(list1, list2)
        assert file_data.similarity_score == expected_score
