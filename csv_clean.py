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
def clean_helpful_rating(review):
    if review is None:
        return
    return re.sub(r'\(Helpful: \d+, Rating: \d\)', '', review).strip()

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

# ====================
# Main cleaning function for description / title
# ====================
def clean_text(text, selected_make):
    return clean_content_from_title(
        clean_title_from_content(
        clean_non_ascii(    
        clean_quotations(
        clean_words_pattern(
        clean_helpful_rating(
        clean_asterisks(
        clean_wrong_make(
        clean_truck(
        check_title_pattern(text)), selected_make))))))))

# Particular function for the description title
def clean_description(text, selected_make):
    return clean_title_from_content(clean_non_ascii(clean_text(text, selected_make)))
    

# Particular function for the title column
def clean_title(text, selected_make):
    return clean_content_from_title(clean_quotations(clean_text(text, selected_make)))


def clean_csv(input_file, output_file):
    with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            selected_make = row['make']
            cleaned_row = {
                'make': row['make'],
                'model':row['model'],
                'parent_generation': row['parent_generation'] ,
                'review_description': clean_description(row['review_description'], selected_make),	
                'rating_stars': row['rating_stars'],	
                'review_title': clean_title(row['review_title'], selected_make),	
                'review_author': row['review_author'], 
                'helpful': row['helpful'],
            }
            writer.writerow(cleaned_row)
    print(f"Finished cleaning {input_file} and outputted to {output_file}")


clean_csv('combined_20240219.csv', 'combined_cleaned_20240219_1605.csv')





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