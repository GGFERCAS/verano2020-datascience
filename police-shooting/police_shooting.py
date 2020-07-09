
import csv

filename = "fatal-police-shootings-data.csv"
file = open(filename, "r", encoding="utf-8")
contents = csv.reader(file)

processors = [int, str, str, str, str, int, str, str, str, str, str, str, str, str]


def process_policemans(contents: csv.reader):
    column_names = next(contents)
    for row in contents:
        processed_data = []
        for proc, data in zip(processors, row):
            try:
                processed_data.append(proc(data))
            except ValueError:
                break
        else:
            police = {name: data for name, data in zip(column_names, processed_data)}
            yield police


policeman = process_policemans(contents)

def get_age(police):
    return police["age"]

def get_manner_of_death(police):
    return police["manner_of_death"]

shoted = 'shot'
def get_all_shoted(police):
    if police["manner_of_death"] == shoted:
        print(police)


if __name__ == '__main__':
    print()

    # policeman_searching = input("Name of the policeman: ")
    # for police in policeman:
    #     if police["name"] == policeman_searching:
    #         print(police)

    # oldest_guy = max(policeman, key=get_age)
    # print(oldest_guy)

    # shoted = 'shot'
    # for police in policeman:
    #     if police["manner_of_death"] == shoted:
    #         print(police)

    # def get_middle_age(police):
    #     all_ages = 


    print()