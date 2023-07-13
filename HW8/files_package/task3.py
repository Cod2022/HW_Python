"""
Запись из json в csv
"""
import json
import csv

def json_csv_write(file_json):
    with (open
        (file_json, 'r', encoding='utf-8') as f_json,
        open('nums_names.csv', 'w', encoding='utf-8', newline='') as f_csv
        ):
        json_dict = json.load(f_json)
        print(json_dict)
        rows = []
        for level, in_dict in json_dict.items():
            for id, name in in_dict.items():
                rows.append({'id': id, 'level': int(level), 'name': name})
        print(rows)

        csv_write = csv.DictWriter(f_csv, fieldnames=['id', 'level', 'name'])
        csv_write.writeheader()
        csv_write.writerows(rows)

if __name__ =='__main__':
    json_csv_write('nums_names.json')


