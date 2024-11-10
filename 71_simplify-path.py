class Solution:
    def simplifyPath(self, path: str) -> str:
        p = path[1:].split('/')
        # print(f'p \t: {p}')
        result = []
        for i in range(len(p)):
            if p[i] == '..' and len(result) == 0:
                continue
            elif p[i] == '..':
                result.pop()
            elif p[i] == '.' or p[i] == '':
                continue
            elif p[i] == '/' or p[i] == '//' or p[i] == '///':
                result.append('/')
            else:
                result.append(p[i])

        # print(f'result \t: {result}')
        return '/' + '/'.join(result)


if __name__ == "__main__":
    test = Solution()

    path1 = "/home/"
    # Output: "/home"

    path2 = "/home//foo/"
    # Output: "/home/foo"

    path3 = "/home/user/Documents/../Pictures"
    # Output: "/home/user/Pictures"

    # path4 = "/../"
    path4 = "/../"
    # Output: "/"

    path5 = "/.../a/../b/c/../d/./"
    # Output: "/.../b/d"

    path6 = "/a/../../b/../c//.//"
    # Output: "/c"

    print(test.simplifyPath(path1))
    print(test.simplifyPath(path2))
    print(test.simplifyPath(path3))
    print(test.simplifyPath(path4))
    print(test.simplifyPath(path5))
    print(test.simplifyPath(path6))
