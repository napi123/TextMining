import re
from nltk import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def cleaning(t: str) -> str:
    emotikony = re.findall(r'[;|:][-]?[\)|\(|<|>]', t)
    tekst_male = t.lower()
    usun_liczby = re.sub(r'\d', '', tekst_male)
    usun_html = re.sub(r'<.*?>', '', usun_liczby)
    usun_interp = re.sub(r'\W(?<!\s)', '', usun_html)
    usun_spacje = usun_interp.strip()
    oczyszczony = usun_spacje + ' '.join(emotikony)
    return oczyszczony


def stopword(t: str) -> str:
    stop_words = stopwords.words("english")
    filtrowany_tekst = [w for w in t if not w.lower() in stop_words]
    return filtrowany_tekst


def stemming(t: str) -> str:
    ps = PorterStemmer()
    return ps.stem(t)


def tokenizer(t: str):
    oczyszczony = cleaning(t)
    tokeny = word_tokenize(oczyszczony)
    bez_stop_words = stopword(tokeny)
    return [stemming(w) for w in bez_stop_words if len(w) > 3]
