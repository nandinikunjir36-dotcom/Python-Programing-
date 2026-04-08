import json
import csv

try:
    with open('/Users/pawar/OneDrive/Documents/data_new.json', 'r')as json_file:
     data=json.load(json_file)

    with open('output.csv','w', newline='')as csv_file:
        headers=data[0].keys()
        writer=csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

        print("conversion successful!")
    
except FileNotFoundError:
    print("Json File Not Found.")