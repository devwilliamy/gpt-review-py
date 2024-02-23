import csv
import csv_helper
import random
# Going to fix images 
# Going to fix helpful range

car_cover_photos = [
'https://coverland.com/review/coupe_review_002_01.webp,https://coverland.com/review/coupe_review_002_02.webp,https://coverland.com/review/coupe_review_002_04.webp',
'https://coverland.com/review/coupe_review_001_04.webp,https://coverland.com/review/coupe_review_001_05.webp',
'https://coverland.com/review/sedan_review_002_01.webp',
'https://coverland.com/review/coupe_review_003_03.webp',
'https://coverland.com/review/sedan_review_001_01.webp,https://coverland.com/review/sedan_review_001_03.webp',
'https://coverland.com/review/sedan_review_001_01.webp,https://coverland.com/review/sedan_review_001_03.webp',
'https://coverland.com/review/sedan_review_001_02.webp',
'https://coverland.com/review/coupe_review_001_01.webp',
'https://coverland.com/review/sports_review_001_02.webp',
]

suv_cover_photos = [
'http://coverland.com/review/suv_review_008_01.webp,http://coverland.com/review/suv_review_008_02.webp',
'http://coverland.com/review/suv_review_006_01.webp,http://coverland.com/review/suv_review_006_02.webp,http://coverland.com/review/suv_review_006_03.webp,http://coverland.com/review/suv_review_006_04.webp',
'http://coverland.com/review/suv_review_009_01.webp,http://coverland.com/review/suv_review_009_02.webp,http://coverland.com/review/suv_review_009_03.webp',
'http://coverland.com/review/suv_review_007_01.webp,http://coverland.com/review/suv_review_007_02.webp',
'http://coverland.com/review/suv_review_012_01.webp,http://coverland.com/review/suv_review_012_02.webp,http://coverland.com/review/suv_review_012_03.webp,http://coverland.com/review/suv_review_012_04.webp',
'http://coverland.com/review/suv_review_011_01.webp',
'http://coverland.com/review/suv_review_005_01.webp,http://coverland.com/review/suv_review_005_02.webp',
'http://coverland.com/review/suv_review_010_01.webp,http://coverland.com/review/suv_review_010_02.webp,http://coverland.com/review/suv_review_010_03.webp',
'http://coverland.com/review/suv_review_004_01.webp,http://coverland.com/review/suv_review_004_02.webp,http://coverland.com/review/suv_review_004_03.webp',
'http://coverland.com/review/suv_review_002_01.webp,http://coverland.com/review/suv_review_002_02.webp,http://coverland.com/review/suv_review_002_03.webp',
]

truck_cover_photos = [
'http://coverland.com/review/truck_review_004_01.webp,http://coverland.com/review/truck_review_004_02.webp,http://coverland.com/review/truck_review_004_03.webp,http://coverland.com/review/',
'http://coverland.com/review/truck_review_017_01.webp,http://coverland.com/review/truck_review_017_02.webp,http://coverland.com/review/truck_review_017_03.webp',
'http://coverland.com/review/truck_review_008_01.webp,http://coverland.com/review/truck_review_008_02.webp,http://coverland.com/review/truck_review_008_03.webp',
'http://coverland.com/review/truck_review_007_01.webp,http://coverland.com/review/truck_review_007_02.webp,http://coverland.com/review/truck_review_007_03.webp',
'http://coverland.com/review/truck_review_013_01.webp,http://coverland.com/review/truck_review_013_02.webp,http://coverland.com/review/truck_review_013_03.webp,http://coverland.com/review/',
'http://coverland.com/review/truck_review_006_01.webp,http://coverland.com/review/truck_review_006_02.webp',
'http://coverland.com/review/truck_review_010_01.webp',
'http://coverland.com/review/truck_review_015_01.webp,http://coverland.com/review/truck_review_015_02.webp,http://coverland.com/review/truck_review_015_03.webp',
'http://coverland.com/review/truck_review_011_01.webp,http://coverland.com/review/truck_review_011_02.webp',
'http://coverland.com/review/truck_review_009_01.webp,http://coverland.com/review/truck_review_009_02.webp,http://coverland.com/review/truck_review_009_03.webp',
'http://coverland.com/review/truck_review_002_01.webp,http://coverland.com/review/truck_review_002_02.webp',
'http://coverland.com/review/truck_review_016_01.webp,http://coverland.com/review/truck_review_016_02.webp',
'http://coverland.com/review/truck_review_018_01.webp,http://coverland.com/review/truck_review_018_02.webp',
'http://coverland.com/review/truck_review_001_01.webp,http://coverland.com/review/truck_review_001_02.webp,http://coverland.com/review/truck_review_001_03.webp,http://coverland.com/review/http://coverland.com/review/truck_review_001_01.webp,http://coverland.com/review/truck_review_001_02.webp,http://coverland.com/review/truck_review_001_03.webp,http://coverland.com/review/truck_review_001_04.;webp',
'http://coverland.com/review/truck_review_003_01.webp,http://coverland.com/review/truck_review_003_02.webp',
'http://coverland.com/review/truck_review_014_01.webp',
'http://coverland.com/review/truck_review_012_01.webp,http://coverland.com/review/truck_review_012_02.webp,http://coverland.com/review/truck_review_012_03.webp,http://coverland.com/review/',
'http://coverland.com/review/truck_review_005_01.webp,http://coverland.com/review/truck_review_005_02.webp,http://coverland.com/review/truck_review_005_03.webp,http://coverland.com/review/',
]
file_name='data/new_id_helpful_count_20240221.csv'
# csv_data = csv_helper.read_csv(file_name)

file_name2='data/Type Helpful Count Distinct 20240222_1305.csv'
# csv_data2= csv_helper.read_csv(file_name2)
assigned_car_photo_index = 0
assigned_suv_photo_index = 0
assigned_truck_photo_index = 0
def randomly_assign_photo(helpful, type):
    global assigned_car_photo_index
    global assigned_suv_photo_index
    global assigned_truck_photo_index
    car_photo_length = len(car_cover_photos)
    suv_photo_length = len(suv_cover_photos)
    truck_photo_length = len(truck_cover_photos)
    if int(helpful) >= 5:
        if type == 'Car Covers':
            photo_to_assign = car_cover_photos[assigned_car_photo_index]
            assigned_car_photo_index+=1
            if assigned_car_photo_index >= car_photo_length:
                assigned_car_photo_index = 0
            return photo_to_assign
        elif type == 'SUV Covers':
            photo_to_assign = suv_cover_photos[assigned_suv_photo_index]
            assigned_suv_photo_index+=1
            if assigned_suv_photo_index >= suv_photo_length:
                assigned_suv_photo_index = 0
            return photo_to_assign
        elif type == 'Truck Covers':
            photo_to_assign = truck_cover_photos[assigned_truck_photo_index]
            assigned_truck_photo_index+=1
            if assigned_truck_photo_index >= truck_photo_length:
                assigned_truck_photo_index = 0
            return photo_to_assign
    return ""

def determine_helpful(helpful, count):
   if int(helpful) > 30 and int(count) > 50 and random.random() < 0.6:
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
                'id': row['id'],
                'type': row['type'],
                'helpful': determine_helpful(helpful, count),
                'review_image': randomly_assign_photo(helpful, type)
            }
            data.append(new_data)
    return data
        


fieldnames=["id","type","helpful", "review_image"]
new_data = fix_helpful()
with open('fix_helpful_count/new_id_helpful_count_20240222_1307.csv', mode='w', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in new_data:
        writer.writerow(row)
print('finished fixing helpful count')