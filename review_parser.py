import generate_names
review="Title: Perfect Fit for My SUV\nContent: I was skeptical about finding the right car cover for my Hyundai SUV, but this one fit perfectly. It comes with adjustable straps, grommets for the anti-theft cable, and even an antenna grommet. Just be careful with detachable antennas!\n\nTitle: Keeps My Honda Hatchback Dry\nContent: The EzyShade Layer Car Cover is truly waterproof. Even during heavy rain and snow, my car stayed completely dry. I'm so satisfied with this purchase and highly recommend it to others.\n\nTitle: The Best Investment for Protection\nContent: I've bought many car covers in the past, but this EzyShade Layer Car Cover is the real deal. It truly provides excellent water protection and holds up well even in strong winds. Definitely worth the investment!\n\nTitle: Great car Cover\nContent: This car cover is not only waterproof, but it's also easy to dry off after rain. It's the best and least expensive car cover I've ever purchased. Couldn't be happier with it.\n\nTitle: Almost as Good as a Garage\nContent: I'm very pleased with this car cover. It's fully waterproof and relatively easy to remove and replace. It adapts to the shape of my vehicle over time, making it even easier to use. Wish I had bought it sooner!\n\nTitle: Great Fit and Durability\nContent: This cover fits my car great and provides excellent water protection. It seems very durable and I believe it will last longer than other covers I've purchased. Highly recommended!\n\nTitle: Best Cover with Outstanding Customer Service\nContent: This cover is the best one I've bought for my Jeep. It fits well, is waterproof, and easy to secure. When I had an issue, the customer service was outstanding. They sent me a new cover right away. Impressed!\n\nTitle: Great Fit, Seems Durable\nContent: This cover fits great and really covers my car. It's waterproof and seems to be holding up well. The customer service is also excellent. Overall, a great value for the price.\n\nTitle: Thin, but Does the Job\nContent: This cover may be thin, but it's waterproof and a good value for the price. It fits my car well and the buckle straps keep it in place. Recommended for light use.\n\nTitle: Perfect Fit for Buick Roadmaster\nContent: I love how well this cover fits my Buick Roadmaster, especially with the zipper to easily access the car. The reflectors and windproofing straps are handy features. Just be mindful of potential leaks through the seams. Overall, a great buy!"

review_2="1. Title: Perfect Fit for My SUV\n   Content: This car cover fits my SUV perfectly. It's made with high-quality materials and has adjustable straps for a secure fit. It kept my car dry during heavy rain and I love that it has grommets for an anti-theft cable. Highly recommended!\n\n2. Title: Excellent Quality and Fit\n   Content: I purchased this car cover for my Honda hatchback and it exceeded my expectations. It's waterproof and stayed securely in place even during strong winds. I'm very satisfied with this purchase.\n\n3. Title: Great Investment of Protection\n   Content: Compared to other car covers I've tried, the Coverland Premium Car Cover is truly waterproof and offers excellent protection. It withstood strong winds without any issues. I'm impressed and happy with my purchase.\n\n4. Title: Waterproof and Easy to Dry\n   Content: This car cover is waterproof and dries off easily after rain. It's the best car cover I've ever bought, and the price is unbeatable. Highly recommended.\n\n5. Title: Almost as Good as a Garage\n   Content: I'm highly pleased with this car cover. It's fully waterproof and relatively easy to install and remove. It adapts to the shape of my vehicle over time and gets easier to use. Wish I had bought it sooner!\n\n6. Title: Great Fit and Durability\n   Content: I've purchased expensive custom covers before, but this one is the best. It fits great, proved to be fully waterproof, and the zipper entry for the driver's door is a great feature.\n\n7. Title: Great Fit and Durable\n   Content: This car cover fits perfectly and provides great coverage. It's waterproof and seems to be holding up well. I believe it will last longer than other covers I've bought. Highly recommended.\n\n8. Title: Best Cover with Outstanding Customer Service\n   Content: I've bought many covers for my Jeep, but this one has been the best. It fits well, is waterproof, and easy to put on and secure. The customer service was exceptional, and they even sent me a replacement when mine wore out. A great company to do business with.\n\n9. Title: Thin but Waterproof\n   Content: This car cover seems thin, but surprisingly, it is waterproof and offers good value for the price. It fits my car well and the buckle straps keep it in place. Recommended.\n\n10. Title: Perfect Fit for Buick Roadmaster\n    Content: I love this car cover for my Buick Roadmaster. It fits very well, including the mirrors. The zipper entry is a handy feature. It's waterproof and the reflective straps are great for windproofing. Only issue is some leakage through the seams, but waterproof spray should help. Overall, a great purchase."

