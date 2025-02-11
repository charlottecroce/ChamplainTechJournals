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
        from part1 import first_element
        try:
            for param, result in [([136, 32.5, 78, -2], 136), ([], None), (['hello'], 'hello')]:
                assert first_element(param) == result, f'Part 1: first_element({param}) should equal {result}'
        except IndexError:
            raise IndexError('Empty list should return None, instead an IndexError is raised')

    def test_part2(self):
        from part2 import second_element
        try:
            for param, result in [([136, 32.5, 78, -2], 32.5), ([], None), (['hello'], None)]:
                assert second_element(param) == result, f'Part 2: second_element({param}) should equal {result}'
        except IndexError:
            raise IndexError('List that does not contain a second element should return None, instead an IndexError is raised')

    def test_part3(self):
        from part3 import last_element
        try:
            for param, result in [([136, 32.5, 78, -2], -2), ([], None), (['hello'], 'hello')]:
                assert last_element(param) == result, f'Part 3: last_element({param}) should equal {result}'
        except IndexError:
            raise IndexError('An empty list should return None, instead an IndexError is raised')

    def test_part4(self):
        from part4 import area_code

        for param, result in [("802-999-3782", "802"), ("617-555-1212", "617")]:
            assert area_code(param) == result, f'Part 4: area_code({param}) should equal {result}'

    def test_part5(self):
        from part5 import last_four_digits

        for param, result in [("802-999-3782", "3782"), ("1-617-555-1212", "1212")]:
            assert last_four_digits(param) == result, f'Part 5: last_four_digits({param}) should equal {result}'

    def test_part6(self):
        from part6 import first_last_name
        for param, result in [("Mae Jemison", ("Mae", "Jemison")), ("Sally Ride", ("Sally", "Ride")),]:
            assert first_last_name(param) == result, f'Part 6: first_last_name({param}) should equal {result}'

    def test_part7(self):
        from part7 import second_smallest
        for param, result in [([9,1,5], 5), ([0.0, 4, 2, 0.0], 0.0)]:
            assert second_smallest(param) == result, f'Part 7: second_smallest({param}) should equal {result}'

    def test_part8(self):
        from part8 import area_code
        for param, result in [("1-410-999-1111", "410"), ("802-555-5555", "802"), ("(802)-555-5555", "802")]:
            assert area_code(param) == result, f'Part 8: area_code({param}) should equal {result}'
