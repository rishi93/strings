from matplotlib import pyplot as plt

path1 = 'Task1/U10S1.TXT'

def create_string(pathname):
    fo = open(pathname)
    lines = fo.readlines()

    x, y = [], []

    # Populate the x and y array
    for line in lines[1:]:
        x_val, y_val, time_val, button_val = line.split(' ')
        x.append(int(x_val))
        y.append(int(y_val))

    '''
    print(x)
    print(y)
    '''

    x_symbol = ['-'] * len(x)
    y_symbol = ['-'] * len(y)
    merged_symbol = ['-'] * len(x)

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

    '''
    print(x_symbol)
    print(y_symbol)
    '''

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
    '''
    print(merged_symbol)
    '''

    final_string = ""

    for elem in merged_symbol:
        if elem != '-':
            final_string += elem
    '''
    print(final_string)
    '''
    return final_string

string1 = create_string(path1)

print(string1)

'''
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, y, 'bo')
plt.show()
plt.close()
'''
