print("Міронова Євгенія, 2 група, Лабораторна робота 3")

import nltk
from nltk.corpus import movie_reviews
import random
import pickle

nltk.download('movie_reviews')

doc = [(list(movie_reviews.words(fileid)), category)
for category in movie_reviews.categories()
for fileid in movie_reviews.fileids(category)]
random.shuffle(doc)

#топ20
all_words = []
for w in movie_reviews.words():
  all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
print(all_words.most_common(20))

#к-ть слововживань
print(all_words["digital"])

#к-ть слововживань позитивні/ негативні
pos_words = []
neg_words = []
for f in doc:
    if f[1] == "neg":
        for w in f[0]:
            neg_words.append(w.lower())
    else:
        for w in f[0]:
            pos_words.append(w.lower())
pos_words = nltk.FreqDist(pos_words)
neg_words = nltk.FreqDist(neg_words)
print(pos_words["digital"])
print(neg_words["digital"])

#7 + 8
word_features = list(all_words.keys())[:4600]
def find_features(d):
  words = set(d)
  features = {}
  for w in word_features:
    features[w] = (w  in words)
  return features

found_words = []
for k, v in find_features(movie_reviews.words('pos/cv025_3108.txt')).items():
    if v is True:
        found_words.append(k)
print(found_words)


#9+10+11
featuresets = [(find_features(rev),category)
for (rev, category) in doc]
training_set = featuresets[:1800]
testing_set = featuresets[1800:]

classifier = nltk.NaiveBayesClassifier.train(training_set)
save_classifier = open("naivebayes.pickle", "wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

classifier_f = open("naivebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

print("Naive Bayes Algorithm accuracy percent:",
      (nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(20)


#12

from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import BernoulliNB

BernoulliNB_classifier = SklearnClassifier(BernoulliNB(), sparse=False).train(training_set)
save_classifier = open("BernoulliNB.pickle", "wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()
classifier_fs = open("BernoulliNB.pickle", "rb")
svc_classifier = pickle.load(classifier_fs)
classifier_fs.close()

print("BernoulliNB Algorithm accuracy percent:",
      (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)
