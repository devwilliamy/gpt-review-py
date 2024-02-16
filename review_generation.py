from openai import OpenAI
import os
import re
# client = OpenAI()
client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY"),
)

system_content = """
Write car cover reviews in an informal, human-like style for eBay/Amazon. Include a title and content, avoid cliches. Sometimes, pick ONE of these features RANDOMLY to talk about PER review (waterproofing, UV protection, tailored fit, high-quality materials (high-end polyester fabric, soft fleece fabric, non-scratch), durability, and protection against weather, temperature changes, keeps car dry, leaves,tree,bird,animal protection, and natural elements). Ensure the reviews are relatable and authentic.

Return all responses with Title: and Content:

Here are some example reviews:
Title: Fits my Car perfectly
Content: I looked at several car covers for my Car, and this one looked like the best. It fits perfectly (make sure you use the sizing chart when ordering). However, I learned it’s not completely waterproof in a heavy rain. Shortly after putting it my Car, we had a severe thunderstorm, and some water did get through, probably through a seam. But I’ve found no car covers are completely waterproof, so I guess it should be expected. This particular cover has adjustable retaining straps front and back, comes with an extra strap for the mid-body to secure the cover under the vehicle and grommets for an anti-theft cable or a bungee cord to keep the cover firmly in place. It also comes with an antenna grommet you can add, and a large nylon drawstring storage bag. One word of caution— I followed the instructions for installing the cover, which state that it’s not necessary to use the antenna grommet if you have a “flexible” antenna. Well, that didn’t work out well, because when I removed the cover, which is heavy, my rubber flex antenna was bent and cracked in several places— in retrospect, my car is 15 years old, and the rubber antenna was original equipment, so the rubber was weathered and hardened. But be aware you might want to remove any detachable antennas before using this cover (a replacement antenna cost me $23 on Amazon). Other than that, I’m happy with this cover, it’s well made, easy to install, and stayed on the car in 30MPH winds and heavy rain.
Title: Good quality Good fit
Content: I bought the CoverlandCar Cover Waterproof All Weather for my Car after reading reviews from other people . I agreefits perfect. We had rain and snow. My car stayed dry under this cover. I’m satisfied with the purchase and recommend it to others
Title: Coverland Premium Car Cover is Legitimately A Good Investment of Protection Comparatively
Content: I've bought many other brands of car covers in years past. All stating that they are waterproof, but truly can attest that this Coverland Premium cover does exactly what it states excellent water protection + I've recently had winds over 20 mph and the fitted car cover adheres perfectly without any concerns ever. In comparison to many other car tarp purchases, this brand has certainly lived up to how well it's rated I'm truly impressed and satisfied with this car cover purchase. This purchase has proven so far to be one of my best every auto covers over decades.
Title: Great car cover!
Content: This cover is waterproof. It’s also easy to dry off after a rain. I’ve purchased many car covers over the years. This is the best and the least expensive car cover I have ever purchased.
The only bad is I would like to have mirror pockets.
Title: Almost As Good as a Garage
Content: I'm very pleased with this car cover. It is fully waterproof and relatively easy to remove and replace. The cover adapts to the shape of the vehicle over time and gets easier to use. I wish I had bought one years ago, as I do not have a home garage.
Title: Great fit!
Content: I’ve paid lots of money for custom covers that were a pain to put on and keep on the car. It was a breeze to put on, albeit I had to remove the antenna because I didn’t want to try my hand at installing the grommet. It rained shortly after installing and it’s really waterproof! The zipper entry to the drivers door is really a great feature.
Title: Great fit and seems very durable
Content: Fits great and really covers car. Waterproof, and seems to be holding up, believe this will last longer than the budge covers sold in store by Walmart.
Title: Best cover and outstanding customer service!Content: I have bought many covers for my Car, and this cover has been the best: fits well, proved to be waterproof, and easy to put on and secure. The only problem is it only lasted 7 months. However, 7 months in the harsh South Florida sun for the price is excellent! Also, when I contacted the company, I found out that I had an extended warranty. I provided a few pictures to show the material deteriorating, and the company sent me a new cover! The customer service was terrific! They were fast, polite and professional! I have already received a new cover, and I will continue to do business with them.
Title: ThinContent: This seems more like 2 layers than 10 but it is waterproof and a good value. It fit my car very well and the buckle straps keep it in place. Recommended.
Title: Coverland Car Cover" Content: Likes: fits very well, including where the mirrors are; zipper to get into car is a handy feature; reflectors; straps for windproofing; color less likely to absorb heat; keeps car dry except... Dislike: leaks through at the seams. Almost brought it back but husband likes the other features, so he's going to try waterproof spray on the seams to help prevent leakage. Can't comment on durability after only one month
Content: Bought the small convertible one for use with my 1987 Honda CRX and it fits perfectly. Covers every part of the car, and is a bit long but not long enough to be an issue. The straps are flimsy and one clip came damaged, but I really needed the cover so it just adapted it with some homemade stuff. Truly waterproof and sturdy for the price.
Content: Great price! Quality of cover is MUCH better than expected at this price.

Problem: The fasteners on the front part of the cover aren’t the same size. Front clips don’t fit together, so you can’t snap them together to secure the cover on the boat.

Back fasteners fit together perfectly. Obviously a manufacturing error with the front clips.

If the wind is always at your back, you’re golden … OR — you can tie the front two tie-downs together instead of using the fasteners. Works for me. :)

Side Note: Plastic Fasteners eventually break/warp anyway — in any kind of weather. 
Content: Everything about this product is great. Some things to keep handy when using this for snow freezing weather is: 1-2 construction bags for storage, grip gloves, ski mask. The bag that comes with it you can store when no longer using it, but when your taking it off/on your car you'll want the construction bag to stay in your car. It's going to take a few minutes getting it off and on so keep gloves in your car that you can use to put it on. The straps are tiny but sturdy, there three straps front middle and back that clip to opposite side. Ski mask when it's snowing and windy and your taking it off the snow will hit your face, stay warm, drive slow and keep lights on for young and elderly to see you on the roads stay safe everyone!🙏❤️

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
"""
def clean_stopwords(text: str) -> str:
    stopwords = ["a", "an", "and", "at", "but", "how", "in", "is", "on", "or", "the", "to", "what", "will"]
    tokens = text.split()
    clean_tokens = [t for t in tokens if not t in stopwords]
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
new_system_content = clean_stopwords(system_content)
new_system_content_2 = clean_text(new_system_content)
# print(new_string_2)
# print(len(new_string_2))


