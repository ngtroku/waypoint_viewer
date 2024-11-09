import csv, sys
import matplotlib.pyplot as plt

def read_csv(file_name):
    x, y = [], []
    status = []
    with open(file_name, newline='', encoding='utf-8') as file:
        reader = csv.reader(file) 
        for row in reader:
            x.append(float(row[0]))
            y.append(float(row[1]))
            status.append(int(row[-1]))
    return x, y, status

if __name__ == "__main__":
    file_name = sys.argv[1]

    x, y, status = read_csv(file_name)
    xmin, xmax = min(x), max(x)
    ymin, ymax = min(y), max(y)

    fig, ax = plt.subplots()

    ax.plot(x, y, marker="o")

    for i, (xi, yi) in enumerate(zip(x, y), start=1):
        if i % 2 != 0:
            if status[i] == 1:
                ax.text(xi+1, yi-7, str(i) + ",stop" , fontsize=9, ha='left', va='bottom', color="red")
            else:
                ax.text(xi+1, yi+3, str(i), fontsize=9, ha='left', va='bottom')

    ax.set_title('Waypoints')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_xlim(xmin-20, xmax+20)
    ax.set_ylim(ymin-20, ymax+20)

    plt.show()
