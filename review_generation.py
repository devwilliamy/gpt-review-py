import random_utils
from openai import OpenAI
import os
import re
from nltk.corpus import stopwords

# client = OpenAI()
client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY"),
)

system_content = """
Write car cover reviews in an informal, human-like style for eBay/Amazon. Include a title and content, avoid cliches. Sometimes, pick ONE of these features RANDOMLY to talk about PER review (waterproofing, UV protection, tailored fit, high-quality materials (high-end polyester fabric, soft fleece fabric, non-scratch), durability, and protection against weather, temperature changes, keeps car dry, leaves,tree,bird,animal protection, and natural elements). Ensure the reviews are relatable and authentic.

IMPORTANT: Return all responses with Title: and Content: format. Do NOT bold or italicize anything.

Here are some example reviews:
Title: Fits my Car perfectly
Content: I looked at several car covers for my Car, and this one looked like the best. It fits perfectly (make sure you use the sizing chart when ordering). However, I learned its not completely waterproof in a heavy rain. Shortly after putting it my Car, we had a severe thunderstorm, and some water did get through, probably through a seam. But Ive found no car covers are completely waterproof, so I guess it should be expected. This particular cover has adjustable retaining straps front and back, comes with an extra strap for the mid-body to secure the cover under the vehicle and grommets for an anti-theft cable or a bungee cord to keep the cover firmly in place. It also comes with an antenna grommet you can add, and a large nylon drawstring storage bag. One word of caution— I followed the instructions for installing the cover, which state that its not necessary to use the antenna grommet if you have a “flexible” antenna. Well, that didnt work out well, because when I removed the cover, which is heavy, my rubber flex antenna was bent and cracked in several places— in retrospect, my car is 15 years old, and the rubber antenna was original equipment, so the rubber was weathered and hardened. But be aware you might want to remove any detachable antennas before using this cover (a replacement antenna cost me $23 on Amazon). Other than that, Im happy with this cover, its well made, easy to install, and stayed on the car in 30MPH winds and heavy rain.
Title: Good quality Good fit
Content: I bought the Coverland Car Cover for my Car after reading reviews from other people . I agreefits perfect. We had rain and snow. My car stayed dry under this cover. Im satisfied with the purchase and recommend it to others
Title: Coverland Premium Car Cover is Legitimately A Good Investment of Protection Comparatively
Content: I've bought many other brands of car covers in years past. All stating that they are waterproof, but truly can attest that this Coverland Premium cover does exactly what it states excellent water protection + I've recently had winds over 20 mph and the fitted car cover adheres perfectly without any concerns ever. In comparison to many other car tarp purchases, this brand has certainly lived up to how well it's rated I'm truly impressed and satisfied with this car cover purchase. This purchase has proven so far to be one of my best every auto covers over decades.
Title: Great car cover!
Content: This cover is waterproof. Its also easy to dry off after a rain. Ive purchased many car covers over the years. This is the best and the least expensive car cover I have ever purchased.
The only bad is I would like to have mirror pockets.
Title: Almost As Good as a Garage
Content: I'm very pleased with this car cover. It is fully waterproof and relatively easy to remove and replace. The cover adapts to the shape of the vehicle over time and gets easier to use. I wish I had bought one years ago, as I do not have a home garage.
Title: Great fit!
Content: Ive paid lots of money for custom covers that were a pain to put on and keep on the car. It was a breeze to put on, albeit I had to remove the antenna because I didnt want to try my hand at installing the grommet. It rained shortly after installing and its really waterproof! The zipper entry to the drivers door is really a great feature.
Title: Great fit and seems very durable
Content: Fits great and really covers car. Waterproof, and seems to be holding up, believe this will last longer than the budge covers sold in store by Walmart.
Title: Best cover and outstanding customer service!Content: I have bought many covers for my Car, and this cover has been the best: fits well, proved to be waterproof, and easy to put on and secure. The only problem is it only lasted 7 months. However, 7 months in the harsh South Florida sun for the price is excellent! Also, when I contacted the company, I found out that I had an extended warranty. I provided a few pictures to show the material deteriorating, and the company sent me a new cover! The customer service was terrific! They were fast, polite and professional! I have already received a new cover, and I will continue to do business with them.
Title: ThinContent: This seems more like 2 layers than 10 but it is waterproof and a good value. It fit my car very well and the buckle straps keep it in place. Recommended.
Title: Coverland Car Cover" Content: Likes: fits very well, including where the mirrors are; zipper to get into car is a handy feature; reflectors; straps for windproofing; color less likely to absorb heat; keeps car dry except... Dislike: leaks through at the seams. Almost brought it back but husband likes the other features, so he's going to try waterproof spray on the seams to help prevent leakage. Can't comment on durability after only one month
Content: Bought the small convertible one for use with my 1987 Honda CRX and it fits perfectly. Covers every part of the car, and is a bit long but not long enough to be an issue. The straps are flimsy and one clip came damaged, but I really needed the cover so it just adapted it with some homemade stuff. Truly waterproof and sturdy for the price.
Content: Great price! Quality of cover is MUCH better than expected at this price.

Problem: The fasteners on the front part of the cover arent the same size. Front clips dont fit together, so you cant snap them together to secure the cover on the boat.

Back fasteners fit together perfectly. Obviously a manufacturing error with the front clips.

If the wind is always at your back, youre golden … OR — you can tie the front two tie-downs together instead of using the fasteners. Works for me. :)

Side Note: Plastic Fasteners eventually break/warp anyway — in any kind of weather. 
Content: Everything about this product is great. Some things to keep handy when using this for snow freezing weather is: 1-2 construction bags for storage, grip gloves, ski mask. The bag that comes with it you can store when no longer using it, but when your taking it off/on your car you'll want the construction bag to stay in your car. It's going to take a few minutes getting it off and on so keep gloves in your car that you can use to put it on. The straps are tiny but sturdy, there three straps front middle and back that clip to opposite side. Ski mask when it's snowing and windy and your taking it off the snow will hit your face, stay warm, drive slow and keep lights on for young and elderly to see you on the roads stay safe everyone!

Content: I bought this cover in December 2020 and it lasted until August 2021 sitting out in the elements 24/7 for those 8 months. One day it just decided it had had enough and basically ripped in half. I plan to buy another one of these but I decided to read reviews (because that's what I like to do for entertainment) before re-ordering. The biggest complaints I've see is "it's not waterproof" and "for the money I spent blah blah blah".

First of all, this is a budget car cover at it's $37 price point and you aren't going to find one that cheap at your local parts store unless it's on sale. The $40+ car covers sold at auto parts stores are not waterproof and will shred apart or blow away with the slightest wind. This car cover at least has 3 straps built-in that will hold it in place so it's definitely not blowing away.

Second, I can't attest for the waterproof aspect of it and while I understand that the description says it's waterproof, even if it's not I have to point back to the price again. What did you think you were getting for $37? If your vehicle needs to be protected from the rain that bad, you may want to consider a garage or storage. If that isn't an option then you're looking at spending $100+ for a car cover that's going to stand up to all of the elements for any extended period of time. I've had a 1991 Firebird that I've kept covered outdoors for 5+ years and I've bought probably 4 or 5 different brand car covers in this price range. There's one things consistent amongst them all ..... they're only going to last you about 8-12 months tops. That's just how it goes when you buy a budget car cover.

year it's far cheaper than paying for a storage unit to put the car in.

UPDATE: The 4th cover lasted 4 months. I might start buying these 2 at a time especially when they're on sale. Right now they're only $22 which is actually closer to what I'd like to pay for these regularly. Still can't complain about a $20-$30 car cover that lasts a few months. I couldn't get a storage unit this cheap to store it in.

UPDATE: My 5th cover lasted 5 months. At this point, I'm just updating this review for research purposes.

Serves it purpose. Pleased for money sent

I got this so I didn't have to scrape the ice off my car and it's a pretty wise idea especially in the morning. Could fit my car better but the straps do their jobs.

Little too big for my classic car but still fits and easy to attach

Works okay but it did rip when a twig fell on my car
Literally withstood a category 4 hurricane that destroyed a lot of our town. Straps held strong, kept the car dry in rain that was defying gravity. Would gosh dang recommend to anyone
This car cover can be used while your vehicle has be outside while your garage is being cleaned out.
Don't let your car get damaged by the weather outside - rain or snow.
Title: FIT
Content: FITS LIKE A GLOVE.

Content: I just received it today, and installed it tonight... the jury is still out. Is it 10 layers? Questionable. Am I happy w/ its construction? So far! It didn't (or mine) didn't come w/ straps to buckle one side to the other. We will see how it holds up, but I think I'll be content... if I can find straps/buckles to lock either side together, from underneath. It seems like a decent car cover, for the price. We'll see how it holds up, for the weather. The side zippers for the doors, is a plus.

Title: Perfect for my car Content: I used it today for the first time and it was VERY easy to put on. I had someone helping me. I think it would have taken longer but still been pretty easy to do by myself though, based on this experience. If I find that is not the case, I will update this review. I used it today during a rainstorm because my car has a small leak and I had to leave it outside. No water got through the cover. I would definitely recommend this for a small SUV or larger hatchback.

Title: skeptical at first given the comparatively low price; however, upon delivery, I was more than Content: pleasantly surprised with the product's overall quality, fit, and durability. Highly recommended.

Title: Works and fits well
Content: Skeptical at first.... worth the $$$ and doing what it's suppose to, even if only temporarily.

Title: Nice quality
Content: I was skeptical as to whether this would be large enough to cover our car, but it is s great fit. Certainly enough protection for inside our shed.

Title: Great Price 
Content:Great price! Quality of cover is MUCH better than expected at this price.

Problem: The fasteners on the front part of the cover aren’t the same size. Front clips don’t fit together, so you can’t snap them together to secure the cover on the boat.

Back fasteners fit together perfectly. Obviously a manufacturing error with the front clips.

If the wind is always at your back, you’re golden … OR — you can tie the front two tie-downs together instead of using the fasteners. Works for me. :)

Side Note: Plastic Fasteners eventually break/warp anyway — in any kind of weather. Faster in extreme cold or heat, but all of them do break.

Title: Fit like a dream
Content: This fit my car very well and I like the additional straps in case it’s windy. It’s a thin nylon and I haven’t checked out the waterproof yet but it looked good on my car. I’d order again.

Title: Good for the price
Content: This car cover is fairly easy to install and with the wind proof straps it works perfectly for my car where it is quite windy. I bought this as it is quite foggy where I live in the morning and the eucalyptus tree above where I park likes to leave brown residue on my car when that happens. This does do it it’s job well at preventing that. That being said, I find that this car cover is mainly water resistant and not waterproof as when it rains it still is soaking wet through the car cover. I would probably avoid using this if you want to keep water off your car if it is leaky or if you want to protect the paint from water. This is probably better suited for garaged cars. But with the outdoor use I get from this, this is more than adequate for what I need from this car cover and I’d recommend it.

Title: Trash
Content: Trash

Title: Fit like glove
Content: Such a perfect fit on my car. And looks great on it and water proof.. I love it!!!!

Title: Good product at good price
Content: The cover fits my car perfectly. It is a better looking cover than many of the other options. The day after I put it on there were high winds. The cover stayed on the car, and didn’t need any adjustments. I would buy again.

Title: Excellent for car parked in driveway
Content: I needed a cover for a car that I could not park in the garage. I have trees that shade the driveway, but also drop sap and twigs onto anything in the driveway. I chose this cover because it is extremely light weight, and also (according to the reviews) easy to install. After a couple of attempts, I did get the hang of putting the cover on, and can now do it in seconds instead of minutes. The cover will stay in place during high winds, due to the straps that fit through the wheels of the car, and snap into place with plastic connectors. There is also a strap that will go under the car in the middle, but so far, I have not had to use it. The cover protect the car from the sun, rain and sap, very efficiently! I highly recommend it!

Title: Excellent Car Cover
Content: Great quality, great price, I am very happy with this purchase

Title: Lightweight but strong
Content: Needed something to cover the car that stays outside and this does the job. Although it’s lightweight, it keeps the car clean and dry and stays in place.

Title: Fits and works so far
Content: We have has 1 wet snow storm since I put this on. The car was dry & no signs of water / dirt pentation. We will see how long this lasts that way.

So far I am happy with this cover for the about $100 paid. Not a custom fit, but good enough for what I wanted!

Title: Perfect Fit
Content: Perfect fit, no complaints. I highly recommend

Title: Pleasantly surprised
Content:  I love my jeep grand Cherokee. It has always been a great car, so I like to take as best care of it as I can. It is always been a car that has been garaged until recently. I’ve never had to deal with a hot car or it getting so much sun and weather exposure while parked. Now that I park outside I have noticed a difference in how I experience my car. It gets extremely hot and I don’t want the outside to wear unnecessarily. So I saw the reviews for this product and I thought I would try it out. The biggest reservation I have with a car cover is will I actually take the time to put it on? So my biggest concern was how durable this product is, and how easy it is to take it off and put it on. I also now live in a place where the winds get extremely forceful in the fall, so I wanted to make sure it was a product that could withstand intense winds. It literally only took me a few minutes to unwrap it and figure out which way it goes on, and finally putting it on with the wind resistant straps secured. The material is very heavy duty, but also very soft. I have confidence that it will not scratch my car. It was very easy to put on. Even the straps (see attached photos) were easy to secure. I’m going to keep it! I just have to be intentional and utilizing it to protect my Jeep.
I’ve only had this product for 20 minutes, but my review is a five-star because my experience of the quality and ease of installation thus far.

Title: Lighter than you think
COntent: It's a little much to put it on correctly but used it for my mothers car, since she is without garage.

Title: Best car cover
Content: We’ve tried ten different car covers. Two car covers a year for five years.
This is the only car cover that didn’t allow dust & dirt to get between the cover and the paint. Also there was no evidence of rain spots on the paint.
After removing the other car covers we’d always have to go rinse off all the dust & dirt.
With this cover even our neighbors commented it looks as if we just washed it.
So this car would sit outside in a covered area for two to five months at a time.

Title: Happily suprised
Content: I have bought MANY car covers and it's always a hit-or miss as to if they fit or not. About half don't fit the car they are advertised for. This one DID!

The other BIG selling point: The fabric is THICK! This is the heaviest car cover that I have ever bought.

Love it, love it, love it.

Title: Fast shipping
Content: Shipped fast. Looks good.

Title: Works
Content: Nice soft fabric on the inside to protect your car. Got it just in time to test it and it worked great for two snow storms, the first turning to freezing rain at the end making a lot of ice. saved a lot of time cleaning the car and waiting for the windows to defrost. No damage to the car or the cover, seems like it has decent quality stiching and will hold together for years.

Title: perfect
Content: This car cover is great for my car. It fits perfectly and keeps my car protected from rain, snow... No complaints at all. Highly recommend.

Title: Good quality
Content: Item quality seems pretty good. This is the first time I'm using this product, we will see how this cover holds up in our island weather which includes, high UV sunlight, heavy rains, and high winds. I'll rate this again after a couple months of our weather
"""

