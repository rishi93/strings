from matplotlib import pyplot as plt

# Read file with all path names
all_fo = open('allfiles.txt', 'r')
lines = all_fo.readlines()
all_fo.close()

# Only running for first 10 files, can run for 1600 files also
for line in lines[0:10]:
    # Remove the last character of the line
    path = line[:-1]

    # Read the contents of file
    fo = open("Task1/" + path, 'r') 
    data_lines = fo.readlines()
    fo.close()
    x, y = [], []

    print("Plotting " + path[:-4])
    
    # Plotting the file
    for data_line in data_lines[1:]:
        x_val, y_val, time_val, button_val = data_line.split(' ')
        x.append(int(x_val))
        y.append(int(y_val))
    
    fig = plt.figure()
    fig.suptitle('path')
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x, y, 'bo')

    # Saving the plot and closing the plot
    plt.savefig("Task1_images/" + path[:-3] + "png")
    plt.close()

    print("Calculating velocity and acceleration for " + path[:-4])

    vx = [0 for x in range(0, len(x))]
    vy = [0 for y in range(0, len(y))]
    ax = [0 for x in range(0, len(x))]
    ay = [0 for y in range(0, len(y))] 

    # Calculating velocity
    for i in range(1, len(x)):
       vx[i] = (x[i] - x[i - 1])/10
       vy[i] = (y[i] - y[i - 1])/10

    # Calculating acceleration
    for i in range(2, len(x)):
        ax[i] = (vx[i] - vx[i - 1])/10
        ay[i] = (vy[i] - vy[i - 1])/10

    # Writing velocity and acceleration to file
    fo = open("Task1/" + path[:-4] + "_vel_acc.TXT", 'w')
    for i in range(0, len(x)):
        fo.write(("%d %d %.2f %.2f %.2f %.2f \n" %(x[i], y[i], vx[i], vy[i], ax[i], ay[i]))) 
    fo.close()
