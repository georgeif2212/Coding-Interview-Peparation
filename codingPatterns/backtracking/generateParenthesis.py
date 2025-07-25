def generateParenthesis(n):
    res = []

    def backtrack(open, close, path):
        if len(path) == 2 * n:
            res.append(path)
            return
        if open < n:
            backtrack(open + 1, close, path + "(")
        if close < open:
            backtrack(open, close + 1, path + ")")

    backtrack(0, 0, "")
    return res


print(generateParenthesis(2))
