
string = str(input('Введите строку: ')) #приглашение для ввода
ru_vowels = "АаЕеЁёИиОоУуЫыЭэЮюЯя"   #переменная для русских гласных букв
eng_vowels= "AaEeIiOoUuYy" #переменная для английских русских букв
count = 0 #начало счётчика
for i in string:   #перебираем элементы в string
    for l in  ru_vowels:  #перебираем элементы в ru_vowels
        if l in i:   #если элементы в ru_vowels есть в элементах string
            count +=1  #увеличиваем счётчик на один
    for b in eng_vowels:  #перебираем элементы в eng_vowels
        if b in i:  #если элементы в eng_vowels есть в элементах string
            count +=1  #увеличиваем счётчик на один
print('Количество гласных: ', count)  #выводим счётчик