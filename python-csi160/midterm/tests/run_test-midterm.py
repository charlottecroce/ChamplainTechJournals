import io
import sys
import importlib

class TestSelfPaced:

    def io_setup(self, input_values):
        """Hijack stdout and stdin for simple autograding"""
        def faux_input():
            return input_values.pop(0)
        self.capturedOutput = io.StringIO() 
        sys.stdout = self.capturedOutput      
        sys.stdin.readline = faux_input

    def io_output(self):
        output = self.capturedOutput.getvalue().strip()
        self.capturedOutput = io.StringIO() 
        sys.stdout = self.capturedOutput  
        return output

    def io_teardown(self):
        """restore stdin and stdout"""
        sys.stdout = sys.__stdout__                   
        sys.stdin = sys.__stdin__

    def test_part1(self):
        from part1 import calculate_discounted_price
        for price, discount, result in [(250, 10, 225.0), (50, 50, 25.0), (100, 0, 100.0)]:
            assert calculate_discounted_price(price, discount) == result, f'Part 1: calculate_discounted_price('f'{price}, {discount}) should equal {result}'

    def test_part2(self):
        from part2 import divide_and_remainder
        for num, base, result in [(10, 3, (3, 1)), (10, 2, (5, 0))]:
            assert divide_and_remainder(num, base) == result, f'Part 2: divide_and_remainder({num}, {base}) should equal {result}'

    def test_part3(self):
        from part3 import lucas
        for param, result in [(0,2), (1,1), (2,3), (5,11), (10,123)]:
            assert lucas(param) == result, f'Part 3: lucas({param}) should equal {result}'

    def test_part4(self):
        from part4 import last2
        for param, result in [['red', 'blue', 'green', 'yellow'], 'green'], [[0,1], 0], [[0], None]:
            assert last2(param) == result, f'Part 4: last2({param}) should equal {result}'

    def test_part5(self):
        from part5 import median

        for param, result in [([1, 4, 5, 2, 3], 3), ([1, 2, 3, 4, 5, 6], 3.5), ([7, 3, 2, 5, 4, 6, 1], 4)]:
            assert median(param) == result, f'Part 5: median({param}) should equal {result}'

    def test_part6(self):
        from part6 import manage_playlist
        for playlist, new_song, search, result in [(['Dream On', 'Bohemian Rhapsody', 'Stairway to Heaven'], 'Hotel California', 'Bohemian Rhapsody', 1), (['Imagine', 'Confortably Numb'], 'Wish You Were Here', 'Wish You Were Here', 2), (['Imagine', 'Confortably Numb'], 'Wish You Were Here', 'Smoking on the Water', None)]:
            assert manage_playlist(playlist, new_song, search) == result, f'Part 6: manage_playlist({playlist}, {new_song}, {search}) should equal {result}'
            assert playlist[-1] == new_song, f'Part 6: manage_playlist({playlist}, {new_song}, {search}) should have {new_song} at the end of the playlist'

    def test_part7(self):
        from part7 import split_full_name
        for param, result in [("John Doe", ("Doe", "John")), ("John Doe Smith", ("Smith", "John")), ("John", ("John","")),("John Doe Smith Lee", ("Lee", "John"))]:
            assert split_full_name(param) == result, f'Part 7: split_full_name({param}) should equal {result}'

    def test_part8(self):
        from part8 import countdown
        for param, result in [(-1, []), (0, [0]), (5, [5, 4, 3, 2, 1, 0]), (10, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])]:
            assert countdown(param) == result, f'Part 8: countdown({param}) should equal {result}'

    def test_part9(self):
        from part9 import above_main_diagonal
        for param, result in [([[1, 1, 1],[1, 1, 1],[1, 1, 1]], 3),([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]], 36)]:
            assert above_main_diagonal(param) == result, f'Part 9: above_main_diagonal({param}) should equal {result}'

    def test_part10(self):
        from part10 import spiral_matrix
        for param, result in [(1, [[1]]), (2, [[1, 2],[4, 3]]), (3, [[1, 2, 3],[8, 9, 4],[7, 6, 5]]), (4, [[1,  2,  3,  4],[12, 13, 14, 5],[11, 16, 15, 6],[10, 9,  8,  7]])]:
            assert spiral_matrix(param) == result, f'Part 10: spiral_matrix({param}) should equal {result}'
