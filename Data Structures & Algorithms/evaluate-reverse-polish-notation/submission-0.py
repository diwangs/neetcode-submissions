class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in set(["+", "-", "*", "/"]):
                y = stack.pop()
                x = stack.pop()

                if token == "+":
                    z = x + y
                elif token == "-":
                    z = x - y
                elif token == "*":
                    z = x * y
                elif token == "/":
                    z = int(x / y)

                stack.append(z)
            else:
                stack.append(int(token))

        return stack[-1]