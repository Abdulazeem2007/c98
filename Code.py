def word_Counter():
    fileName = input("Please Give the filename of The File you want us to count the words.  ")
    File_object= open(fileName,'r')
    number = 0
    for line in File_object:
        words= line.split()
        number= number + len(words)
        print (words)
    print(number)

word_Counter()