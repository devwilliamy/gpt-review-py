original_prompt=f"""
Write car cover reviews in an informal, human-like style for eBay/Amazon. Include a title and content, avoid cliches. Sometimes, pick ONE of these features RANDOMLY to talk about PER review (waterproofing, UV protection, tailored fit, high-quality materials (high-end polyester fabric, soft fleece fabric, non-scratch), durability, and protection against weather, temperature changes, keeps car dry, leaves,tree,bird,animal protection, and natural elements). Ensure the reviews are relatable and authentic.

IMPORTANT: Return all responses with Title: and Content: format. Do NOT bold or italicize anything.
"""
###### Old reviews
# Give me 1 reviews where user sort of didn't like the product from ONE of these topics: (pick from color fading from sun, took too long to put on without help, didn't like the material as much, little heavier than expected) in 50 words or less Add ('Helpful: 1, Rating: 2). ONLY to the title line. Do not be too critical
# 1 where user bought for someone else OR for themselves and they loved it OR to talk about their location (Randomly Pick ONE from this list (Florida, Louisiana, Texas, North Carolina, South Carolina, Alabama, Mississippi) OR sometimes rnadomly pick another US State). Add '(Helpful: 10, Rating: 5)' ONLY to the title line OR
######

critical_prompt=f"""
Write car cover reviews in an informal, human-like style for eBay/Amazon. Include a title and content, avoid cliches. Sometimes, pick ONE of these features RANDOMLY to talk about PER review (waterproofing, UV protection, tailored fit, high-quality materials (high-end polyester fabric, soft fleece fabric, non-scratch), durability, and protection against weather, temperature changes, keeps car dry, leaves,tree,bird,animal protection, and natural elements). Ensure the reviews are relatable and authentic.

IMPORTANT: Return all responses with Title: and Content: format. Do NOT bold or italicize anything.

Here are some example reviews:
Title: Fits my Car perfectly
Content: I looked at several car covers for my Car, and this one looked like the best. It fits perfectly (make sure you use the sizing chart when ordering). However, I learned its not completely waterproof in a heavy rain. Shortly after putting it my Car, we had a severe thunderstorm, and some water did get through, probably through a seam. But Ive found no car covers are completely waterproof, so I guess it should be expected. This particular cover has adjustable retaining straps front and back, comes with an extra strap for the mid-body to secure the cover under the vehicle and grommets for an anti-theft cable or a bungee cord to keep the cover firmly in place. It also comes with an antenna grommet you can add, and a large nylon drawstring storage bag. One word of caution— I followed the instructions for installing the cover, which state that its not necessary to use the antenna grommet if you have a “flexible” antenna. Well, that didnt work out well, because when I removed the cover, which is heavy, my rubber flex antenna was bent and cracked in several places— in retrospect, my car is 15 years old, and the rubber antenna was original equipment, so the rubber was weathered and hardened. But be aware you might want to remove any detachable antennas before using this cover (a replacement antenna cost me $23 on Amazon). Other than that, Im happy with this cover, its well made, easy to install, and stayed on the car in 30MPH winds and heavy rain.
Title: Good quality Good fit
"""

def get_original_user_prompt(make, model):
    return f"""

    Give me 10 reviews total. Create your own but also use the reviews as inspiration. Don't just repeat the provided reviews, have your own spin on it.
    The title and content need to be related. Randomly choose to have make and model in title or content (10% of the time). Otherwise have the title be related to the review
    Here are the make, model.
    {make},{model}
    Use a different tone for each review provided (
    "Positive and Enthusiastic",
    "Professional and Detailed",
    "Casual and Friendly",
    "Skeptical but Fair",
    "Humorous and Light-hearted",
    "Critical but Constructive",
    "Formal and Reserved",
    "Informal and Conversational",
    "Honest and Direct",
    "Reflective and Thoughtful")
    2 reviews that are longer well written about their experience in 120 words or less. Add '(Helpful: 20, Rating: 5)'. ONLY to the title line.
    1 reviews that are skeptical but ended up loving the product in 50-120 words. Add '(Helpful: 15, Rating: 5)' ONLY to the title line.

    2 short perfect review in less than 25 words. Add (Helpful: 2, Rating: 5)  ONLY to the title line.
    4 short good review in less than 25 words. Add (Helpful: 1, Rating: 5) ONLY to the title line.
    IMPORTANT: Return all responses with Title: and Content: format. Do NOT bold or italicize anything. Only include make/model in ONE of the title or content ONCE. 
    """


def get_original_user_prompt_good(random_word_count, level_of_liking, good_topic, tone, make, model, year, random_mention):
    return f"""
    Give me a {random_word_count} word review where user felt like: {level_of_liking}. Title and content need to be related. 
    Talk about this: {good_topic} in a {tone} tone.
    Here's the make, model, year range: {make} {model} {year}
    {random_mention} 
    """

def get_critical_prompt(random_word_count, topic, tone):
    return f"""
    Give me a {random_word_count} word review where user sort of didn't like the product. Title and content need to be related. 
    Talk about this: {topic} in a {tone} tone.
    """