# GPT Reviews

## Installing Stopwords
In order to use stopwords, have to open Python interpreter

```py
import nltk
nltk.download('stopwords')
``` 

### Steps
Before I forget how this works, quick instructions:
Main.py
- Need a distinct list of make / model / year / type from supabase
- Update to and from count in .env
- If you want to skip reviews, uncomment the thing (mainly for making critical reviews)
-  review_generation.generate_review will run
  - This is where ChatGPT lies
  - Can set different word counts, use random_utils to set different topics
  - Will need to change prompts for regular reviews vs critical
  - Can set own topics to have it go off of (more topics the better)
  - Note some topics have been kinda bad ("Just say it was okay","Just say you liked it","Just say it's a really great product") these will sometimes literally have those as the review
  - NEED TO update folder names and/or file names for input, output, and reports
- After reviews have been generated, will attempt to parse the GPT reviews to put it into a structure for writing to CSV
- This parser will try to find Title and Content
  - However, there was a time where I was doing (Helpful: and Content:) and parsing it like that. GPT had issues being consistent about it, so might be better assigning it after
- After the parser, it should write a CSV
- If you have multiple CSV (because you batched it), run the csv_combine (you can run just the script, don't need to do it from main)
  - Have to update foldesr/filenames if needed
- After that, need to clean it, can run the script itself , don't need to do main
  - Have to update foldesr/filenames if needed
- After that, can upload it to supabase
  - Give it id column (uuid)
- Find the scripts for reviews
  - Probably have to add review at column to the gpt review table 
  - randomize that 
  - if images are in can skip that step in the sql sccript
  - insert into reviews table, make sure slugs are updated with the script
- If review images aren't already starting with it , have to create another csv with id, type, helpful and the count 
- Run the fix_image_and_helpful script 
- Add table to supabase
- Update the GPT table with that one
- and then update the rest of stuff 

- And then i dno't know what the heck else there is to do

### TODOS
- Improve the initial review generation to include cover type (will be able to remove a step)
- Probably also want to add in columns for review_image
- Include step for randomizing helpfulness and adding photos in an earlier step (currently it's away)
- Need to re-incorporate critical reviews with the process so don't have to do separate step
  - Will probably need some more ternaries and stuff 
- Make changing folder names / file names easier 
- Improve Supabase Script or extract the important parts out (GPT Reviews & Reviews-2)