review_string = """
Title: Dissatisfied with the Product (Helpful: 1, Rating: 2)
Content: I purchased the Coverland Premium Car Cover Waterproof All Weather for my AC 3000ME and was disappointed with its performance. It claimed to be waterproof, but water leaked through the seams. I almost returned it, but my husband liked the other features, so he decided to try a waterproof spray on the seams to prevent leakage. I can't comment on its durability yet as it has only been a month.

Title: Excellent Protection and Customer Service (Helpful: 20, Rating: 5)
Content: I have bought many covers for my AC 3000ME over the years, but the Coverland Premium Car Cover stands out as the best. It fits perfectly and has proven to be waterproof during heavy rain. The zipper entry on the driver's door is a great feature. When I contacted the company about the cover's durability, they provided outstanding customer service and sent me a new cover under warranty. Highly recommended!

Title: Pleasantly Surprised (Helpful: 15, Rating: 5)
Content: I was skeptical about the Coverland Premium Car Cover at first, but it surpassed my expectations. It fits great and really covers the entire car. It is truly waterproof and seems to be holding up well against the elements. I believe this cover will last longer than others I have purchased in the past. Great fit and durability combined with excellent customer service make this a top-notch product.

Title: Perfect Gift (Helpful: 10, Rating: 5)
Content: I bought the Coverland Premium Car Cover Waterproof All Weather for my friend's AC 3000ME as a gift, and they loved it. The cover fits perfectly, provides excellent protection against rain and sun, and is easy to put on and secure. My friend couldn't be happier with this car cover. Definitely a great purchase for anyone looking to protect their AC 3000ME.

Title: Ideal for Southern States (Helpful: 5, Rating: 5)
Content: Living in Louisiana, I needed a car cover that could withstand the hot and humid weather. The Coverland Premium Car Cover has been perfect for my AC 3000ME. It is waterproof, keeps the car dry even during heavy rainstorms, and provides protection against the intense sun. I highly recommend this car cover to fellow residents of Florida, Louisiana, Texas, North Carolina, South Carolina, Alabama, and Mississippi.

Title: Perfect Fit (Helpful: 2, Rating: 5)
Content: The Coverland Premium Car Cover fits my AC 3000ME perfectly and stays in place. It is waterproof and easy to dry off after rain. Best car cover I've ever bought for my AC 3000ME.

Title: Good Quality (Helpful: 1, Rating: 5)
Content: The Coverland Premium Car Cover is of good quality and fits my AC 3000ME well. It provides excellent waterproof protection, and I am satisfied with this purchase.
"""

