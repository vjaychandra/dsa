
def lp(s):

    ans = ""
    n = len(s)
    max_len = 0
    dp = [ [False]*n for _ in range(n) ]

    # single char palindrome
    for i in range(n):
        ans = s[i]
        max_len = 1
        dp[i][i] = True

    # check for s of length 2
    for i in range(n-1):
        if s[i] == s[i+1]:
            max_len = 2            
            ans = s[i:i+2]
            dp[i][i+1] = True

    # check for length > 3
    for j in range(n):
        for i in range(0, j-1):
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                if max_len < j-i+1:
                    max_len = j-i+1
                    ans = s[i:j+1]

    #return "\n".join(map(str, [i for i in dp]))
    return ans



if __name__ == "__main__":
    s = "babad"
    print(lp(s))
