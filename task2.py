# расчет количества книг на диске

BYTES_ONE_CHARS = 4
volume = 1.44 #объем дискеты
pages = 100
line = 50
chars = 25

total_chars = pages * line * chars
book_volume = total_chars * BYTES_ONE_CHARS

disk_volume = volume * 1024 * 1024
numbers_book = disk_volume // book_volume
print('Количество книг на дискете:', numbers_book)

# Арифметические операторы и избегание магических чисел
lenght = 90
width = 50
perimetr = lenght + lenght + width + width
print('Периметр футбольного поля:' , perimetr)

# Расчет периметра и площади геометрических фигур
radius = 5
side = 5
pi = 3.1415
print ('Периметр:' , round (perimetr,2))

# Формирование строки из повторяющихся чисел






