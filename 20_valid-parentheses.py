class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for i in s:
            if i in d:
                stack.append(i)
                # print(f'stack ke-{s.index(i)} => {stack}')
            elif len(stack) == 0 or d[stack.pop()] != i:
                return False
        return len(stack) == 0


if __name__ == "__main__":
    test = Solution()

    s1 = "()"
    # Output: true

    s2 = "()[]{}"
    # Output: true

    s3 = "(]"
    # Output: false

    s4 = "([])"
    # Output: true

    s5 = "(([]){})"
    # Output: true

    print(test.isValid(s1))
    print(test.isValid(s2))
    print(test.isValid(s3))
    print(test.isValid(s4))
    print(test.isValid(s5))
