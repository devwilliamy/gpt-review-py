import random_utils
from openai import OpenAI
import os
import re
from nltk.corpus import stopwords
from prompts import *
import tokenizer

api_key=os.environ.get("OPENAI_API_KEY"),
review_generation_output_report_dir=os.environ.get("REVIEW_GENERATION_OUTPUT_REPORT_DIR")
if api_key is None or review_generation_output_report_dir is None:
    print("Error: OPENAI_API_KEY or REVIEW_GENERATION_OUTPUT_REPORT_DIR environment variables are not set.")
    exit(1)
client = OpenAI(api_key)

# print(os.environ.get("OPENAI_API_KEY"))

# new_system_content = clean_stopwords(system_content)
########################
# Tokenize
# Why tokenize? To try to reduce the amount of tokens passed into ChatGPT to save money
# This will take out certain words that don't add to the prompt
# Will also remove spaces and symbols
########################
new_system_content = tokenizer.clean_stopwords(original_prompt)
new_system_content_2 = tokenizer.clean_text(new_system_content)

review_count = 0

def generate_review(make, model, year):
    global review_count
    print(f"Review Count: {review_count}")
    review_count += 1
    ########################
    # Random topics and such
    ########################
    random_word_count = random_utils.generate_random_word_count(10, 50)
    topic = random_utils.generate_random_topic()
    good_topic = random_utils.generate_random_good_topic()
    tone = random_utils.generate_random_tonality()
    level_of_liking = random_utils.generate_random_level_of_liking()
    random_mention = random_utils.random_mentions()
    ########################
    # Prompts
    ########################
    user_prompt_original=get_original_user_prompt(make, model)
    user_prompt_critical=get_critical_prompt(random_word_count, topic, tone)
    user_prompt_good = get_original_user_prompt_good(random_word_count, level_of_liking, good_topic, tone, make, model, year, random_mention)
    # new_user_prompt = clean_stopwords(user_prompt)
    # new_user_prompt_2 = clean_text(new_user_prompt)

    ########################
    # Actual Generation
    ########################
    print(f'Generating...{make},{model},{year}')
    print(f'Random Options: {random_word_count}, {topic}, {tone}')
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_content_good},
        {"role": "user", "content": user_prompt_good}
    ]
    )

    #####################
    ### Writing Report ##
    #####################
    print(f'Finished Generating, writing report...{make},{model},{year}')
    directory = f'{review_generation_output_report_dir}/{make}'
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
    with open(f'{review_generation_output_report_dir}/token_tracker.txt', 'a') as file:
      file.write(f'{make}_{model}_{year}_reviews')
      file.write(f'\ncompletion_tokens: {completion.usage.completion_tokens}, ')
      file.write(f'prompt_tokens:, {completion.usage.prompt_tokens}, ')
      file.write(f'total_tokens:, {completion.usage.total_tokens}\n')
    return(completion.choices[0].message.content)
