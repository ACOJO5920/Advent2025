from practice_2024 import do_part_1


class Test2024Day1:
    def test_basic_answer(self):
        """
        Tests that running the part 1 function gets me the right answer
        """
        assert do_part_1("input_practice.txt") == 26800609
