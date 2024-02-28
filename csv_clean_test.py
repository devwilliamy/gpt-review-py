from csv_clean import *
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