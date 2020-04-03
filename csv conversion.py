import csv
names = ["filename", "composer", "genre_id"]

csv_data = read_csv(
    'metadata.csv',
    names = names,
    sep=",")

for i in csv_data:
	