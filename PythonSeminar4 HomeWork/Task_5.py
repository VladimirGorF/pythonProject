# Сделать локальный чат-бот с JSON хранилищем на основе приложенного буткемпа. Тема чат-бота любая.
# Просьба - постараться не использовать простой одномерный список или простой одномерный словарь.
#
from random import *
import json
hobbies = []

def save():
    with open("hobbies.json", "w", encoding="utf-8") as ho:
        ho.write(json.dumps(hobbies, ensure_ascii=False))
    print('Our hobbies was successfully saved in our library: "hobbies.json"')

def load():
    with open("hobbies.json", "r", encoding="utf-8") as ho:
        hobbies = json.load(ho)
        print('hobbies was successfully loaded!')

try:
    with open("hobbies.json", "r", encoding="utf-8") as ho:
        hobbies = json.load(ho)
        print('hobbies was successfully loaded!')
except:
    hobbies = [["Matrix", "Solyaris", "Lord of Rings", "Texass benzopila", "Santa Barbara", "Knock to the sky"],
     ["Bryus Yillis", "Jenifer Aniston", "Micle Duglas", "SheronStone"], ["BMW", "Mercedes", "Porsche", "Toyota"]]

while True:
    command = input('Please input a command ')
    if command == "/start":
        print('Film-Bot is starting')
    elif command =="/stop":
        save()
        print("Bot was stopped. Wellcome again!")
        break
    elif command == "/all":
        print('This is current list of hobbies: ')
        for i in hobbies:
            print(i)
    elif command == "/films":
        print('This is current list of films: ')
        print(hobbies[0])
    elif command == "/actors":
        print('This is current list of actors: ')
        print(hobbies[1])
    elif command == "/cars":
        print('This is current list of cars: ')
        print(hobbies[2])

    elif command == '/add film':
        f = input('Please input the name of a film ')
        if f in hobbies[0]:
            print('This film already added to films!')
        else:
            hobbies[0].append(f)
            print('Film was added successfully')

    elif command == '/add actor':
        f = input('Please input the name of a actor ')
        if f in hobbies[1]:
            print('This actor already added to actors!')
        else:
            hobbies[1].append(f)
            print('Actor was added successfully')

    elif command == '/add car':
        f = input('Please input the name of a car ')
        if f in hobbies[2]:
            print('This car already added to cars!')
        else:
            hobbies[2].append(f)
            print('Car was added successfully')

    elif command == '/help':
        print('Here is manual')

    elif command == '/delete film':
        f = input('Please input the name of a film ')
        try:
            hobbies[0].remove(f)
            print('film was deleted!')
        except:
            print('This film is absent in our library!')

    elif command == '/delete actor':
        f = input('Please input the name of a actor ')
        try:
            hobbies[1].remove(f)
            print('actor was deleted!')
        except:
            print('This actor is absent in our library!')

    elif command == '/delete car':
        f = input('Please input the name of a car ')
        try:
            hobbies[2].remove(f)
            print('car was deleted!')
        except:
            print('This hobbies is absent in our library!')

    elif command == '/random':
        print('Random choice shows you hobbies - ' + choice(hobbies))
    elif command == '/save':
        save()
    elif command == '/load':
        load()
    else:
        print('Unknown command. Please use manual  /help')





