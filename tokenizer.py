import re
from nltk.corpus import stopwords

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