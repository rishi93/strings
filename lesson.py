"This program calculates edit distance between two signature files"
from matplotlib import pyplot as plt

path1 = 'Task1/U10S1.TXT'
path2 = 'Task1/U10S2.TXT'

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

'''
def edit_distance(string1, string2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if string1[m - 1] == string2[n - 1]:
        return edit_distance(string1, string2, m - 1, n - 1) 
    
    return 1 + min(edit_distance(string1,string2,m,n-1), edit_distance(string1,string2,m-1,n), edit_distance(string1,string2,m-1,n-1))
'''

def edit_distance(string1, string2, m, n):
    dp = [[0 for i in range(0, n + 1)] for j in range(0, m + 1)]

    for i in range(0, m + 1):
        for j in range(0, n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Insert, Remove, Replace
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
    return dp[m][n]

print("Calculating edit distance between strings:")
editDistance = edit_distance(string1, string2, m, n)
final_score = editDistance/(m + n)

print("Edit distance: {}".format(final_score))

'''
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, y, 'bo')
plt.show()
plt.close()
'''
