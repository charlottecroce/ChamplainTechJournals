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
        imported = None

        def p1(inputs, output, message):
            nonlocal imported
            self.io_setup(inputs)
            if imported:
                importlib.reload(imported)
            else:
                imported = importlib.import_module('part1')

            x = self.io_output()
            assert output in x, message
            self.io_teardown()

        for num in ('10', '4', '9'):
            result = "".join([str(x) + '\n' for x in range(int(num), 0, -1)])[0:-1]
            p1([num], result, f'Part 1 x={num} should print: {result.__repr__()}')

    def test_part2(self):
        imported = None

        def p2(inputs, output, message):
            nonlocal imported
            self.io_setup(inputs)
            if imported:
                importlib.reload(imported)
            else:
                imported = importlib.import_module('part2')

            x = self.io_output()
            assert output in x, message
            self.io_teardown()

        for a, b in (('1', '10'), ('4', '9')):
            result = "".join([str(x) + '\n' for x in range(int(a), int(b)+1)])[0:-1]
            p2([a, b], result, f'Part 2 a={a}, b={b} should print: {result.__repr__()}')

    def test_part3(self):
        from part3 import all_squares
        for param, result in [(50, [1, 4, 9, 16, 25, 36, 49]), (9, [1, 4, 9])]:
            assert all_squares(param) == result, f'Part 3: all_squares({param}) should equal {result}'

    def test_part4(self):
        imported = None

        def p4(inputs, output, message):
            nonlocal imported
            self.io_setup(inputs)
            if imported:
                importlib.reload(imported)
            else:
                imported = importlib.import_module('part4')

            x = self.io_output()
            assert output in x, message
            self.io_teardown()

        sample_names = ['Barry, Barbara', 'Sally, Sajid, Solomon']
        results = ['Hello Barry\nHello Barbara', 'Hello Sally\nHello Sajid\nHello Solomon']
        for names, result in zip(sample_names, results):
            p4([names], result, f'Part 4 Names: {names} should print: {result.__repr__()}')

    def test_part5(self):
        from part5 import num_distinct_elements
        for param, result in [([2, 5, 5, 7, 2, 9.5, 2, 4], 5), ([2, 1, 1, 7, 1, 9.5, 2, 1], 4)]:
            assert num_distinct_elements(param) == result, f'Part 5: num_distinct_elements({param}) should equal {result}'

    def test_part6(self):
        from part6 import fibonacci
        for param, result in [(6,8),(3,2),(1,1),(7,13)]:
            assert fibonacci(param) == result, f'Part 6:fibonnaci({param}) should equal {result}'