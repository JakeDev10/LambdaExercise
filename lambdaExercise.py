import csv
import json
from functools import reduce

f = open('911.csv')
dictionaryObject = csv.DictReader(f)
listOfDictionaries = list(dictionaryObject)
f.close()
#PART 1
#removing blanks and zeroes
cleanedList = list(filter(lambda a: a["zip_code"] != "0" and a["neighborhood"] != "", listOfDictionaries))
cleanedList = list(filter(lambda a: a["dispatchtime"] != '' and a["dispatchtime"] != '0', cleanedList))
cleanedList = list(filter(lambda a: a["totalresponsetime"] != '' and a["totalresponsetime"] != '0', cleanedList))
cleanedList = list(filter(lambda a: a["totaltime"] != '' and a["totaltime"] != '0', cleanedList))

totalDispatch = reduce(lambda time1, time2: time1 + float(time2["dispatchtime"]), cleanedList, 0)
totalResponse = reduce(lambda time1, time2: time1 + float(time2["totalresponsetime"]), cleanedList, 0)
totalTime = reduce(lambda time1, time2: time1 + float(time2["totaltime"]), cleanedList, 0)
print(f"Average dispatch time is {totalDispatch / len(cleanedList)}")
print(f"Average response time is {totalResponse / len(cleanedList)}")
print(f"Average total time is {totalTime / len(cleanedList)}")

#PART 3
f = open('911.json', "w")
json.dump(cleanedList, f)
f.close()

#This writes the dictionary back to a csv
#f = open('911filtered.csv', "w", newline = '')
#writer = csv.DictWriter(f, fieldnames = listOfDictionaries[1])
#writer.writeheader()
#writer.writerows(cleanedList)
#f.close()