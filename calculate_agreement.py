import csv

file_names = ['data/part1.txt']#, 'data/part2.txt', 'data/part3.txt']

for file_name in file_names:
    with open(file_name + ".csv", 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        total_us_tagged = 0
        total_rows = 0
        total_agreement = 0
        for row in csvreader:
            total_rows += 1
            if total_rows > 1:
                our_tag = row[-1]
                if len(our_tag) > 0:
                    total_us_tagged += 1
                    if our_tag == row[-2]:
                        total_agreement += 1

        print("Total tagged for file " + file_name + ": " + str(total_us_tagged) + " of " + str(total_rows))
        print("Agreement: " + str(total_agreement) + " (" + str(total_agreement / total_us_tagged * 100) + "%)")
