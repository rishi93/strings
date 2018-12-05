def breakdown(c):
    if c >= 'a' and c <= 'd':
        return c
    elif c == 'e':
        return "ac"
    elif c == 'f':
        return "ad"
    elif c == 'g':
        return "bc"
    elif c == 'h':
        return "bd"

def get_weight(c):
    return len(breakdown(c))

def simple_edit_distance(string1, string2, m, n):
    if m == 0:
        return n
    elif n == 0:
        return m
    elif string1[m - 1] == string2[n - 1]:
        return simple_edit_distance(string1, string2, m - 1, n - 1)
    else:
        return 1 + min(simple_edit_distance(string1, string2, m - 1, n), simple_edit_distance(string1, string2, m, n - 1), simple_edit_distance(string1, string2, m - 1, n - 1))

# We treat the substitution between two characters as edit distance between two strings
def get_substition_cost(char1, char2):
    string1 = breakdown(char1)
    string2 = breakdown(char2)

    return simple_edit_distance(string1, string2, len(string1), len(string2))

def editDistance(string1, string2, m, n):
    dp = [[0 for i in range(n + 1)] for i in range(0, m + 1)]

    for i in range(0, m + 1):
        for j in range(0, n + 1):
            # If no characters in string1, then add all characters of string2
            if i == 0:
                total_weight = 0
                for x in range(0, j):
                    total_weight += get_weight(string2[x])
                dp[i][j] = total_weight
           
           # If no characters in string2, then add all characters of string1
            elif j == 0:
                total_weight = 0
                for x in range(0, i):
                    total_weight += get_weight(string1[x])
                dp[i][j] = total_weight
           
           # If the character in string1 and string2 are same, then no need to change anything
            elif string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
           
           # If the character in string1 and string2 are different, then we need to consider removal, insertion and substitution
            else:
                # The cost of removing a character from string1
                removal_cost = get_weight(string1[i - 1]) + dp[i - 1][j]
                addition_cost = get_weight(string2[j - 1]) + dp[i][j - 1]
                substition_cost = get_substition_cost(string1[i - 1], string2[j - 1]) + dp[i - 1][j - 1]
                dp[i][j] = min(removal_cost, addition_cost, substition_cost)

    return dp[m][n] 

string1, string2 = "add", "ahg"
m,n = len(string1), len(string2)

result = editDistance(string1, string2, m, n)

print(result)
