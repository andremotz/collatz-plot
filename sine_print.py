import matplotlib.pyplot as plt
import math


def main():
    f = plt.figure()
    counter = 0
    items_x = []
    items_y = []
    while counter < math.pi*2:
        items_x.append(counter)
        items_y.append(math.sin(counter))
        counter += .01

    plt.plot(items_x, items_y, 'o', color='black', markersize=1)
    f.savefig("/Users/andremotz/Desktop/plot-sin-1.pdf", bbox_inches='tight')

    plt.show()

if __name__ == "__main__":
    main()