import os
import nltk
import spacy
import string
import spacy.cli
import json

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

NLTK_DATA_PATH = os.path.expanduser("~") + "/nltk_data"
if not os.path.exists(NLTK_DATA_PATH):
    os.makedirs(NLTK_DATA_PATH)

nltk.data.path.append(NLTK_DATA_PATH)

try:
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords', download_dir=NLTK_DATA_PATH)

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', download_dir=NLTK_DATA_PATH)

try:
    nlp = spacy.load("en_core_web_sm")
    spacy.prefer_gpu()
except OSError:
    print("Downloading spaCy model 'en_core_web_sm'...")
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")


def search_products(sentence):
    stopWords = set(stopwords.words('english'))
    punctuations = set(string.punctuation)

    TokenizedSentence = word_tokenize(sentence)
    FilteredSentence = [
        word.lower() for word in TokenizedSentence
        if word.lower() not in stopWords and word not in punctuations
    ]

    sentence_ = " ".join(FilteredSentence)
    doc = nlp(sentence_)

    print("Original Sentence:", sentence)
    print("Tokenized Sentence:", TokenizedSentence)
    print("Filtered Sentence:", FilteredSentence)

    with open("products.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    for token in doc:
        print(f"{token.text:<10} {token.pos_:<10} {token.tag_:<10} {token.dep_:<10} {token.lemma_:<10}")
    
    search_name = lambda data, term: list(filter(lambda x: term.lower() in x["name"].lower(), data))

    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)

    print(f"\n{'Products':<20}Shelf Location")
    productList = []

    for token in doc:
        if (token.pos_ == "NOUN" or token.pos_ == "PROPN") and not token.is_stop:
            product = {}
            products = search_name(data["goods"], token.lemma_)
            #print(f" - {token.text} ({token.lemma_}) - ", f"Shelf {products[0]['shelf_number']}" if products else "Not found")
            pro = f"{token.lemma_:<20}"
            shell = f"{products[0]['shelf_number']}" if products else "Not found"
            product["printElement"] =  pro + shell
            product["location"] = products[0]['shelf_number'] if products else "Not found"
            productList.append(product)

    sorted_productList = sorted(productList, key=lambda x: (x["location"] == "Not found", x["location"]))

    if sorted_productList:
        for product in sorted_productList:
            print(product["printElement"])


#GivenSentence = "I want to buy Apples, milk, and detergent."
#search_products(GivenSentence)

if __name__ == "__main__":
    while(True):
        #handle key board interrupt
        try:
            input_sentence = input("\nEnter a sentence (or 'exit'/'ctrl+c' to quit): ")
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        if input_sentence.lower() == 'exit':
            break
        #clear terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        
        search_products(input_sentence)
