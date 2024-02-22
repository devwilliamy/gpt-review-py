import csv
import csv_helper
import random
# Going to fix images 
# Going to fix helpful range


file_name='data/ID Type Helpful For Image Fix.csv'
# csv_data = csv_helper.read_csv(file_name)

file_name2='data/Type Helpful Count Distinct.csv'
# csv_data2= csv_helper.read_csv(file_name2)

def determine_helpful(helpful, count):
   if int(helpful) > 30 and int(count) > 100 and random.random() < 0.5:
        helpful = random.randint(2, 20)
        return helpful
   else:
       return helpful

def fix_helpful():
    type_lookup = {}
    with open(file_name2, 'r', newline='') as file:
        reader = csv.DictReader(file)
        # header_columns = next(reader)
        for row in reader:
            type_lookup[(row['\ufeff"type"'], row['helpful'])] = row['count']
    data = []
    with open(file_name, 'r', newline='') as file:
        reader = csv.DictReader(file)
        header_columns = next(reader)
       
        for row in reader: 
            type = row['type']
            helpful = row['helpful']
            count = type_lookup[(type, helpful)]
            new_data = {
                'id': row['\ufeff"id"'],
                'type': row['type'],
                'helpful': determine_helpful(helpful, count)
            }
            data.append(new_data)
    return data
        


fieldnames=["id","type","helpful"]
new_data = fix_helpful()
with open('fix_helpful_count/new_id_helpful_count.csv', mode='w', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in new_data:
        writer.writerow(row)
print('finished fixing helpful count')