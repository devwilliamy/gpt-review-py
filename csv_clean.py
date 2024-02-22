import random
import csv_helper
import re
import csv
# This script is to take a CSV and clean it

# Read in the distinct make and model, store that data in an array
file_name='data/Distinct Make, Model, and Parent Generation.csv'
unique_make_model = csv_helper.read_csv(file_name)

unique_make = set()
for item in unique_make_model:
    unique_make.add(item['make'])

file_name_2 = 'data/Distinct Make Model Parent Generation and Type.csv'
type_lookup = {}
def read_csv_2(file_name_path):
    data = []  # To store the data 
    with open(file_name_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        header_columns = next(reader)  # Read the header row
        for row in reader:
            # Create an object from the row
            car_object = {
                'make': row['\ufeff"make"'],
                'model': row['model'],
                'parent_generation': row['parent_generation'],
                'type' : row['type']
            }
            type_lookup[(row['\ufeff"make"'], row['model'])] = row['type']
            data.append(car_object)
    return data
unique_make_model_year_type = read_csv_2(file_name_2)


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
                .replace("CoverShield Deluxe", "Coverland")\

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
    return randomly_delete(clean_wrong_product_type_in_description(
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
        ))))))))), selected_type), rating)

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
    
clean_csv('combined_csv_02212024_1408/combined_02212024_1408.csv', 'combined_csv_02212024_1408/combined__cleaned_02212024_1408.csv')

#=================
# Testing the clean functions
#=================
review = "I love my Jeep Grand Cherokee, and this cover protects it perfectly! Easy to install and holds up in intense winds. Highly recommend it. (Helpful: 20, Rating: 5)"
review_2 = "Ideal fit for Alfa Romeo Spider. Keeps my car safe and dry. Excellent quality. Highly recommend."
selected_make = "Alfa Romeo"
# print(clean_wrong_make(review_2, selected_make))
review_3 = "**Title:** Pleasantly Surprised Skeptic\n**Content:** I doubted its quality, but the cover proved to be outstanding. Water-repellent and durable, it's now an essential part of protecting my car."
review_4 = "Easy to put on, lightweight, yet durable. Perfect for my needs. Highly recommend this cover. (Helpful: 2, Rating: 5)"
review_5 = """
"lpful: 20, Rating: 5)**  
   **Reluctant at First, but Now I Swear by It**  
   *Initially skeptical, this cover for my Alfa Romeo 2000 1958-1962 won me over. Durable, easy to install, great protection ��� a wise investment.*"

   """
# print(clean_non_ascii(review_5))

review_6="""
"Fits my AMC Rambler Cross Country perfectly 
Content: I looked at several car covers for my AMC Rambler Cross Country and this one looked like the best. It fits perfectly, just make sure you use the sizing chart when ordering. However, I learned that it's not completely waterproof in heavy rain. Shortly after putting it on my car, we had a severe thunderstorm and some water did get through, probably through the seam. But I've found that no car covers are completely waterproof, so I guess it should be expected. This particular cover has adjustable retaining straps in the front and back and comes with an extra strap for the midbody to secure the cover under the vehicle. It also has grommets for an anti-theft cable or bungee cord to keep the cover firmly in place. It also comes with an antenna grommet, and you can add a large nylon drawstring storage bag. One word of caution, I followed the instructions for installing the cover which state that it's not necessary to use the antenna grommet if you have a flexible antenna. Well, that didn't work out well because when I removed the cover, which was heavy, my rubber flex antenna was bent and cracked in several places. In retrospect, my car's six years old and the rubber was weathered and hardened. But be aware that you might want to remove any detachable antennas before using this cover, as a replacement antenna cost me [Amazon]. Other than that, I'm happy with this cover, it's well made, easy to install, and stayed on my car during 70 MPH winds and heavy rain."

"""
# print(clean_content_from_title(review_6))

review_7="""
I was skeptical about buying this car cover, but it turned out to be a perfect fit for my Acura NSX. The high-quality material and tailored fit provide excellent protection against weather and temperature changes. It's easy to put on and secure with the adjustable straps. Definitely worth the investment!
"""
# print(clean_wrong_make(review_7, 'Acura'))

review_8="""
I bought the Coverland Premium Car Cover Waterproof All Weather for my Shelby Cobra, but I wasn't impressed. After a heavy rain, water leaked through the seams. I almost returned it, but my husband likes the other features, so he's going to try a waterproof spray on the seams to prevent leakage. Can't comment on durability after only one month.
"""
# print(clean_waterproof_all_weather(review_8))


# Examples
# reviews = [
#     "Perfect Fit and Quality Cover (Helpful: 2, Rating: 5",
#     "Great product Helpful: 2, Rating: 5",
#     "Excellent (Helpful: 2, Rating: 5 )",
#     "Good value Helpful: 1, Rating: 2)"
# ]

# cleaned_reviews = [clean_helpful_rating(review) for review in reviews]
# for cleaned_review in cleaned_reviews:
#     print(cleaned_review)

review_9 = """
The Covercraft Car Cover for my Chevrolet Silverado 1500HD is top-notch. The material is durable, the fit is perfect, and it withstands heavy rain and wind admirably. I highly recommend it.
"""
# print(clean_wrong_product_type_in_description(review_9, "Truck Cover"))

review_10 = """
So, I got this car cover, right? Looks good and all, but when I tried to put it on, man, it was a headache. The installation instructions were kinda vague, and I had to figure things out on my own. Definitely not user-friendly for newbies like me. So, if you're a first-timer, be prepared to do some trial and error.
"""
# print(clean_text(review_10, "AMC", "Car Covers", 0))