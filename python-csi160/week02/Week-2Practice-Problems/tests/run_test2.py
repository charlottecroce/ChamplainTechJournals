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
        inputs = ['5','7','3']
        self.io_setup(inputs)
        import part1
        assert self.io_output()[-2:] == "15", 'Input of 5, 7, 3 should have resulted in 15'
        self.io_teardown()
        
    def test_part2(self):
        self.io_setup(['John'])
        import part2
        assert self.io_output().split('\n')[-1] == "Hello, John!", 'Input of "John" expected result "Hello, John!"'
        self.io_teardown()

    def test_part3(self):
        self.io_setup(['258'])
        import part3
        output = self.io_output()
        try:
            line1 = output.split('\n')[-2]
            line2 = output.split('\n')[-1]
        except:
            line1, line2 = None, None
        assert line1 == "The next number for the number 258 is 259", \
            'line1 expected: "The next number for the number 258 is 259"'
        assert line2 == "The previous number for the number 258 is 257", \
            'line 2 expected: "The previous number for the number 258 is 257"'

        self.io_teardown()

    def test_part4(self):
        inputs = ['10', '2']
        self.io_setup(inputs)
        import part4
        output = self.io_output().split()[-1]
        try:
            output = float(output)
        except:
            print('Unable to convert output to an int')

        assert output == 10.0, 'Base 10.0, Height 2.0 should yield Area 10.0'

        self.io_teardown()

    def test_part5(self):
        inputs = ['4', '17']
        self.io_setup(inputs)
        import part5
        output = self.io_output().split('\n')

        assert output[-1] == '1', "With 4 students and 17 apples, we would expect 1 left in the basket"
        assert output[-2].split()[-1] == '4', "With 4 students and 17 apples, we would expect 4 apples per student"

        self.io_teardown()

    def test_part6(self):
        imported = None
        def p6(input,output,message):
            nonlocal imported
            inputs = [input]
            self.io_setup(inputs)
            if imported:
                importlib.reload(imported)
            else:
                imported = importlib.import_module('part6')

            x = self.io_output()
            assert x == output, message
            self.io_teardown()
        p6('12345', '3 205', "12345 seconds past midnight is should print '3 205'")
        p6('86010', '23 1433', "86010 seconds past midnight is should print '23 1433'")

    def test_part7(self):
        imported = None
        def p7(inputs,output,message):
            nonlocal imported
            self.io_setup(inputs)
            if imported:
                importlib.reload(imported)
            else:
                imported = importlib.import_module('part7')

            x = self.io_output()
            assert x == output, message
            self.io_teardown()
        p7(['2', '50', '4'], '10 0', "$2 and 50cents 4 cupcakes should print '10 0'")
        p7(['3000', '99', '3000'], '9002970 0', "$3000 and 99 cents should print '9002970 0'")
