name = 'Міронова Євгенія, 2 група, Лабораторна робота 2'
print(name)

import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import wordnet as wn

for synset in wn.synsets('ace', wn.NOUN):
    print(synset.name()+ ':', synset.definition())

for synset in wn.synsets('base', wn.NOUN):
    print(synset.name()+ ':', synset.definition())

print(wn.synset('ace.n.01').hypernyms())
print(wn.synset('ace.n.02').hypernyms())
print(wn.synset('base.n.01').hypernyms())
print(wn.synset('base.n.02').hypernyms())


print(wn.synset('ace.n.01').hyponyms())
print(wn.synset('ace.n.02').hyponyms())
print(wn.synset('base.n.01').hyponyms())
print(wn.synset('base.n.02').hyponyms())

#найнижчий у ієрархії понять спільний гіперонім
ace = wn.synset('ace.n.01')
base = wn.synset('base.n.01')
print(pear.lowest_common_hypernyms(apple))

#Path Distanse Similarity
print(ace.path_similarity(base))

#W-Palmer Similarity
print(ace.wup_similarity(base))

#Leackock Chodorow Similarity
print(ace.lch_similarity(base))

#Відстань Левенштейна
def levenshtein(s1, s2):
    d = {}
    s1_length = len(s1)
    s2_legth = len(s2)
    for i in range(-1, s1_length + 1):
        d[(i, -1)] = i + 1
    for j in range (-1, s2_legth + 1):
        d[(-1, j)] = j + 1

    for i in range(s1_length):
        for j in range(s2_legth):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i, j)] = min(
                d[(i - 1, j)] + 1, # delete
                d[(i, j - 1)] + 1, # insert
                d[(i - 1, j - 1)] + cost, # subst
            )
    return d[s1_length - 1, s2_legth - 1]
word1 = 'ace'
word2 = 'base'
dl = levenshtein(word1, word2)
print(f"results for '{word1}' & '{word2}':", dl)

#Найближчі слова з словника

from operator import itemgetter

def dict_distance(word, num_words):
    file = open(r'C:\Users\Lenovo\Downloads\chesterton-brown.txt', 'r')
    lines = file.readlines()
    file.close()

    distances = {}
    for line in lines:
        word_distance = levenshtein(word,line.strip())
        distances[line.strip()] = word_distance
    sorted_dict = sorted(distances.items(), key = itemgetter(1))

    closest_words = []
    for i in range(num_words):
        closest_words.append(sorted_dict[i])
    return closest_words

your_word = input("Please, input your word here (the word must be in English): ")
print(your_word,":", dict_distance(your_word, 5))

#2 частина
name = 'Міронова Євгенія, 2 група, Лабораторна робота 2'
print(name)

#your_word = input("Please, input your word here (the word must be in English): ")

import nltk
#nltk.download('wordnet')
from nltk.corpus import wordnet as wn

from collections import Counter

with open(r'C:\Users\Lenovo\Downloads\chesterton-brown.txt', 'r') as f:
    text = f.read()

words = [w.strip('!,.?1234567890-=@#$%^&*()_+') for w in text.split()]
counter = Counter(words)

import sys
sys.stdout = open('chesterton.sorted.txt', "w")
print("\n".join("{} {}".format(*p) for p in counter.most_common()))
sys.stdout.close()

