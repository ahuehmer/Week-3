import os
import csv 

#ask user what book they want 
book = input('What book would you like to search for?')

#set path for file
dirname = os.path.dirname(__file__)
filepath = os.path.join(dirname, '../Resources/comic_books.csv')

#set variable to check if file was found 
found = False

#open csv file
with open(filepath, encoding='utf') as comicnew_file:
    csvreader = csv.reader(comicnew_file, delimiter=',')

    #look for book
    for row in csvreader:
        if row[0] == book:
            print(row[0] + ' was published by ' + row[8] + ' in ' + row[9])

            #set variable to confirm that book was found 
            found = True

    if found is False:
        print('Sorry, we couldnt find it.')