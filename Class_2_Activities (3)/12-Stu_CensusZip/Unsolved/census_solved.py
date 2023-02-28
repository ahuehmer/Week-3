import os
import csv 

#import file
dirname = os.path.dirname(__file__)
filepath = os.path.join(dirname, '../Resources/census_starter.csv')

#list to store data
place = []
population= []
income =[]
poverty_count = []
poverty_rate = []
county = []
state = []

#open csv file
with open(filepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        place.append(row[0])
        population.append(row[1])
        income.append(row[4])
        poverty_count.append(row[8])

        #determine poverty rate to 2 decimal places, convert to string
        percent = round(int(row[8]) / int(row[1]) * 100, 2)
        poverty_rate.append(str(percent) + "%")

        #split place into county and state 
        split_place = row [0].split(",")
        county.append(split_place[0])
        state.append(split_place[1])

#zip lists together
cleaned_csv = zip( place, population, income, poverty_count, poverty_rate, county, state)

#set variable for output file
output_file = os.path.join("census_final.csv")

#open output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    #write header row
    writer.writerow(["Place", "Population", "Per Capita Income", "Poverty Count", "Poverty Rate", 
                    "County", "Place"])
    
    #write in zipped rows
    writer.writerows(cleaned_csv)