'''
Небольшой код для выборки всех слов в файле с последующим добавление в массив.
Примечание:    файл должен содержать исключительно набор слов, и не содержать пробелов в начале файла и в конце.
'''
inpath = input(r"Input path:    ")
def Readerwords(inpath):
    i = 0
    ii = 1
    first = 0
    second = 1
    last = [0] # 0 - Точка отсчета. Исключает ошибку с неверным индексом.
    mass = []

    file = open(inpath,"r",encoding="ANSI") # откроем файл.
    fileread = (file.read()) # Содержимое.

    while i != len(fileread): # Пока i не равно количеству символов содержимого.
        if fileread[i] == " ": # Если находим пробел.
            last.append(i+1) # Добавляем его айди в список.
        i += 1
    last.append(len(fileread)) # Добавляем кол символов в список с индексом пробелов. Исключает ошибку с неверным индексом.
    while ii != len(last): # Пока ii не равно кол индексов пробела.
        mass.append(fileread[last[first]:(last[second]-1)]) # Добавить в список mass символы от first до second-1. -1 для исключения последнего символа. Им являеться пробел.
        first += 1
        second += 1
        ii += 1
    return mass
print(Readerwords(inpath))
