# Creating the bot

## Goals
- Create 10 reviews for each make and model
- 1 critical review
- 2 longer well written review about their experience
- 3 skeptical but ended up loving the product
- 1 bought for someone else and they loved it
- 1 to talk about their location (Florida, Louisiana, Texas, North Carolina, South Carolina, Alabama, Mississippi)
- 1 short perfect review
- 1 short good review


## Steps

!! Need to try to add helpful and rating to them

- Read make/model/generation
    - Get an array of each of these
- Maybe plug in all the array?
- get completion.choices[0].message.content
- run that through reivew_parser
    - return object
- fill in review_author with generate_names
- 