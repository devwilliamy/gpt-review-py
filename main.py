import csv_helper
import review_generation
import review_parser
# Read in the distinct make and model, store that data in an array
file_name='csv/Distinct Make, Model, and Parent Generation.csv'
csv_data = csv_helper.read_csv(file_name)
# print(csv_data[:3])

ready_review_data_list = []
# =======================
# CHANGE THESE 
# =======================
to_count=11
# Remember this is NOT INCLUSIVE, so it'll be to this number - 1.
# For example, if you do 0, 3, you'll only get 3 back [0,1,2]
from_count=21 


for i in range(to_count, from_count):
# for i in range(0, 1):
    make = csv_data[i]["make"]
    model = csv_data[i]["model"]
    year = csv_data[i]["parent_generation"]
    generated_reviews = review_generation.generate_review(make, model, year)
    parsed_reviews = review_parser.parse_reviews(generated_reviews, make, model, year)
    ready_review_data_list.extend(parsed_reviews)
    





field_names = ['make', 'model', 'parent_generation', 'review_description', 'rating_stars', 'review_title', 'review_author', 'helpful']

csv_helper.write_csv(f'csv/reviews_{to_count}_{from_count}.csv', field_names, ready_review_data_list)