system_content_critical = f"""
Write car cover reviews in an informal, human-like style for eBay/Amazon. Include a title and content, avoid cliches. Sometimes, pick ONE of these features RANDOMLY to talk about PER review (waterproofing, UV protection, tailored fit, high-quality materials (high-end polyester fabric, soft fleece fabric, non-scratch), durability, and protection against weather, temperature changes, keeps car dry, leaves,tree,bird,animal protection, and natural elements). Ensure the reviews are relatable and authentic.

IMPORTANT: Return all responses with Title: and Content: format. Do NOT bold or italicize anything.

Here are some example reviews:
Title: Fits my Car perfectly
Content: I looked at several car covers for my Car, and this one looked like the best. It fits perfectly (make sure you use the sizing chart when ordering). However, I learned its not completely waterproof in a heavy rain. Shortly after putting it my Car, we had a severe thunderstorm, and some water did get through, probably through a seam. But Ive found no car covers are completely waterproof, so I guess it should be expected. This particular cover has adjustable retaining straps front and back, comes with an extra strap for the mid-body to secure the cover under the vehicle and grommets for an anti-theft cable or a bungee cord to keep the cover firmly in place. It also comes with an antenna grommet you can add, and a large nylon drawstring storage bag. One word of caution— I followed the instructions for installing the cover, which state that its not necessary to use the antenna grommet if you have a “flexible” antenna. Well, that didnt work out well, because when I removed the cover, which is heavy, my rubber flex antenna was bent and cracked in several places— in retrospect, my car is 15 years old, and the rubber antenna was original equipment, so the rubber was weathered and hardened. But be aware you might want to remove any detachable antennas before using this cover (a replacement antenna cost me $23 on Amazon). Other than that, Im happy with this cover, its well made, easy to install, and stayed on the car in 30MPH winds and heavy rain.
Title: Good quality Good fit
"""
# In order to use stopwords, have to open Python interpreter
# import nltk
# nltk.download('stopwords')

