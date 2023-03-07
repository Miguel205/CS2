import numpy as np
import matplotlib.pyplot as plt
def dici(file_name,dictionary_file):
    '''
    :param file_name: the name of the file
    :return: dictionary the words in the file
    '''
    f = open(dictionary_file, "w+")                                                 # opening the file with w+ mode truncates the file
    f.close()  # close file
    d = dict()
    my_file = open(file_name, "r")                                                   # opens file
    data = my_file.read()                                                            # reads file
    data = data.lower()                                                              # lower case all the text
    data = data.replace(",", "")                                                    # replace all commas
    data = data.replace(".", "")                                                    # replace all periods
    data_into_list = data.replace('\n', ' ').split(" ")                              # replace the enters  with spaces and split data into spaces



    for word in data_into_list:                                                     # for word in the file
        if str(word) not in d:                                                      # if the word is not already in the dictionary
            d[str(word)] = 1                                                        # give the word a value of one
        else:
            d[str(word)] += 1                                                       # add one to word's value

    sortedDict = sorted(d.items(), key=lambda x: x[1], reverse=True)                # sort the items in the dictionary then reverse the order
    print(sortedDict)
    with open(dictionary_file, "a") as f:                                          # open dictionary.csv in append mode
        for key, value in sortedDict:                                               #for word and value in the dictionary
            if str(key) not in \
                    ["","the","you","and","or","to","of","my",
                     "that","i","in","thy","thou","with","for",
                     "is","a","not","but","thee","so","be","as",
                     "all","me","which","it","his","when","this","by","your","do","from","on","have","then","if","are"] :                                                      # if word is a space
                f.write(str(key) + "," + str(value) + "\n")                         #add word and value to dictionary.csv
def plotly_graph():
    '''

    :return: graph of dictionary file
    '''
    heights = []                                             # how tall the values on the graph are
    bar_labels = []                                          # labels for values
    left_coordinates = []                                    # number of values
    counter = 1                                              # counter for number of values
    with open("dictionary.csv", "r") as r:                   # open file and set that to r

        for line in r:                                       # for line in r
            if counter== 11:
                break
            collums = line.split(",")                        # split line at ,
            numb = collums[1].split("\n")                    # split line at \n
            bar_labels.append(collums[0])                    # add stuff to list
            heights.append(int(numb[0]))                     # add stuff to list
            left_coordinates.append(int(counter))            # add stuff to list
            counter += 1                                     # add 1 counter
    plt.bar(left_coordinates, heights, tick_label=bar_labels, width=0.6, color=['blue'])  # info for bar
    plt.xlabel('words')# x axis
    plt.ylabel('Number of times word shows up')              #y axis
    plt.title("Most common words")                           # tile of graph
    plt.show()                                               # show graph
def matpie(file_name):
    '''

    :param file_name: name of the file
    :return: a list of numbers and a list of words that can be graphed
    '''
    word=[]                                                            #list of words
    num=[]                                                             #list of numbers
    counter=0
    dicti_one=open(file_name,"r")
    for line in dicti_one:                                             #for line in file
        line=line.split(",")                                           #split csv in comma
        if counter <11:                                                #run code for ten times
            word.append(line[0])                                       #add word to list
            num.append(line[1].replace("\n",''))                       #add number to list
            counter+=1
    y = np.array(num)                                                   # numbers for chart
    return y,word
def plot(y,y2,word,word2,filename,filename2):
    fig, axs=plt.subplots(2)
    axs[0].pie(y, labels=word)                                          #make a pie char with the list of words and numbers
    axs[0].set_title(filename)                                           #label for graph
    axs[1].set_title(filename2)                                           #label for graph
    axs[1].pie(y2, labels=word2)                                         #make a pie char with the list of words and numbers
    plt.show()#show the graph'''
def main():
    '''
    :return:     function takes two file makes a directory for each and then graphs them both
    '''
    print("input txt file name \n ex quote.txt")
    while True:
        try:
            file_name=input()
            dici(file_name,"dictionary.csv")

            break
        except:
            print("not valid file name try again")
    print("input txt file name \n ex quote.txt")
    while True:
        try:
            file_name2=input()
            dici(file_name2,"dictionary2.csv")
            break
        except:
            print("not valid file name try again")
    y=matpie("dictionary.csv")[0]
    word=matpie("dictionary.csv")[1]
    y2=matpie("dictionary2.csv")[0]
    word2=matpie("dictionary2.csv")[1]
    plot(y,y2,word,word2,file_name,file_name2)

if __name__ == "__main__":
    main()