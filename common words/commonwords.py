import matplotlib.pyplot as plt
def dici(file_name):
    f = open("dictionary.csv", "w+")  # opening the file with w+ mode truncates the file
    f.close()  # close file
    d = dict()
    my_file = open(file_name, "r")
    data = my_file.read()
    # replacing end of line('/n') with ' ' and
    # splitting the text it further when '.' is seen.
    data = data.lower()
    data = data.replace(",", " ")
    data_into_list = data.replace('\n', ' ').split(" ")

    # printing the data

    for word in data_into_list:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1

    sortedDict = sorted(d.items(), key=lambda x: x[1], reverse=True)
    print(sortedDict)
    with open("dictionary.csv", "a") as f:  # open dcitionary frist.csv in apened mode
        for key, value in sortedDict:
            if str(key) != "":
                f.write(str(key) + "," + str(value) + "\n")
def plotly_graph():
    # graph stuff
    heights = []  # how tall the values on the graph are
    bar_labels = []  # labels for values
    left_coordinates = []  # number of values
    counter = 1  # counter for number of values
    with open("dictionary.csv", "r") as r:  # open file and set that to r

        for line in r:  # for line in r
            if counter== 11:
                break
            collums = line.split(",")  # split line at ,
            numb = collums[1].split("\n")  # split line at \n
            bar_labels.append(collums[0])  # add stuff to list
            heights.append(int(numb[0]))  # add stuff to list
            left_coordinates.append(int(counter))  # add stuff to list
            counter += 1  # add 1 counter
    plt.bar(left_coordinates, heights, tick_label=bar_labels, width=0.6, color=['blue'])  # info for bar
    plt.xlabel('words')# x axis
    plt.ylabel('Number of times word shows up') #y axis
    plt.title("Most common words")# tile of graph
    plt.show()# show graph
def main():
    print("input txt file name \n ex quote.txt")
    while True:
        try:
            file_name=input()
            dici(file_name)
            plotly_graph()

            break
        except:
            print("not vaild file name try again")

if __name__ == "__main__":
    main()
