import os
import csv

dirname = os.path.dirname(__file__)
cereal_csv = os.path.join(dirname, '../Resources/cereal.csv')

#open and read CSV
with open(cereal_csv) as cerealnew_file:
    csv_reader = csv.reader(cerealnew_file, delimiter=',')

    #read the header row 
    csv_header = next(cerealnew_file)
    print(f'Header: {csv_header}')

    #read through each row of data
    for row in csv_reader:

        #convert row to float and compare to grams of fiber
        if float(row[7]) >= 5:
            print(row)