class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanStr = ''.join([c for c in s if c.isalnum()])
        strTup = tuple(cleanStr.lower())

        p1 = 0
        p2 = 0
        if len(strTup) % 2 == 0:
            p1 = len(strTup) // 2 - 1
            p2 = len(strTup) // 2
        else:
            p1 = len(strTup) // 2 - 1
            p2 = len(strTup) // 2 + 1

        print(p1, p2, strTup)

        while not p1 < 0:
            if strTup[p1] != strTup[p2]:
                return False
            p1 -= 1
            p2 += 1

        return True

        