import csv

file_names = ['data/part1.csv', 'data/part2.csv', 'data/part3.csv']

for file_name in file_names:
    with open(file_name, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        total_us_tagged = 0
        total_rows = 0
        total_agreement = 0
        for row in csvreader:
            total_rows += 1
            if total_rows > 1:
                our_tag = row[-1].strip()
                their_tag = row[-2].strip()
                if our_tag == "NNP":
                    our_tag = "NP"
                elif our_tag == "NNPS":
                    our_tag = "NPS"
                elif our_tag == "PRP":
                    our_tag = "PP"
                elif our_tag == "PRP$":
                    our_tag = "PP$"
                elif our_tag == ".":
                    our_tag = "SENT"
                if len(our_tag) > 0:
                    total_us_tagged += 1
                    if our_tag == their_tag or (our_tag == "VB" and their_tag == "VBP"):
                        total_agreement += 1

        print("Total tagged for file " + file_name + ": " + str(total_us_tagged) + " of " + str(total_rows) + " total rows")
        print("Agreement: " + str(total_agreement) + " tokens (" + str(total_agreement / total_us_tagged * 100) + "%)")
