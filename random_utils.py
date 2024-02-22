import random 

def generate_random_word_count(start, end):
    return random.randint(start, end)
critical_topics = [
"The cover was a bit heavy.",
"It was a little harder for one person to put on.",
"My package came later than expected.",
"UPS lost my package.",
"The fit was a bit tighter than expected.",
"My wheel wasn't covered all the way to the ground.",
"It fit really well but it doesn't cover my wheels all the way",
"The storage bag that came with it was too small.",
"I really like the way it fits, but I received the wrong color.",
"I received the wrong color, but customer service sent the right one immediately.",
"I didn't like it, at least the return process was easy",
"The return was easy, but I didn't like it.",
"It's convenient for quick use, but folding it back into the storage bag takes some effort.",
"I needed some help putting it on, difficult when it's by myself",
"It took some time to figure out the correct orientation for installation.",
"Took me awhile to put it on",
"The cover does its job, but it's a bit challenging to fold neatly for storage.",
"It fits well, but I had to adjust it a few times to get it just right.",
"It's heavy duty and easy to store, but I wish it came with a larger storage bag.",
"The customer service was helpful, but the response time could be faster.",
"The price is reasonable, but I would have liked a few more color options.",
"The installation instructions could be clearer for first-time users.",
"It's convenient for quick use, but folding it back into the storage bag takes some effort.",
"The cover protects the car well, but it's a bit bulky when folded up.",
"The cover is easy to use, but a few more instructions on the best way to put it on would be helpful.",
"The cover provides good protection, but it was a little heavy to handle alone",
"It's a snug fit, but I wish it extended a bit further down the sides.",
"It's great for keeping the car clean, but I had to wait longer than expected for delivery.",
]

tonalities = [
"Positive and Enthusiastic",
"Professional and Detailed",
"Casual and Friendly",
"Skeptical but Fair",
"Humorous and Light-hearted",
"Critical but Constructive",
"Formal and Reserved",
"Informal and Conversational",
"Honest and Direct",
"Reflective and Thoughtful",
]
def generate_random_topic():
    return random.choice(critical_topics)

def generate_random_tonality():
    return random.choice(tonalities)

# print(generate_random_word_count(10, 20))
# print(generate_random_topic())
# print(generate_random_tonality())