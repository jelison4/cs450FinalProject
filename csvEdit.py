from pandas import read_csv

names = ["filename", "composer", "genre_id"]

csv_data = read_csv(
    'metadata.csv',
    names = names,
    sep=",")

for filename, composer, genre_id in zip(csv_data.filename, csv_data.composer, csv_data.genre_id):
    filepath = "csvData/" + composer + "/" + filename[:-4] + ".csv"
    #print(command)
    my_file = open(filepath)
    string_list = my_file.readlines()
    print(string_list[30])