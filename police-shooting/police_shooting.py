
import csv

filename = "fatal-police-shooting.data.csv"
file = open(filename, "r", encoding="utf-8")
contents = csv.reader(file)

processors = [int, str, str, str, int, str, str, str]