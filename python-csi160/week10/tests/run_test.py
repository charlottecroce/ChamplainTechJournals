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

        p1(['32'], "{'location': 'Burlington, VT', 'age': '32', 'first_name': 'John', 'last_name': 'Doe'}", "Part 1: For age=32 expected output was '{'location': 'Burlington, VT', 'age': '32', 'first_name': 'John', 'last_name': 'Doe'}'")

        
    def test_part2(self):
        from part2 import synonym_lookup
        tests = [(((('Hello', 'Hi'), ('Goodbye','Bye'), ('Snake', 'Serpent')), "Serpent"), "Snake"),
                    (((('a', 'A'), ('B','b'), ('C', 'c')), "B"), "b")]

        for params, result in tests:
            assert synonym_lookup(*params) == result, f'Part 2: synonym_lookup({params}) should equal {result}'
    
    
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

        p3([], "{'Miro Weinberger': 570, 'Max Tracy': 603, 'Ali Dieng': 293}", "Part 3: Expected output was '{'Miro Weinberger': 570, 'Max Tracy': 603, 'Ali Dieng': 293}'")


    def test_part4(self):
        from part4 import word_frequency
        tests = [("The silly cat is the silly face.", {'the': 2, 'silly': 2, 'cat': 1, 'is': 1, 'face': 1})]

        for param, result in tests:
            assert word_frequency(param) == result, f'Part 4: word_frequency("{param}") should equal {result}'
    