import csv
import os


full_path = os.path.abspath(__file__)
os.chdir(os.path.dirname(full_path))


filename = "meteorites.csv"
file = open(filename, "r", encoding="utf-8")
contents = csv.reader(file)


processor = [str, int, str, str, float, str, str, float, float, str]


def process_meteorites(contents: csv.reader):
    column_names = next(contents)
    for row in contents:
        processed_data = []
        for proc, data in zip(processor, row):
            try:
                processed_data.append(proc(data))
            except ValueError:
                break

        else:
            meteor = {name: data for name, data in zip(
                column_names, processed_data)}
            yield meteor


meteorites = process_meteorites(contents)


def get_mass(meteor):
    return meteor["mass (g)"]


def get_name_lenght(meteor):
    return len(meteor["name"])

if __name__ == '__main__':


    # meteorite_searched = input("Name of the meteorite: ")
    # for meteor in meteorites:
    #     if meteor["name"] == meteorite_searched:
    #         print(meteor)


    # # longest_name = max(meteorites, key=get_name_lenght)
    # # print("Longest name:", longest_name)

    # print()
    # print()
    largest_mass = max(meteorites, key=get_mass)
    print("largest mass:", largest_mass)

    # print()
    # print()



