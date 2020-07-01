import csv

filename = "meteorites.csv"
file = open(filename, "r", encoding="utf-8")
contents = csv.reader(file)



processor = [str, int, str, str, float, str, str, float, float, str]


def process_meteorites(contents):
    column_names = next(contents)
    for row in contents:
        processed_data = []
        for proc, data in zip(processor, row):
            try:
                processed_data.append(proc(data))
            except ValueError:
                break

        else:
            meteor = {name: data for name, data in zip(column_names, processed_data)}
            yield meteor



def get_mass(meteor):
    return meteor["mass (g)"]

def get_name_lenght(meteor):
    return len(meteor["name"])

def get_mass_(meteor):
    meteor_name_ = input('Enter meteorite name to search mass: ')
    if meteor_name_ in meteorites:
        return meteor(meteor_name_["mass (g)"])


    

meteorites = process_meteorites(contents)



# largest_mass = max(meteorites, key=get_mass)

search = max(meteorites, key=get_mass_)

# # longest_name = max(meteorites, key=get_name_lenght)

# print()
# print()
# # print("Longest name:", longest_name)
# # print("largest mass:", largest_mass)
print(search)
# print()
# print()


file.close()
