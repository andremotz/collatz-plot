import matplotlib.pyplot as plt

def collatz(number):

    if number % 2 == 0:
        #print(number // 2)
        return number // 2


    elif number % 2 == 1:
        result = 3 * number + 1
        #print(result)
        return result


def main():
    f = plt.figure()
    counter = 1
    #colors = (255, 255, 0)

    items_x = []
    items_y = []
    while counter < 10**6:
        counter += 1
        number_current = counter

        if counter % 10 == 0:
            print(counter)

        counter_collatz = 0
        while number_current != 1:
            counter_collatz += 1
            number_current = collatz(int(number_current))

        items_x.append(counter)
        items_y.append(counter_collatz)


        #plt.scatter(items_x, items_y)
    plt.plot(items_x, items_y, 'o', color='red', markersize=0.1)

    f.savefig("/Users/andremotz/Desktop/collatz_1000000_markersize-0.1.pdf", bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    main()