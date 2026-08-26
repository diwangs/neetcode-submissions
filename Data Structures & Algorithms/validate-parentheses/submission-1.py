class Solution:
    def isValid(self, s: str) -> bool:
        openBracketStack = []

        for bracket in tuple(s):
            if self.isOpenBracket(bracket):
                openBracketStack.append(bracket)
            else:
                if len(openBracketStack) == 0:
                    return False
                lastOpenBracket = openBracketStack[-1]
                if self.doesBracketMatch(lastOpenBracket, bracket):
                    openBracketStack.pop()
                else:
                    return False

        return len(openBracketStack) == 0


    def isOpenBracket(self, c: str) -> bool:
        if c == '(' or c == '{' or c == '[':
            return True
        return False

    def doesBracketMatch(self, o: str, c: str) -> bool:
        if o == '(' and c == ')':
            return True
        elif o == '{' and c == '}':
            return True
        elif o == '[' and c == ']':
            return True
        return False