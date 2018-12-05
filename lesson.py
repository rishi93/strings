"This program calculates edit distance between two signature files"
from matplotlib import pyplot as plt

path1 = 'Task1/U11S1.TXT'
path2 = 'Task1/U11S3.TXT'

def create_string(pathname):
    print("Opening the file")
    fo = open(pathname)
    lines = fo.readlines()

    x, y = [], []
    
    print("Reading x and y values")
    # Populate the x and y array
    for line in lines[1:]:
        x_val, y_val, time_val, button_val = line.split(' ')
        x.append(int(x_val))
        y.append(int(y_val))

    x_symbol = ['-'] * len(x)
    y_symbol = ['-'] * len(y)
    merged_symbol = ['-'] * len(x)

    print("Calculating the string from minimas and maximas")
    if x[0] < x[1]:
        x_symbol[0] = 'a'
    if x[0] > x[1]:
        x_symbol[0] = 'b'

    # Check if xi is xmin or ymin
    for i in range(1, len(x) - 1):
        if x[i] < x[i - 1] and x[i] < x[i + 1]:
            x_symbol[i] = 'a'
        elif x[i] > x[i - 1] and x[i] > x[i + 1]:
            x_symbol[i] = 'b'

    if x[len(x) - 1] < x[len(x) - 2]:
        x_symbol[len(x) - 1] = 'a'
    if x[len(x) - 1] > x[len(x) - 2]:
        x_symbol[len(x) - 1] = 'b'

    if y[0] < y[1]:
        y_symbol[0] = 'c'
    if y[0] > y[1]:
        y_symbol[0] = 'd'

    # Check if yi is ymin or ymax
    for i in range(1, len(y) - 1):
        if y[i] < y[i - 1] and y[i] < y[i + 1]:
            y_symbol[i] = 'c'
        elif y[i] > y[i - 1] and y[i] > y[i + 1]:
            y_symbol[i] = 'd'

    if y[len(y) - 1] < y[len(y) - 2]:
        y_symbol[len(y) - 1] = 'c'
    if y[len(y) - 1] > y[len(y) - 2]:
        y_symbol[len(y) - 1] = 'd'

    for i in range(0, len(x)):
        if x_symbol[i] == 'a' and y_symbol[i] == 'c':
            merged_symbol[i] = 'e'
        elif x_symbol[i] == 'a' and y_symbol[i] == 'd':
            merged_symbol[i] = 'f'
        elif x_symbol[i] == 'b' and y_symbol[i] == 'c':
            merged_symbol[i] = 'g'
        elif x_symbol[i] == 'b' and y_symbol[i] == 'd':
            merged_symbol[i] = 'h'
        elif x_symbol[i] == 'a' and y_symbol[i] == '-':
            merged_symbol[i] = 'a'
        elif x_symbol[i] == 'b' and y_symbol[i] == '-':
            merged_symbol[i] = 'b'
        elif x_symbol[i] == '-' and y_symbol[i] == 'c':
            merged_symbol[i] = 'c'
        elif x_symbol[i] == '-' and y_symbol[i] == 'd':
            merged_symbol[i] = 'd'

    final_string = ""

    for elem in merged_symbol:
        if elem != '-':
            final_string += elem

    return final_string

print("Processing signature file 1...")
string1 = create_string(path1)
print("Processing signature file 2...")
string2 = create_string(path2)

m = len(string1)
n = len(string2)

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

print("Calculating edit distance between strings:")
edit_distance = editDistance(string1, string2, m, n)
final_score = edit_distance/(m + n)

print("Edit distance: {}".format(final_score))

'''
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, y, 'bo')
plt.show()
plt.close()
'''
