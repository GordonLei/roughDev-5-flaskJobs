import csv
import random


file = "occupations.csv"

#Open csv file
reader = csv.reader(open(file))


#Job dictionary
jobs = {}

def returnReader():
        return reader
#creates Dictionary consisting of Jobs as keys and percents as its values
def createDict():
        for rows in reader:
                if rows[0] == "Job Class" or rows[0] == "Total":
                        continue
                else:
                        jobs[rows[0]] = float(rows[1])
        return jobs

#pick a random job based off percentages.
def randomJob(dict):
        randNum = float(random.randint(1,998)/10) #create a random float
        #print randNum
        for keys in dict.keys():
                randNum = randNum - dict[keys]
                if randNum <= 0:
                        #if randNum <0, print out the job that caused this and break the loop
                        return keys
                        break


#pick a frandom job.          
print createDict()
print randomJob(createDict())