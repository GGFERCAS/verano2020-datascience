
import csv

filename = "fatal-police-shootings-data.csv"
file = open(filename, "r", encoding="utf-8")
contents = csv.reader(file)

processors = [int, str, str, str, str, int, str, str, str, str, str, str, str, str]

for row in contents:
    meteor = {
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