def clean_stopwords(text: str) -> str:
    # stopwords = ["a", "an", "and", "at", "but", "how", "in", "is", "on", "or", "the", "to", "what", "will"]
    nltk_stopwords = stopwords.words('english')
    tokens = text.split()
    clean_tokens = [t for t in tokens if not t in nltk_stopwords]
    return " ".join(clean_tokens)

def clean_text(text):
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    
    # Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)
    
    # Remove everything that's not a letter (a-z, A-Z)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Remove whitespace, tabs, and new lines
    text = ''.join(text.split())

    return text
print(os.environ.get("OPENAI_API_KEY"))

# new_system_content = clean_stopwords(system_content)
new_system_content = clean_stopwords(system_content_critical)
new_system_content_2 = clean_text(new_system_content)
# print(new_string_2)
# print(len(new_string_2))
# print(new_user_prompt_2)


review_count = 0
def generate_review(make, model, year):
    global review_count
    print(f"Review Count: {review_count}")
    review_count += 1
    random_word_count = random_utils.generate_random_word_count(10, 25)
    topic = random_utils.generate_random_topic()
    tone = random_utils.generate_random_tonality()
    user_prompt_original=f"""
    Give me 10 reviews total. Create your own but also use the reviews as inspiration. Don't just repeat the provided reviews, have your own spin on it.
    The title and content need to be related. You can have make and model and year in title or content ONCE. Otherwise have the title be related to the review
    Here are the make, model, year range.
    {make},{model},{year}
    Give me 1 reviews where user sort of didn't like the product from ONE of these topics: (pick from color fading from sun, took too long to put on without help, didn't like the material as much, little heavier than expected) in 50 words or less Add ('Helpful: 1, Rating: 2). ONLY to the title line. Do not be too critical
    2 reviews that are longer well written about their experience in 120 words or less. Add '(Helpful: 20, Rating: 5)'. ONLY to the title line.
    1 reviews that are skeptical but ended up loving the product in 50-120 words. Add '(Helpful: 15, Rating: 5)' ONLY to the title line.

    2 short perfect review in less than 25 words. Add (Helpful: 2, Rating: 5)  ONLY to the title line.
    4 short good review in less than 25 words. Add (Helpful: 1, Rating: 5) ONLY to the title line.
    IMPORTANT: Return all responses with Title: and Content: format. Do NOT bold or italicize anything. Only include make/model in ONE of the title or content ONCE. 
    """
    user_prompt_critical=f"""
    Give me a {random_word_count} word review where user sort of didn't like the product. Title and content need to be related. 
    Talk about this: {topic} in a {tone} tone.
    """
    # 1 where user bought for someone else OR for themselves and they loved it OR to talk about their location (Randomly Pick ONE from this list (Florida, Louisiana, Texas, North Carolina, South Carolina, Alabama, Mississippi) OR sometimes rnadomly pick another US State). Add '(Helpful: 10, Rating: 5)' ONLY to the title line OR
    # new_user_prompt = clean_stopwords(user_prompt)
    # new_user_prompt_2 = clean_text(new_user_prompt)
    print(f'Generating...{make},{model},{year}')
    print(f'Random Options: {random_word_count}, {topic}, {tone}')
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    # model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": new_system_content_2},
        {"role": "user", "content": user_prompt_critical}
    ]
    )
    # print(completion.choices[0].message.content)   
    # print(
    # 'completion_tokens:', completion.usage.completion_tokens,
    # 'prompt_tokens:', completion.usage.prompt_tokens,
    # 'total_tokens:', completion.usage.total_tokens
    # )
    print(f'Finished Generating, writing report...{make},{model},{year}')
    directory = f'reports_02212024_1408/{make}'

    # Create the directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)

    # Specify the file path
    file_path = os.path.join(directory, f'{make}_{model}_{year}_reviews.txt')

    with open(file_path, 'a') as file:
      file.write(completion.choices[0].message.content)
      file.write(f'Random Options: {random_word_count}, {topic}, {tone}')
      file.write(f'\ncompletion_tokens: {completion.usage.completion_tokens}, ')
      file.write(f'prompt_tokens:, {completion.usage.prompt_tokens}, ')
      file.write(f'total_tokens:, {completion.usage.total_tokens}\n')
    with open(f'reports_02212024_1408/token_tracker.txt', 'a') as file:
      file.write(f'{make}_{model}_{year}_reviews')
      file.write(f'\ncompletion_tokens: {completion.usage.completion_tokens}, ')
      file.write(f'prompt_tokens:, {completion.usage.prompt_tokens}, ')
      file.write(f'total_tokens:, {completion.usage.total_tokens}\n')
    return(completion.choices[0].message.content)

# generate_review()