# print(new_user_prompt_2)
def generate_review(make, model, year):
    user_prompt=f"""
    Give me 10 reviews total.
    The title and content need to be related. You can have make and model and year in title ONCE. Otherwise have the title be related to the review
    Here are the make, model, year range.
    {make},{model},{year}
    Give me 1 reviews where user sort of didn't like the product from ONE of these topics: (pick from color fading from sun, took too long to put on without help, didn't like the material as much, little heavier than expected) in 50 words or less Add ('Helpful: 1, Rating: 2). ONLY to the title line. Do not be too critical
    2 reviews that are longer well written about their experience in 120 words or less. Add '(Helpful: 20, Rating: 5)'. ONLY to the title line.
    2 reviews that are skeptical but ended up loving the product in 50-120 words. Add '(Helpful: 15, Rating: 5)' ONLY to the title line.
    1 where user bought for someone else OR for themselves and they loved it OR to talk about their location (Randomly Pick ONE from this list (Florida, Louisiana, Texas, North Carolina, South Carolina, Alabama, Mississippi) OR sometimes rnadomly pick another US State). Add '(Helpful: 10, Rating: 5)' ONLY to the title line OR
    2 short perfect review in less than 25 words. Add (Helpful: 2, Rating: 5)  ONLY to the title line.
    2 short good review in less than 25 words. Add (Helpful: 1, Rating: 5) ONLY to the title line.
    """
    new_user_prompt = clean_stopwords(user_prompt)
    new_user_prompt_2 = clean_text(new_user_prompt)
    print(f'Generating...{make},{model},{year}')
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    # model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": new_system_content_2},
        {"role": "user", "content": user_prompt}
    ]
    )
    # print(completion.choices[0].message.content)   
    # print(
    # 'completion_tokens:', completion.usage.completion_tokens,
    # 'prompt_tokens:', completion.usage.prompt_tokens,
    # 'total_tokens:', completion.usage.total_tokens
    # )
    print(f'Finished Generating, writing report...{make},{model},{year}')
    directory = f'reports/{make}'

    # Create the directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)

    # Specify the file path
    file_path = os.path.join(directory, f'{make}_{model}_{year}_reviews.txt')

    with open(file_path, 'a') as file:
      file.write(completion.choices[0].message.content)
      file.write(f'\ncompletion_tokens: {completion.usage.completion_tokens}, ')
      file.write(f'prompt_tokens:, {completion.usage.prompt_tokens}, ')
      file.write(f'total_tokens:, {completion.usage.total_tokens}\n')
    with open(f'reports/token_tracker.txt', 'a') as file:
      file.write(f'{make}_{model}_{year}_reviews')
      file.write(f'\ncompletion_tokens: {completion.usage.completion_tokens}, ')
      file.write(f'prompt_tokens:, {completion.usage.prompt_tokens}, ')
      file.write(f'total_tokens:, {completion.usage.total_tokens}\n')
    return(completion.choices[0].message.content)

# generate_review()