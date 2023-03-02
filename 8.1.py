# Телефонный справочник с возможностью создания, изменения и удаления данных.

import json
import datetime
import argparse
from random import randint as rd
from pprint import pprint
import os

# парсим командную строку с помощью argparse
parser = argparse.ArgumentParser(description="Phone book v. 0.1")

parser.add_argument('command', type=str, help='Название команды: add, list, find, update, delete')
parser.add_argument('-n', '--name', type=str, help='Имя')
parser.add_argument('-s', '--surname', type=str, help='Фамилия')
parser.add_argument('-p', '--phone', type=str, help='Номер телефона')
args = parser.parse_args()

# получаем директорию и файл
dirname = os.path.dirname(__file__)

filename = dirname + "\\note.json"

# получаем текущее время и дату и конвертируем в int
dt = datetime.datetime.now()
int_dt = int(dt.strftime("%Y%m%d%H%M%S"))

# добавляет новую запись (add -n name -p phone)
def add(name, surname, phone):
    new_data = {
        "name": name,
        "surname": surname,
        "phone": phone,
        "datetime": int_dt
    }
    new_data = json.dumps(new_data)
    new_data = json.loads(str(new_data))

    with open(filename, encoding = 'utf-8') as file:
        data = json.load(file)
        data['notes'].append(new_data)
        with open(filename, 'w', encoding = 'utf-8') as outfile:
            json.dump(data, outfile, indent = 4)

# измененяет существующую запись по имени (update -n name -p phone)
def update(name, surname, phone):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        index = 0
        for note in data['notes']:
            if note['name'] == str(name):
                note['surname'] = surname
                note['phone'] = phone
                note['datetime'] = int_dt
            elif note['surname'] == str(surname):
                note['name'] = name
                note['phone'] = phone
                note['datetime'] = int_dt 
            else:
                None
            index = index + 1
        with open(filename, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii = False, indent = 4)

# выводит список всех записей, отсортированных по дате добавления (list)
def list():
    with open(filename, 'r', encoding = 'utf-8') as file:
        data = json.load(file)
        new_data = sorted(data['notes'], key=lambda k: k['datetime'], reverse = True)
        pprint(new_data)

# осуществляет поиск записи по имени (find -s surname)
def find(surname):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        index = 0
        for note in data['notes']:
            if note['surname'] == str(surname):
                pprint(data['notes'][index])
            else:
                None
            index = index + 1

# удаляет запись по фамилии (delete -n surname)
def delete(surname):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        index = 0
        for note in data['notes']:
            if note['surname'] == str(surname):
                data['notes'].pop(index)
            else:
                None
            index = index + 1
        with open(filename, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii = False, indent = 4)


if args.command == 'add':
    add(args.name, args.surname, args.phone)
elif args.command == 'update':
    update(args.name, args.surname, args.phone)
elif args.command == 'list':
    list()
elif args.command == 'find':
    find(args.surname)
elif args.command == 'delete':
    delete(args.surname)
else:
    print("Введите корректную команду")