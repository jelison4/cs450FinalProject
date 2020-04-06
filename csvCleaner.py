from pandas import read_csv, DataFrame
import csv

def filter(composer, filename):
    with open("csvData/"+ composer + "/" + filename) as inFile:
        reader=csv.reader(inFile)
        with open("cleanCsv/"+ composer + "/" + filename, 'w', newline ='') as outFile:
            writer = csv.writer(outFile)
            for row in reader:
                if (len(row) == 6):
                    writer.writerow(row[3:])


names = ["filename", "composer", "genre_id"]

csv_data = read_csv(
    "metadata.csv",
    names = names,
    sep=",")

names = ["filename", "composer", "genre_id"]

csv_data = read_csv(
    'metadata.csv',
    names = names,
    sep=",")

for filename, composer, genre_id in zip(csv_data.filename, csv_data.composer, csv_data.genre_id):
    filter(composer, filename[:-4]+".csv")
