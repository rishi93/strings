from matplotlib import pyplot as plt

fo = open('Task1/U10S1.TXT')
lines = fo.readlines()

x, y = [], []

# Populate the x and y array
for line in lines[1:]:
    x_val, y_val, time_val, button_val = line.split(' ')
    x.append(int(x_val)/50)
    y.append(int(y_val)/50)

x_symbol = [0] * len(x)
y_symbol = [0] * len(y)

# Check if xi is xmin or ymin
for i in range(1, len(x) - 1):
    if x[i] < x[i - 1] and x[i] < x[i + 1]:
        x_symbol[i] = 'a'
    elif x[i] > x[i - 1] and x[i] > x[i + 1]:
        x_symbol[i] = 'b'

# Check if yi is ymin or ymax
for i in range(1, len(y) - 1):
    if y[i] < y[i - 1] and y[i] < y[i + 1]:
        y_symbol[i] = 'c'
    elif y[i] > y[i - 1] and y[i] > y[i + 1]:
        y_symbol[i] = 'd'

'''
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, y, 'bo')
plt.show()
plt.close()
'''
