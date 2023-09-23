class BraceBalancer:
    def __init__(self):
        self.braces = ['[', '{', '(', ')', '}', ']']
        self.stack = []

    def doBracesMatch(self, braceA, braceB):
        if braceA == '[' and braceB == ']' or braceA == '{' and braceB == '}' or braceA == '(' and braceB == ')':
            return True
        return False

    def areBracesBalanced(self, braces):
        for brace in [*braces]:
            if not self.stack:
                self.stack.append(brace)
            elif self.doBracesMatch(self.stack[-1], brace):
                _ = self.stack.pop()
            else:
                self.stack.append(brace)
        return (not self.stack)