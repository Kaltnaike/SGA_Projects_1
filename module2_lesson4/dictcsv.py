big_list = [
    {'Name':'Awonaike Tawakalitu', 'userid':150, 'is_admin':False},
    {'Name':'Balogun Wahab', 'userid':230, 'is_admin':False},
    {'Name':'Asade Darasimi', 'userid':100, 'is_admin':False},
    {'Name':'Asade Olanrewaju', 'userid':300, 'is_admin':True},
    ]
import csv

with open('output.csv','w') as output_csv:
    fields = ['Name','userid', 'is_admin']
    output_writer = csv.DictWriter(output_csv, fieldnames=fields)
    output_writer.writeheader()

    for item in big_list:
        output_writer.writerow(item)