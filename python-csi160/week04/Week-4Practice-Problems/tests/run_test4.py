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
            assert output in x.lower(), message
            self.io_teardown()

        p1(['78'], 'even', "Part 1: 78 should print 'even'")
        p1(['21'], 'odd', "Part 1: 21 should print 'odd'")
        p1(['0'], 'even', "Part 1: 0 should print 'even'")

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

        p2(['79', '105'], '79', "Part 2: n1: 79 n2: 105 should print 79")
        p2(['24', '-2'], '-2', "Part 2: n1: 24, n2: -2 should print -2")

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
            assert output == x.split()[-1], message
            self.io_teardown()

        p3(['792'], '1', "Part 3: 792 should print '1'")
        p3(['0'], '0', "Part 3: 0 should print '0'")
        p3(['-100'], '-1', "Part 3: -100 should print '-1'")

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
            assert output == x.split()[-1], message
            self.io_teardown()

        p4(['2021'], 'YES', "Part 4: 2021 should print 'YES'")
        p4(['2000'], 'NO', "Part 4: 2000 should print 'NO'")
        p4(['2100'], 'YES', "Part 4: 2100 should print 'YES'")
        p4(['1796'], 'NO', "Part 4: 1796 should print 'YES'")

    def test_part5(self):
        from part5 import one_positive
        for params, result in [([20, -3], True), ([-9, -3], False), ([20, 3], False)]:
            assert one_positive(*params) == result, f'Part 5: one_positive({params}) should equal {result}'

    def test_part6(self):
        from part6 import ascending_digits
        for params, result in [([136], True), ([925], False), ([163], False)]:
            assert ascending_digits(*params) == result, f'Part 6: ascending_digits({params}) should equal {result}'

    def test_part7(self):
        imported = None

        def p7(inputs, output, message):
            nonlocal imported
            self.io_setup(inputs)
            if imported:
                importlib.reload(imported)
            else:
                imported = importlib.import_module('part7')

            x = self.io_output()
            assert output == x.split()[-1], message
            self.io_teardown()

        months = range(1, 13)
        days = (31,28,31,30,31,30,31,31,30,31,30,31)
        for month, day in zip(months, days):
            p7([str(month)], str(day), f'Part 7 Month {month} should print {day}')

    def test_part8(self):
        from part8 import is_legal_rook_move
        moves = [((1, 2, 1, 6), True),
                 ((1, 2, 3, 6), False),
                 ((1, 2, 3, 2), True),
                 ((1, 1, 1, 1), False),
                 ((5, 6, 3, 6), True),
                 ((1, 7, 1, 3), True)]
        for params, result in moves:
            assert is_legal_rook_move(*params) == result, f'Part 8: is_legal_rook_move{params} should equal {result}'

    def test_part9(self):
        from part9 import is_legal_king_move
        moves = [((1, 2, 2, 3), True),
                 ((1, 2, 3, 6), False),
                 ((2, 2, 1, 2), True),
                 ((1, 1, 1, 1), False),
                 ((5, 6, 4, 5), True),
                 ((1, 7, 2, 6), True),
                 ((4, 4, 6, 6), False)]
        for params, result in moves:
            assert is_legal_king_move(*params) == result, f'Part 9: is_legal_king_move{params} should equal {result}'

    def test_part10(self):
        from part10 import is_legal_bishop_move
        moves = [((4, 4, 3, 5), True),
                 ((1, 4, 4, 7), True),
                 ((5, 4, 2, 1), True),
                 ((4, 4, 6, 2), True),
                 ((5, 4, 1, 1), False),
                 ((5, 4, 6, 4), False),
                 ((1, 1, 1, 1), False)]
        for params, result in moves:
            assert is_legal_bishop_move(*params) == result, f'Part 10: is_legal_bishop_move{params} should equal {result}'

