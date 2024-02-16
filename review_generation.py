from openai import OpenAI
import os
import re
# client = OpenAI()
client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY"),
)

system_content = """
Write car cover reviews in an informal, human-like style for eBay/Amazon. Include a title and content, avoid cliches. Highlight features like waterproofing, UV protection, tailored fit, high-quality materials (high-end polyester fabric, soft fleece fabric, non-scratch), durability, and protection against weather, temperature changes, keeps car dry, leaves,tree,bird,animal protection, and natural elements. Ensure the reviews are relatable and authentic.

Return all responses with Title: and Content:

Here are some example reviews:
Title: Fits my Car perfectly
Content: I looked at several car covers for my Car, and this one looked like the best. It fits perfectly (make sure you use the sizing chart when ordering). However, I learned it’s not completely waterproof in a heavy rain. Shortly after putting it my Car, we had a severe thunderstorm, and some water did get through, probably through a seam. But I’ve found no car covers are completely waterproof, so I guess it should be expected. This particular cover has adjustable retaining straps front and back, comes with an extra strap for the mid-body to secure the cover under the vehicle and grommets for an anti-theft cable or a bungee cord to keep the cover firmly in place. It also comes with an antenna grommet you can add, and a large nylon drawstring storage bag. One word of caution— I followed the instructions for installing the cover, which state that it’s not necessary to use the antenna grommet if you have a “flexible” antenna. Well, that didn’t work out well, because when I removed the cover, which is heavy, my rubber flex antenna was bent and cracked in several places— in retrospect, my car is 15 years old, and the rubber antenna was original equipment, so the rubber was weathered and hardened. But be aware you might want to remove any detachable antennas before using this cover (a replacement antenna cost me $23 on Amazon). Other than that, I’m happy with this cover, it’s well made, easy to install, and stayed on the car in 30MPH winds and heavy rain.
Title: Good quality Good fit
Content: I bought the CoverlandCar Cover Waterproof All Weather for my Car after reading reviews from other people . I agreefits perfect. We had rain and snow. My car stayed dry under this cover. I’m satisfied with the purchase and recommend it to others
Title: Coverland Premium Car Cover is Legitimately A Good Investment of Protection Comparatively
Content: I've bought many other brands of car covers in years past. All stating that they are waterproof, but truly can attest that this Coverland Premium cover does exactly what it states excellent water protection + I've recently had winds over 20 mph and the fitted car cover adheres perfectly without any concerns ever. In comparison to many other car tarp purchases, this brand has certainly lived up to how well it's rated I'm truly impressed and satisfied with this car cover purchase. This purchase has proven so far to be one of my best every auto covers over decades.
Title: Great truck cover!
Content: This cover is waterproof. It’s also easy to dry off after a rain. I’ve purchased many truck covers over the years. This is the best and the least expensive truck cover I have ever purchased.
The only bad is I would like to have mirror pockets.
Title: Almost As Good as a Garage
Content: I'm very pleased with this car cover. It is fully waterproof and relatively easy to remove and replace. The cover adapts to the shape of the vehicle over time and gets easier to use. I wish I had bought one years ago, as I do not have a home garage.
Title: Great fit!
Content: I’ve paid lots of money for custom covers that were a pain to put on and keep on the car. It was a breeze to put on, albeit I had to remove the antenna because I didn’t want to try my hand at installing the grommet. It rained shortly after installing and it’s really waterproof! The zipper entry to the drivers door is really a great feature.
Title: Great fit and seems very durable
Content: Fits great and really covers car. Waterproof, and seems to be holding up, believe this will last longer than the budge covers sold in store by Walmart.
Title: Best cover and outstanding customer service!Content: I have bought many covers for my Car, and this cover has been the best: fits well, proved to be waterproof, and easy to put on and secure. The only problem is it only lasted 7 months. However, 7 months in the harsh South Florida sun for the price is excellent! Also, when I contacted the company, I found out that I had an extended warranty. I provided a few pictures to show the material deteriorating, and the company sent me a new cover! The customer service was terrific! They were fast, polite and professional! I have already received a new cover, and I will continue to do business with them.
Title: ThinContent: This seems more like 2 layers than 10 but it is waterproof and a good value. It fit my car very well and the buckle straps keep it in place. Recommended.
Title: Coverland Premium Car Cover Waterproof All Weather for Buick Roadmaster 228" lengthContent: Likes: fits very well, including where the mirrors are; zipper to get into car is a handy feature; reflectors; straps for windproofing; color less likely to absorb heat; keeps car dry except... Dislike: leaks through at the seams. Almost brought it back but husband likes the other features, so he's going to try waterproof spray on the seams to help prevent leakage. Can't comment on durability after only one month
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
    Give me 1 reviews where user didn't like the product in 50 words or less Add ('Helpful: 1, Rating: 2). ONLY to the title line. 
    2 reviews that are longer well written about their experience in 120 words or less. Add '(Helpful: 20, Rating: 5)'. ONLY to the title line.
    3 reviews that are skeptical but ended up loving the product in 50-120 words. Add '(Helpful: 15, Rating: 5)' ONLY to the title line.
    1 where user bought for someone else and they loved it. Add '(Helpful: 10, Rating: 5)' ONLY to the title line.
    1 to talk about their location (Florida, Louisiana, Texas, North Carolina, South Carolina, Alabama, Mississippi). Add '(Helpful: 5, Rating: 5)' ONLY to the title line.
    1 short perfect review in less than 25 words. Add (Helpful: 2, Rating: 5)  ONLY to the title line.
    1 short good review in less than 25 words. Add (Helpful: 1, Rating: 5) ONLY to the title line.
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

#     - 1 critical review
# - 2 longer well written review about their experience
# - 3 skeptical but ended up loving the product
# - 1 bought for someone else and they loved it
# - 1 to talk about their location (Florida, Louisiana, Texas, North Carolina, South Carolina, Alabama, Mississippi)
# - 1 short perfect review
# - 1 short good review
    )
    # print(completion.choices[0].message.content)   
    # print(
    # 'completion_tokens:', completion.usage.completion_tokens,
    # 'prompt_tokens:', completion.usage.prompt_tokens,
    # 'total_tokens:', completion.usage.total_tokens
    # )
    print(f'Finished Generating, writing report...{make},{model},{year}')

    with open(f'reports/{make}_{model}_{year}_reviews.txt', 'a') as file:
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