problem_string="""
"Review 1:\nTitle: Fits my AC Greyhound 1959-1963 perfectly (Helpful: 1, Rating: 2)\nContent: I bought this car cover for my AC Greyhound and was disappointed with the fit. It was too tight and didn't cover the entire car properly. The material also felt cheap and flimsy. I wouldn't recommend this cover for vintage cars like mine.\n\nReview 2:\nTitle: Excellent car cover for my AC Greyhound 1959-1963 (Helpful: 20, Rating: 5)\nContent: I am extremely pleased with this car cover for my AC Greyhound. It fits perfectly and provides excellent protection against the elements. The high-quality material feels durable and waterproof. The cover also has convenient features like zipper entry and reflective straps for added security. I highly recommend this cover for vintage car owners.\n\nReview 3:\nTitle: Pleasantly surprised by the quality (Helpful: 20, Rating: 5)\nContent: I was initially skeptical about buying this car cover, but it exceeded my expectations. The fit is snug and tailored, offering great protection against weather and temperature changes. The high-end polyester fabric feels sturdy and durable, while the soft fleece fabric inside protects my AC Greyhound's paint from scratches. This cover has proven to be a worthwhile investment.\n\nReview 4:\nTitle: Bought it for my dad's AC Greyhound and he loves it (Helpful: 10, Rating: 5)\nContent: I purchased this car cover as a gift for my dad's AC Greyhound, and he couldn't be happier. It fits perfectly and provides excellent protection against all types of weather. The high-quality material ensures durability, and the tailored fit adds a touch of elegance. My dad is thrilled with this gift and highly recommends it to other vintage car owners.\n\nReview 5:\nTitle: Perfect for the hot and humid climate in Florida (Helpful: 5, Rating: 5)\nContent: Living in Florida, I needed a car cover that could withstand the intense heat and humidity. This cover has been a lifesaver. It effectively keeps my AC Greyhound protected from the scorching sun and occasional rain showers. The waterproofing and UV protection features are a bonus. I am extremely satisfied with this purchase.\n\nReview 6:\nTitle: Great fit, excellent protection (Helpful: 15, Rating: 5)\nContent: I was initially skeptical about the claims of this car cover, but it has proven to be worth every penny. The snug fit ensures that my AC Greyhound is fully covered and protected from the elements. Despite my initial reservations, the cover is indeed waterproof and offers excellent durability. I highly recommend this car cover to anyone in need of reliable protection.\n\nReview 7:\nTitle: Best car cover I've ever owned (Helpful: 15, Rating: 5)\nContent: I've gone through several car covers before, but this one takes the cake. The tailored fit and high-quality material make a significant difference in terms of protection and durability. It keeps my AC Greyhound dry even in heavy rain and provides ample protection against the sun's harmful UV rays. Trust me, you won't be disappointed with this car cover.\n\nReview 8:\nTitle: Great for my AC Greyhound in Texas (Helpful: 5, Rating: 5)\nContent: As a proud owner of an AC Greyhound in Texas, I needed a car cover that could withstand the hot and dry climate. This cover does the job perfectly. It keeps my car protected from the intense sun and dust storms. The water-resistant feature also ensures that my car stays dry during occasional rain showers. Highly recommended for Texas residents!\n\nReview 9:\nTitle: Perfect fit and excellent quality (Helpful: 2, Rating: 5)\nContent: This car cover is everything I was looking for. It fits my AC Greyhound perfectly, and the high-quality material provides excellent protection against the elements. I've been using it for a while now, and it still looks brand new. I highly recommend this cover to anyone in need of a reliable and durable car cover.\n\nReview 10:\nTitle: Good car cover for my AC Greyhound (Helpful: 1, Rating: 5)\nContent: This car cover fits my AC Greyhound well and offers decent protection against rain and dust. The material feels durable, and the adjustable straps help keep it in place. It's a good value for the price. I'm satisfied with my purchase."
"""

def parse_reviews(review_string, make, model, year):
    reviews = []
    review_list = review_string.split('\n\n')
    for review_block in review_list:
        try:
            title_start = review_block.find('Title: ') + len('Title: ')
            helpful_start = review_block.find('Helpful: ') + len('Helpful: ')
            rating_start = review_block.find('Rating: ') + len('Rating: ')
            content_start = review_block.find('Content: ') + len('Content: ')
            title_end = review_block.find('(', title_start)
            title = review_block[title_start:title_end].strip()
            content = review_block[content_start:]
            helpful_end = review_block.find(',', helpful_start)
            helpful = int(review_block[helpful_start:helpful_end])
            rating_end = review_block.find(')', rating_start)
            rating = int(review_block[rating_start:rating_end])
            review_obj = {
                'make': make,
                'model': model,
                'parent_generation':year,
                'review_description': content,
                'rating_stars': rating,
                'review_title': title,
                'review_author': generate_names.generate_name(),
                'helpful': helpful,
            }
            reviews.append(review_obj)
        except ValueError:
            print(f"Error with this: {review_block}")
            with open(f'reports/{make}/{make}_{model}_{year}_reviews.txt', 'a') as file:
                file.write(f"{make},{model},{year}: Error with this: {review_block}")
            with open(f'reports/Error_reviews.txt', 'a') as file:
                file.write(f"{make},{model},{year}: Error with this: {review_block}")
                
    return reviews

parsed_reviews = parse_reviews(review_string, 'bmw', '3-series', '1997-2008')

# print(parsed_reviews[:3])


