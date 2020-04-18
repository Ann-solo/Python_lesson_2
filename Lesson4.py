# Функция (F)
from random import choices

list_name = ['Ира', 'Саша', 'Лена', 'Василиса', 'Катя', 'Аня', 'Яна', 'Олеся', 'Лиза', 'Авраам', 'Алексей', 'Александр',
             'Петр', 'Сергей', 'Роман', 'Наталья', 'Марина', 'Юля', 'Раиса', 'Татьяна', 'Василиса', 'Самсон', 'Лев',
             'Егор', 'Анастасия', 'Евгений', 'Ольга', 'Александра']


def list_20(list_name, N):
    return choices(list_name, k=N)


name_100=list_20(list_name, N=100)
print(name_100)

def common_name(name_100):
    dict_name={}
    for el in name_100:
        dict_name[el]=dict_name.get(el,0)+1
    dict_name=sorted(list(dict_name.items()),key=lambda x: x[1], reverse=True)
    return dict_name[0][0]

print(common_name(name_100))

def rare_letter(name_100):
    dict_letter={}
    for el in name_100:
        for letter in el[0]:
            dict_letter[letter]=dict_letter.get(letter,0)+1
    dict_letter=sorted(list(dict_letter.items()),key=lambda x: x[1])
    return dict_letter[0][0]

print(rare_letter(name_100))



