import csv
import json
import os
# data = [
#     {'make': 'Toyota', 'model': 'Camry', 'parent_generation': '1991-2008', 'review_description': 'Great car', 'rating_stars': 5, 'review_title': 'Excellent', 'review_author': 'John Doe', 'helpful': True},
#     {'make': 'Honda', 'model': 'Accord', 'parent_generation': '2008-2012', 'review_description': 'Reliable', 'rating_stars': 4, 'review_title': 'Good car', 'review_author': 'Jane Smith', 'helpful': False}
# ]

# Specify the CSV file path
file_name_path = 'csv/reviews_test.csv'

# Define the field names (column names)
field_names = ['make', 'model', 'parent_generation', 'review_description', 'rating_stars', 'review_title', 'review_author', 'helpful']

# Test Data
# data = [{'make': 'bmw', 'model': '3-series', 'parent_generation': '1997-2008', 'review_description': "I purchased the Coverland Premium Car Cover Waterproof All Weather for my AC 3000ME and was disappointed with its performance. It claimed to be waterproof, but water leaked through the seams. I almost returned it, but my husband liked the other features, so he decided to try a waterproof spray on the seams to prevent leakage. I can't comment on its durability yet as it has only been a month.", 'rating_stars': 2, 'review_title': 'Dissatisfied with the Product', 'review_author': 'Caroline Desotel', 'helpful': 1}, {'make': 'bmw', 'model': '3-series', 'parent_generation': '1997-2008', 'review_description': "I have bought many covers for my AC 3000ME over the years, but the Coverland Premium Car Cover stands out as the best. It fits perfectly and has proven to be waterproof during heavy rain. The zipper entry on the driver's door is a great feature. When I contacted the company about the cover's durability, they provided outstanding customer service and sent me a new cover under warranty. Highly recommended!", 'rating_stars': 5, 'review_title': 'Excellent Protection and Customer Service', 'review_author': 'Nannette Winters', 'helpful': 20}, {'make': 'bmw', 'model': '3-series', 'parent_generation': '1997-2008', 'review_description': 'I was skeptical about the Coverland Premium Car Cover at first, but it surpassed my expectations. It fits great and really covers the entire car. It is truly waterproof and seems to be holding up well against the elements. I believe this cover will last longer than others I have purchased in the past. Great fit and durability combined with excellent customer service make this a top-notch product.', 'rating_stars': 5, 'review_title': 'Pleasantly Surprised', 'review_author': 'Genevieve Tointon', 'helpful': 15}]
def write_csv(file_name_path, field_names, data):
    try:
        with open(file_name_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            
            # Write the header (column names) to the CSV file
            writer.writeheader()
            
            # Write the data to the CSV file
            for row in data:
                writer.writerow(row)
        print(f"Data has been written to '{file_name_path}'")
    except IOError:
        # Append '_2' to the file name if the file cannot be written to
        file_name, file_extension = os.path.splitext(file_name_path)
        new_file_name = f"{file_name}_2{file_extension}"
        print(f"Could not write to '{file_name_path}'. Writing to '{new_file_name}' instead.")
        write_csv(new_file_name, field_names, data)

# Test write_csv
# write_csv(file_name_path, field_names, data)
        

def read_csv(file_name_path):
    data = []  # To store the data 
    with open(file_name_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        header_columns = next(reader)  # Read the header row
        for row in reader:
            # Create an object from the row
            car_object = {
                'make': row['\ufeff"make"'],
                'model': row['model'],
                'parent_generation': row['parent_generation']
            }
            data.append(car_object)
    return data

# Test read_csv
# read_csv()
