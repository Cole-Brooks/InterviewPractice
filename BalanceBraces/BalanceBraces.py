class BalanceBraces:
    def __init__(self):
        self.braces = ['[', '{', '(', ')', '}', ']']
        self.stack = []

    def clean_stack(self):
        self.stack = []

    def do_braces_match(self, braceA, braceB):
        if braceA == '[' and braceB == ']' or braceA == '{' and braceB == '}' or braceA == '(' and braceB == ')':
            return True
        return False

    def massage_inputs(self, braces):
        '''
        Takes a string 'braces' as input. Outputs a list of brace characters. Other characters are not
        looked at when we're determining if braces are balanced.
        '''
        return [brace for brace in [*braces] if brace in self.braces]


    def are_braces_balanced(self, braces):
        for brace in self.massage_inputs(braces):
            if not self.stack:
                self.stack.append(brace)
            elif self.do_braces_match(self.stack[-1], brace):
                _ = self.stack.pop()
            else:
                self.stack.append(brace)
        balanced = not self.stack
        self.clean_stack()
        return (balanced)
    
def test_against_sample_input(test_string):
    braceBalancer = BalanceBraces()
    print(test_string)
    print(braceBalancer.are_braces_balanced(test_string))

if __name__=="__main__":
    sample_input = "[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()[({[()()]})]()"
    test_against_sample_input(sample_input)