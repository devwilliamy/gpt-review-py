import random 
import csv_helper
import review_generation
import review_parser
import os
from dotenv import load_dotenv

# Read in the distinct make and model, store that data in an array
file_name='data/Distinct Make, Model, and Parent Generation.csv'
csv_data = csv_helper.read_csv(file_name)
# print(csv_data[:3])
load_dotenv()

ready_review_data_list = []
# =======================
# CHANGE THESE 
# =======================
# to_count=300
to_count=os.environ.get("TO_COUNT")
# Remember this is NOT INCLUSIVE, so it'll be to this number - 1.
# For example, if you do 0, 3, you'll only get 3 back [0,1,2]
# So if you're doing 10-20, 21-30, you'd do (10,21) and then (21,31)
# Or I guess you can do (10,20) and then (20,30)
# from_count=400
from_count=os.environ.get("FROM_COUNT")
if to_count is None or from_count is None:
    print("Error: TO_COUNT or FROM_COUNT environment variables are not set.")
    exit(1)

to_count = int(to_count)
from_count = int(from_count)
print(f"TO_COUNT: {to_count}, FROM_COUNT: {from_count}")
skipped_times = 0
for i in range(to_count, from_count):
# for i in range(0, 1):
    # try: 
    
    if random.random() <= 0.75:
        skipped_times += 1
        # print(f"Skip Count: {skipped_times}")
        continue
    make = csv_data[i]["make"]
    model = csv_data[i]["model"]
    year = csv_data[i]["parent_generation"]
    generated_reviews = review_generation.generate_review(make, model, year)
    parsed_reviews = review_parser.parse_reviews(generated_reviews, make, model, year)
    ready_review_data_list.extend(parsed_reviews)
    # except:
    #     print(f"Error at index: {i}")
    
print(f"Skip Count: {skipped_times}")





directory = f'csv_02212024_1408'

# Create the directory if it doesn't exist
os.makedirs(directory, exist_ok=True)

# Specify the file path
file_path = os.path.join(directory, f'{make}_{model}_{year}_reviews.txt')

field_names = ['make', 'model', 'parent_generation', 'review_description', 'rating_stars', 'review_title', 'review_author', 'helpful']

csv_helper.write_csv(f'{directory}/reviews_{to_count}_{from_count}.csv', field_names, ready_review_data_list)