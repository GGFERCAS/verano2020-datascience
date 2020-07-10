
import csv
from matplotlib import pyplot


filename = "fatal-police-shootings-data.csv"
file = open(filename, "r", encoding="utf-8")
contents = csv.reader(file)

policemen = []
column_names = next(contents)
for row in contents:
    policeman = {
        "id": row[0],
        "name": row[1],
        "date": row[2],
        "manner_of_death": row[3],
        "armed": row[4],
        "age": row[5],
        "gender": row[6],
        "race": row[7],
        "city": row[8],
        "state": row[9],  
        "signs_of_mental": row[10],    
        "threat_level": row[11],  
        "flee": row[12], 
        "body_camera": row[13],  
    }
    if not policeman["age"] == '':
        policeman["age"] = int(policeman["age"])
    else:
        continue

    policemen.append(policeman)


def age_policeman(policeman):
    return policeman["age"]


def average_age(policeman):
    ages = list(map(age_policeman, policemen))
    total_ages = sum(ages)
    number_of_ages = len(ages)
    average_ages = total_ages / number_of_ages
    print(average_ages)

average_age(policeman)
x_axis = policeman["city"]
y_axis = policeman["thread_level"]

pyplot.char()