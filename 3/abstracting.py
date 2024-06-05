#Створити новий консольний проєкт мовою Python, при запуску вивести власне прізвище, ім’я, групу, номер ЛР.
print("Міронова Євгенія, 2 група, Лабораторна робота 5")

#Імпортувати до проєкту бібліотеку NLTK та інші необхідні модулі
import nltk

from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')
nltk.download('punkt')


# Створення реферату із довільним порогом
# обчислення частотності
def freq_table(text_string) -> dict:
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text_string)
    ps = PorterStemmer()
    freqTable = dict()
    for word in words:
        word = ps.stem(word)
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
    return freqTable


# 3.1.1 частотність у тхт файлі
file = open(r"C:\штуки\holidays.txt", "r")
text = file.read()
print(freq_table(text))

# 3.2 токенізація тексту
from nltk import sent_tokenize

print(sent_tokenize(text))


# оцінювання речень
def score_sentences(sentences, freqTable) -> dict:
    sent_value = dict()
    for sent in sentences:
        word_count_in_sentence = (len(word_tokenize(sent)))
        for wordValue in freqTable:
            if wordValue in sent.lower():
                if sent[:50] in sent_value:
                    sent_value[sent[:50]] += freqTable[wordValue]
                else:
                    sent_value[sent[:50]] = freqTable[wordValue]
        sent_value[sent[:50]] = sent_value[sent[:50]] / word_count_in_sentence
    return sent_value


# рез-ти оцінювання
ft = freq_table(text)
s = sent_tokenize(text)
sv = score_sentences(s, ft)
print(sv)


# визначення порогу
def avg_score(sentValue) -> float:
    sumValues = 0
    for entry in sentValue:
        sumValues += sentValue[entry]
    average = sumValues / len(sentValue)
    return average


avg = avg_score(sv)
print(avg)


# генерування реферату
def summary(sentences, sentValue, threshold):
    sentence_count = 0
    summary = ''
    for sent in sentences:
        if sent[:50] in sentValue and sentValue[sent[:50]] > (threshold):
            summary += " " + sent
            sentence_count += 1
    return summary


summ1 = summary(s, sv, avg)
print(summ1)


# генерування реферату№2

# обчислення частотності
def freq_table(text_string) -> dict:
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text_string)
    ps = PorterStemmer()
    freqTable = dict()
    for word in words:
        word = ps.stem(word)
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
    return freqTable

# частотність у тхт файлі
file = open(r"holidays.txt", "r")
text = file.read()
print(freq_table(text))

# токенізація тексту
from nltk import sent_tokenize

print(sent_tokenize(text))


# оцінювання речень
def score_sentences(sentences, freqTable) -> dict:
    sent_value = dict()
    for sent in sentences:
        word_count_in_sentence = (len(word_tokenize(sent)))
        for wordValue in freqTable:
            if wordValue in sent.lower():
                if sent[:50] in sent_value:
                    sent_value[sent[:50]] += freqTable[wordValue]
                else:
                    sent_value[sent[:50]] = freqTable[wordValue]
        sent_value[sent[:50]] = sent_value[sent[:50]] / word_count_in_sentence
    return sent_value


# рез-ти оцінювання
ft = freq_table(text)
s = sent_tokenize(text)
sv = score_sentences(s, ft)
print(sv)


# визначення порогу
def avg_score(sentValue) -> float:
    sumValues = 0
    for entry in sentValue:
        sumValues += sentValue[entry]
    average = sumValues / len(sentValue)
    return average


avg = avg_score(sv)
print(avg * 1.2)  # збільшити поріг на 20%


# генерування реферату
def summary(sentences, sentValue, threshold):
    sentence_count = 0
    summary = ''
    for sent in sentences:
        if sent[:50] in sentValue and sentValue[sent[:50]] > 5:
            summary += " " + sent
            sentence_count += 1
    return summary


summ2 = summary(s, sv, avg)
print(summ2)
