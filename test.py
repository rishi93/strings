from matplotlib import pyplot as plt

# Read file with all path names
all_fo = open('allfiles.txt', 'r')
lines = all_fo.readlines()
all_fo.close()

for line in lines[1000:]:
    # Remove the last character of the line
    path = line[:-1] 
    # Read the contents of file
    fo = open("Task1/" + path) 
    data_lines = fo.readlines()
    x, y = [], []

    print("Plotting " + path)

    for data_line in data_lines[1:]:
        x_val, y_val, time_val, button_val = data_line.split(' ')
        x.append(int(x_val)/50)
        y.append(int(y_val)/50)

    fig = plt.figure()
    fig.suptitle('path')
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x, y, 'bo')

    plt.savefig("Task1_images/" + path[:-3] + "png")
    plt.close()
