import string
import nltk
import unicodedata

#nltk.download('stopwords')

def remove_punctuation(text):
    translator = text.maketrans('', '', string.punctuation)
    return text.translate(translator)

def remove_stop_words(text):
    stop_words = nltk.corpus.stopwords.words('english')
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

def remove_numbers(text):
    return ''.join([i for i in text if not i.isdigit()])

def preprocess_text(text):
    text = remove_punctuation(text)
    text = remove_stop_words(text)
    text = remove_numbers(text)
    text = remove_accents(text)
    return text.upper()

# remove accents from a string
def remove_accents(letter):
    return unicodedata.normalize("NFD", letter).encode("ascii", "ignore").decode()

text = ""
with open('../data/before-preprocessing/alice_en.txt', 'r') as f:
    text = f.read()


preprocess_text_ = preprocess_text(text)

with open('../data/after-preprocessing/alice_en.txt', 'w') as f:
    f.write(preprocess_text_)
