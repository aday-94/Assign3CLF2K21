import subprocess
import csv
from typing import List

file_names = ['data/part1.txt', 'data/part2.txt', 'data/part3.txt']

for file_name in file_names:
    file_text = " ".join(open(file_name).read().split("\n"))
    tagged_output: List[str] = subprocess.run('cat ' + file_name + "|" + "tree-tagger-english", stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8').split("\n")
    tagged_output: List[str] = tagged_output[0:]
    print("output:\n" + "\n".join(tagged_output))
    with open(file_name + ".csv", 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(["Text token", "Base token", "Tree Tagger Tagged POS", "Our Tagged POS"])
        for line in tagged_output:
            non_empty_tks = list(filter(lambda x: len(x) > 0, line.split("\t")))
            if len(non_empty_tks) == 3:
                original_token, tagged_pos, base_token = non_empty_tks
                csvwriter.writerow([original_token, base_token, tagged_pos, ""])
            else:
                print(len(non_empty_tks))
