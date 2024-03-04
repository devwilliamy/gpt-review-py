import random
import csv_helper
import re
import csv
import os

distinct_make_model_parent_file=os.environ.get("IN_DISTINCT_MAKE_MODEL_PARENT_GENERATION_CSV")
distinct_make_model_parent_type_file=os.environ.get("IN_DISTINCT_MAKE_MODEL_PARENT_GENERATION_TYPE_CSV")
if distinct_make_model_parent_file is None or distinct_make_model_parent_type_file is None:
    print("Error: IN_DISTINCT_MAKE_MODEL_PARENT_GENERATION_CSV or IN_DISTINCT_MAKE_MODEL_PARENT_GENERATION_TYPE_CSV environment variables are not set.")
    exit(1)

# This script is to take a CSV and clean it

# Read in the distinct make and model, store that data in an array
# distinct_make_model_parent_file='data/Distinct Make, Model, and Parent Generation.csv'
# unique_make_model = csv_helper.read_csv(distinct_make_model_parent_file)
distinct_make_model_parent_file='data/Remaining Distinct Make Model and Parent Generation and Type.csv'
unique_make_model = csv_helper.read_csv(distinct_make_model_parent_file)

unique_make = set()
for item in unique_make_model:
    unique_make.add(item['make'])

type_lookup = {}
def read_csv_2(file_name_path):
    data = []  # To store the data 
    with open(file_name_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        header_columns = next(reader)  # Read the header row
        for row in reader:
            # Create an object from the row
            car_object = {
                # 'make': row['\ufeff"make"'],
                'make': row['make'],
                'model': row['model'],
                'parent_generation': row['parent_generation'],
                # 'type' : row['type']
                'type' : row['\ufeff"type"']
            }
            # type_lookup[(row['\ufeff"make"'], row['model'])] = row['type']
            type_lookup[(row['make'], row['model'])] = row['\ufeff"type"']
            data.append(car_object)
    return data
unique_make_model_year_type = read_csv_2(distinct_make_model_parent_type_file)


# print(unique_make)

# Will detect if there's a make in the sentence and detect if it doesn't match the make we're in
def clean_wrong_make(review, selected_make):
    if review is None:
        return
    if selected_make.lower() in review.lower():
        return review
    for make in unique_make:
        if make.lower() != selected_make.lower() and make.lower() in review.lower():
            review = re.sub(r'\b' + re.escape(make) + r'\b', '', review, flags=re.IGNORECASE)
            return ""
    return review

# Sometimes (Helpful: ...) got left in. Remove it
# Examples:
# - Perfect Fit and Easy to Use (Helpful: 2, Rating: 5 --- this one should probably be nuked (the whole row) or make the title = the description cus description is missing the first letter 
# - Helpful: 2, Rating: 5
# - (Helpful: 2, Rating: 5 )
# - Helpful: 1, Rating: 2)
# - Note: Also need to have a cleaning for t: 
# - Note : Need a cleaning for ( ex: Pontiac	Trans AM	1969-1981

def clean_helpful_rating(review):
    if review is None:
        return
    return clean_parenthesis(re.sub(r'\(?Helpful: \d+, Rating: \d\)?', '', review).strip())

# ChatGPT returned stuff in bold. This really messed with the formatting so the data isn't good
def clean_asterisks(s):
    if s is None:
        return
    if '*' in s:
        return ''
    else:
        return s

# Sometimes quotes got into title
def clean_quotations(text):
    if text is None:
        return
    return re.sub(r'"', '', text).strip()

def clean_parenthesis(text):
    if text is None:
        return
    return re.sub(r'\)', '', text).strip()
    
# Get rid of weird emojis 
def clean_non_ascii(text):
    if text is None:
        return
    return re.sub(r'[^\x00-\x7F]+', '', text)

# Sometimes content leaked into title. But JK running on both anyway because it spread to both
def clean_content_from_title(text):
    if text is None:
        return
    return re.sub(r'Content:.*', '', text).strip()

# Sometimes title leaked into content. But JK running on both anyway because it spread to both
def clean_title_from_content(text):
    if text is None:
        return
    return re.sub(r'Title:.*', '', text).strip()

# Sometimes there's "(16 words)" in the string so get rid of that part
def clean_words_pattern(text):
    if text is None:
        return
    return re.sub(r'\(\d+ words\)', '', text).strip()

# If it has 1. Title: ... 2. Title: .... just get rid of the entire thing
def check_title_pattern(text):
    if re.search(r'^(\d+\.|\*\.)\s*Title:', text, flags=re.MULTILINE):
        return ''
    return text

# Some truck words got into some stuff so we clean dem
def clean_truck(text):
    if "truck" in text.lower():
        return ""
    return text

# Remove waterproof all weather
def clean_waterproof_all_weather(text):
    return text.replace("Waterproof All Weather", "").replace("  ", " ")

def clean_wrong_brand(text):
    return text.replace("CoverMaster", "Coverland")\
                .replace("CoverMasters", "Coverland")\
                .replace("CoverTech", "Coverland")\
                .replace("Covercraft", "Coverland")\
                .replace("EliteGuard", "Coverland")\
                .replace("LuxeShield", "Coverland")\
                .replace("ShieldPro", "Coverland")\
                .replace("ProShield", "Coverland")\
                .replace("CarGuard", "Coverland")\
                .replace("WeatherShield", "Coverland")\
                .replace("ClassicGuard", "Coverland")\
                .replace("WeatherGuard", "Coverland")\
                .replace("All-Weather", "Coverland")\
                .replace("CoverPlex", "Coverland")\
                .replace("CoverShield Deluxe", "Coverland")

def extract_just_say_phrase(input_string):
    phrase = "just say"
    if phrase in input_string.lower():
        start_index = input_string.lower().find(phrase)
        end_index = input_string.find('.', start_index)
        if end_index == -1:
            end_index = len(input_string)

        before_phrase = input_string[:start_index].strip()
        after_phrase = input_string[start_index + len(phrase):end_index].strip()

        return before_phrase + after_phrase + '.'
    else:
        return input_string
    
def clean_wrong_product_type_in_description(text, product_type):
    if product_type == "SUV Covers":
        replacement = "SUV"
        return re.sub(r'\bcar\b', replacement, text, flags=re.IGNORECASE)
    elif product_type == "Truck Covers":
       replacement = "truck"
       return re.sub(r'\bcar\b', replacement, text, flags=re.IGNORECASE)
    else: 
        return text


def randomly_delete(text, rating, base_probability=0.1, trigger_word="color", increased_probability=0.3):
    
    if int(rating) <= 2:
        if trigger_word in text.lower():
            # print("Color found")
            probability = increased_probability
        else:
            probability = base_probability
        
        if random.random() < probability:
            # print(f"Should have deleted: {text}")
            text = ""
    return text

def randomly_set_helpful(helpful, description, title):
    helpful = int(helpful)
    if description == '' and title =='':
        return 0
    if helpful == 1:
        return random.randint(5, 7)
    elif helpful == 2: 
        return random.randint(7, 10)
    elif helpful == 5:
        return random.randint(10, 15)
    elif helpful == 10:
        return random.randint(15, 20)
    elif helpful == 15:
        return random.randint(20, 25)
    elif helpful == 20:
        return random.randint(25,35)
    else:
        return 1
# ====================
# Main cleaning function for description / title
# ====================
def clean_text(text, selected_make, selected_type, rating):
    return clean_wrong_product_type_in_description(
        extract_just_say_phrase(
        clean_wrong_brand(
        clean_waterproof_all_weather(
        clean_content_from_title(
        clean_title_from_content(
        clean_non_ascii(    
        clean_quotations(
        clean_words_pattern(
        clean_helpful_rating(
        clean_asterisks(
        # clean_wrong_make(
        clean_truck(
        check_title_pattern(text)), #selected_make
        )))))))))), selected_type)

# # Particular function for the description title
# def clean_text(text, selected_make):
#     return clean_title_from_content(clean_non_ascii(clean_text(text, selected_make)))
    

# # Particular function for the title column
# def clean_title(text, selected_make):
#     return clean_content_from_title(clean_quotations(clean_text(text, selected_make)))

def clean_csv(input_file, output_file):
    with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ["type"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            selected_make = row['make']
            selected_type = type_lookup.get((row['make'], row['model']))
            selected_rating = row['rating_stars']
            cleaned_row = {
                'make': row['make'],
                'model':row['model'],
                'parent_generation': row['parent_generation'] ,
                'review_description': clean_text(row['review_description'], selected_make, selected_type, selected_rating),	
                'rating_stars': row['rating_stars'],	
                'review_title': clean_text(row['review_title'], selected_make, selected_type, selected_rating),	
                'review_author': row['review_author'], 
                'helpful': randomly_set_helpful(row['helpful'], row['review_description'], row['review_title']),
                'type': selected_type
            }
            writer.writerow(cleaned_row)
    print(f"Finished cleaning {input_file} and outputted to {output_file}")

# =============================
# Change the file names down here
# =============================

input_to_clean_csv=os.environ.get("IN_TO_CLEAN_CSV")
output_cleaned_csv=os.environ.get("OUT_CLEANED_CSV")
if distinct_make_model_parent_file is None or distinct_make_model_parent_type_file is None:
    print("Error: IN_TO_CLEAN_CSV or OUT_CLEANED_CSV environment variables are not set.")
    exit(1)

clean_csv(input_to_clean_csv, output_cleaned_csv)

