import string
import nltk

#nltk.download('stopwords')

def remove_punctuation(text):
    translator = text.maketrans('', '', string.punctuation)
    return text.translate(translator)

def remove_stop_words(text):
    stop_words = nltk.corpus.stopwords.words('english')
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

def preprocess_text(text):
    text = remove_punctuation(text)
    text = remove_stop_words(text)
    return text.upper()

text = ""
with open('../data/before-preprocessing/text1.txt', 'r') as f:
    text = f.read()


preprocess_text_ = preprocess_text(text)

with open('../data/after-preprocessing/text1.txt', 'w') as f:
    f.write(preprocess_text_)
