# Необходимо создать функцию wite_words(word_count, file_name), где word_count
# - количество записываемых слов, file_name - название файла,
# куда будут записываться слова.
# Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>"
# в соответствующий файл с прерыванием после записи каждого на 0.1 секунду.
# Сделать паузу можно при помощи функции sleep из модуля time, предварительно
# импортировав её: from time import sleep.
# В конце работы функции вывести строку "Завершилась запись в файл <название файла>".
# После создания файла вызовите 4 раза функцию wite_words, передав в неё
# следующие значения:
# 10, example1.txt
# 30, example2.txt
# 200, example3.txt
# 100, example4.txt
# После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
# 10, example5.txt
# 30, example6.txt
# 200, example7.txt
# 100, example8.txt
# Запустите эти потоки методом start не забыв, сделать остановку основного потока
# при помощи join.
# Также измерьте время затраченное на выполнение функций и потоков.


import time
import threading
from time import sleep


# Определение функции write_words
def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)  # Пауза в 0.1 секунды после записи каждого слова
    print(f"Завершилась запись в файл {file_name}")


# Взятие текущего времени
start_time = time.time()

# Вызов функции write_words
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Взятие текущего времени после выполнения функций
stop_time = time.time()
time_rez = stop_time - start_time

# Вывод разницы начала и конца работы функcций
print('Время выполнения потоков:', time_rez, 'cекунд')


# Взятие текущего времени перед запуском потоков
start_thread_time = time.time()

# Создание и запуск потоков
threads = []
thread_args = [
    (10, 'example5.txt'),
    (30, 'example6.txt'),
    (200, 'example7.txt'),
    (100, 'example8.txt')
]

for args in thread_args:
    thread = threading.Thread(target=write_words, args=args)
    threads.append(thread)
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

# Взятие текущего времени после завершения потоков
end_thread_time = time.time()
time_thread_rez = end_thread_time - start_thread_time
# Вывод разницы начала и конца работы потоков
print('Время выполнения потоков:', time_thread_rez, 'cекунд')
