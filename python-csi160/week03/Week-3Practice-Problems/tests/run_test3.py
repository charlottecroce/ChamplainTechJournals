import io
import sys
import importlib
from math import isclose

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

        p1(['79'], '7 9', "Part 1: 79 should print '7 9'")
        p1(['20'], '2 0', "Part 1: 20 should print '2 0'")

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

        p2(['79'], '97', "Part 2: 79 should print '97'")
        p2(['24'], '42', "Part 2: 24 should print '42'")

    def test_part3(self):
        imported = None

        def p3(inputs, output, message):
            nonlocal imported
            self.io_setup(inputs)
            if imported:
                importlib.reload(imported)
            else:
                imported = importlib.import_module('part3')

            x = self.io_output()
            assert output in x, message
            self.io_teardown()

        p3(['792'], '18', "Part 3: 792 should print '18'")
        p3(['914'], '14', "Part 3: 914 should print '14'")
        p3(['100'], '1', "Part 3: 100 should print '1'")

    def test_part4(self):
        import part4
        for param, result in ((4, 96), (3, 72)):
            assert part4.days_to_hours(param) == result, f'Part 4: days_to_hours({param}) should equal {result}'
        for param, result in ((2, 2880), (3, 4320)):
            assert part4.days_to_minutes(param) == result, f'Part 4: days_to_minutes({param}) should equal {result}'
        for param, result in ((4, 345600), (2, 172800)):
            assert part4.days_to_seconds(param) == result, f'Part 4: days_to_seconds({param}) should equal {result}'

    def test_part5(self):
        import part5
        for param, result in ((20.0, 68.0), (1, 33.8), (-5.7, 21.74)):
            assert isclose(part5.celsius_to_fahrenheit(param), result, rel_tol=0.05), f'Part 5: celsius_to_fahrenheit({param}) should equal {result}'

    def test_part6(self):
        import part6
        try:
            assert isclose(part6.volume_cone(radius=2, height=3),12.566370614359172, rel_tol=0.05), 'Part 6: Radius of 2 and Height of 3 should yield 12.566370614359172'

        except (NameError, AttributeError):
            assert False, 'Part 6: Function not defined, check that the function name is correct'

        except TypeError:
            assert False, 'Part 6: Function improperly defined, likely the function parameters are incorrect'


