import csv

filename = "meteorites.csv"
file = open(filename, "r", encoding="utf-8")
contents = csv.reader(file)



meteorites = []
processor = [str, int, str, str, float, str, str, float, float, str]

column_names = next(contents)
for row in contents:
    processed_data = []
    for proc, data in zip(processor, row):
        try:
            processed_data.append(proc(data))
        except ValueError:
            continue
#    meteor = {column_names[i]: row[i] for i in range(len(column_names))}
#    meteor = {column_names[i]: row[i] for i in zip(column_names, row)}
    meteor = {name: data for name, data in zip(column_names, processed_data)}

   #region meteor = {
   #    "name": row[0],
   #    "id": row[1],
   #    "nametype": row[2],
   #    "recclass": row[3],
   #    "mass (g)": row[4],
   #    "fall": row[5],
   #    "year": row[6],
   #    "reclat": row[7],
   #    "reclong": row[8],
   #    "GeoLocation": row[9],
   #    
   # endregion}




    meteorites.append(meteor)


def get_mass(meteor):
    return meteor["mass (g)"]

def get_name_lenght(meteor):
    return len(meteor["name"])


largest_mass = max(meteorites, key=get_mass)

longest_name = max(meteorites, key=get_name_lenght)

print("largest mass:", largest_mass)
print("Longest name:", longest_name)

file.close()
