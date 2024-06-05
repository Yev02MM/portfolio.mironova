# 1Створюємо новий консольний проєкт мовою Python, при запуску вивести власне прізвище, ім’я, групу, 
# номер ЛР. Встановити та імпортувати до проєкту бібліотеки NLTK, ChatterBot (версію 1.0.0 або іншу) та інші 
# допоміжні/службові бібліотеки. 

import nltk
import random
import chatterbot_corpus
import time
import logging
import collections
from collections import defaultdict
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from chatterbot.trainers import ChatterBotCorpusTrainer

time.clock = time.time
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)

collections.Hashable = collections.abc.Hashable
print("Міронова Євгенія, група 2, Лабораторна робота 4")


# 2 Створюємо функцію, яка на вхід приймає текст (змінну рядкового типу), визначає залежності між словами за ланцюгом
# Маркова (для кожного слова – всі слова, які йдуть після нього) та повертає їх як словник (ключ – слово, значення –
# список наступних слів).
def markov_chain(text):
    words = text.split(' ')
    my_dict = defaultdict(list)
    for current_word, next_word in zip(words[0: -1], words[1:]):
        my_dict[current_word].append(next_word)
    my_dict = dict(my_dict)
    return my_dict


# 3 Створюємо функцію генерації тексту, яка на вхід як аргумент приймає створений у минулому завданні словник і число
# слів для генерації, після чого генерує текст заданої довжини з урахуванням залежностей зі словника та виводить його
# в консоль.
def generate_sentence(chain, word_count):
    cur_word = random.choice(list(chain.keys()))
    sentence = cur_word.capitalize()
    for i in range(word_count - 1):
        next_word = random.choice(chain[cur_word])
        sentence += ' ' + next_word
        cur_word = next_word
    sentence += '.'
    return sentence


# 4 Використовуємо розроблені функції, задавши для створення словника текстовий файл за індивідуальним варіантом,
# а для генерації тексту – число слів N.
myfile = open(r"C:\штуки\chesterton-brown.txt", "r")
test_text = myfile.read()
test_dict = markov_chain(test_text)
for word in test_dict:
    print(word, test_dict[word])

print(generate_sentence(test_dict, 15))

# 5 6 Реалізовуємо чат-бота з використанням з використанням бібліотеки ChatterBot за зразком із лекції №9: задаємо
# списки фраз small_talk та math_talk, проводимо навчання бота на цих фразах і перевіряємо його роботу в діалозі,
# також проводимо навчання чат-бота на корпусі мовою за індивідуальним варіантом та аналогічно перевіряємо його
# роботу в діалозі

my_bot = ChatBot(name="Mitten", read_only=True,
                 logic_adapters=["chatterbot.logic.MathematicalEvaluation", "chatterbot.logic.BestMatch"])
small_talk = ["Hallå där!",
              "Hej",
              "Hallå",
              "Hur mår du?",
              "Hur mår du?"
              "Jag är cool",
              "Bra och du?",
              "Alltid cool",
              "Jag är okej",
              "Glad att höra det",
              "Jag mår bra",
              "Glad att höra det",
              "Jag känner mig fantastisk",
              "Utmärkt, kul att höra det",
              "Inte så bra",
              "Jag beklagar",
              "Vad heter du?",
              "Jag är Mitten, ställ mig en matematikfråga, snälla"
              ]

math_talk_1 = ["Berätta för mig Pythagoras sats",
               "a^2 + b^2 = c^2"]
math_talk_2 = ["Vad är formeln för cosinussatsen?",
               "c^2 = a^2 + b^2 - 2*a*b*cos(gamma)"]
math_talk_3 = ["Vilken är diskriminantens formel?",
               "D = b^2 - 4*a*c"]
math_talk_4 = ["Hur låter Newtons tredje lag?",
               "F1,2 = - F2,1"]
list_trainer = ListTrainer(my_bot)
for item in (small_talk, math_talk_1, math_talk_2, math_talk_3, math_talk_4):
    list_trainer.train(item)
corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train("chatterbot.corpus.swedish")

print("Hallå! Mitt namn är Mitten.")
for i in range(5):
    user_input = input()
    print(my_bot.get_response(user_input))


