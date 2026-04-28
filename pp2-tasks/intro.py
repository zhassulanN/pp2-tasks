number1 = input()
number2 = input()
operator = int(input())
def calculator(number1, number2):
    if number1 == "ZER":
        number1 = 0
    if number1 == "ONE":
        number1 = 1
    if number1 == "TWO":
        number1 = 2
    if number1 == "THR":
        number1 = 3
    if number1 == "FOU":
        number1 = 4
    if number1 == "FIV":
        number1 = 5
    if number1 == "SIX":
        number1 = 6
    if number1 == "SEV":
        number1 = 7
    if number1 == "EIG":
        number1 = 8
    if number1 == "NIN":
        number1 = 9
    if number2 == "ZER":
        number2 = 0
    if number2 == "ONE":
        number2 = 1
    if number2 == "TWO":
        number2 = 2
    if number2 == "THR":
        number2 = 3
    if number2 == "FOU":
        number2 = 4
    if number2 == "FIV":
        number2 = 5
    if number2 == "SIX":
        number2 = 6
    if number2 == "SEV":
        number2 = 7
    if number2 == "EIG":
        number2 = 8
    if number2 == "NIN":
        number2 = 9

    







# number = int(input())
# def isNumberUsual(number):
#     if number % 2 == 0 and number % 3 == 0 and number % 5 == 0:
#         print("Yes")
#     else:
#         print("No")

# isNumberUsual(number)




















# 610
# n = int(input())

# numbers = list(map(int, input().split()))

# count_truthy = sum(map(bool, numbers))

# print(count_truthy)

# 609
# n = int(input())

# keys = input().split()

# values = input().split()

# dictionary = dict(zip(keys, values))

# query = input().strip()

# print(dictionary.get(query, "Not found"))

# 608
# n = int(input())

# numbers = list(map(int, input().split()))

# unique_sorted = sorted(set(numbers))

# print(" ".join(map(str, unique_sorted)))

# 607
# n = int(input())

# words = input().split()

# longest = max(words, key=len)

# print(longest)

# 606
# n = int(input())

# numbers = list(map(int, input().split()))

# if all(x >= 0 for x in numbers):
#     print("Yes")
# else:
#     print("No")


# 605
# s = input()

# vowels = "aeiouAEIOU"

# if any(ch in vowels for ch in s):
#     print("Yes")
# else:
#     print("No")


# 604
# n = int(input())

# A = list(map(int, input().split()))

# B = list(map(int, input().split()))

# dot_product = sum(a * b for a, b in zip(A, B))

# print(dot_product)

# 603
# n = int(input())

# words = input().split()

# indexed_words = [f"{i}:{word}" for i, word in enumerate(words)]

# print(" ".join(indexed_words))


# 602
# n = int(input())

# numbers = list(map(int, input().split()))

# evens = filter(lambda x: x % 2 == 0, numbers)

# result = len(list(evens))

# print(result)



# 601
# n = int(input())

# numbers = list(map(int, input().split()))

# squares = map(lambda x: x**2, numbers)

# result = sum(squares)

# print(result)






# score = 0
# def add_points(points):
#     global score
#     score = score + points
#     print(f"Added: {points} points. Total: {score}")

# def show_score():
#     print(f"Current score: {score}")

# add_points(2)
# add_points(10)
# show_score()


# counter = 0
# def increment():
#     global counter
#     counter = counter + 1
#     print(f"Counter: {counter}")

# def reset():
#     global counter
#     counter = 0
#     print("Counter reset to 0")

# increment()
# increment()
# increment()
# reset()
# increment()







# def valid_num(number):
#     number = int(input())
#     isValid = True
#     while number > 0:
#         last = number % 10
#         if last % 2 != 0:
#             return False
#         number = number // 10
#     return True
# if valid_num(number):
#     print("Valid")
# else:
#     print("Not Valid")         


        

        


    




# def create_profile(**info):
    
#     for key, value in info.items():
#         print(f"{key} : {value}")

# profile = {}
# n = int(input())
# for i in range(n):
#     key = input(f"{i+1}: ")
#     value = input(f"{i+1}: ")
#     profile[key] = value
# create_profile(**profile) 







# def filter_numbers(filter, *numbers):
#     filteredNums = 0
#     for i in numbers:
#         if i > filter:
#             filteredNums = filteredNums + 1
#     return filteredNums

# filter = int(input())
# numbers = list(map(int, input().split()))

# filteredNums = filter_numbers(filter, *numbers)
# print(filteredNums)



# def count_even(*numbers):
#     evenNumbers = 0
#     for i in numbers:
#         if i % 2 == 0:
#             evenNumbers = evenNumbers + 1
#     return evenNumbers

# numbers = list(map(int, input().split()))

# evenNumbers = count_even(*numbers)
# print(evenNumbers)


# def find_max(*numbers):
#     maxNum = numbers[0]
#     for i in numbers:
#         if i > maxNum:
#             maxNum = i
#     return maxNum
        

# numbers = list(map(int, input().split()))

# maxNum = find_max(*numbers)
# print(maxNum)

# total = 0
# for i in numbers:
#     total = i + total
# return total


# def celcius_to_fahrenheit(celcius):
#     fahrenheit = celcius * 1.8 + 32
#     return fahrenheit

# celcius = float(input())

# fahrenheit = celcius_to_fahrenheit(celcius)
# print(fahrenheit)


# circle.area.claude
# def circle_area(radius, pi):
#     area = pi * radius * radius
#     return area

# radius = int(input())
# pi = 3.14

# area = circle_area(radius, pi)
# print(area)

# rectangle.area.claude
# def rectangle_area(length, width):
#     area = length * width
#     return area

# length = int(input())
# width = int(input())

# area = rectangle_area(length, width)
# print(area)


# def make_sandwich(typeOfBread, *fillings):
#   fillings_str = ", ".join(fillings)
#   print("Making a", typeOfBread, "sandwich with:", fillings_str)

# typeOfBread = input()

# fillings = input()
# fillings_list = fillings.split()

# make_sandwich(typeOfBread, *fillings_list)






# def my_function(greeting, *names):
#   for name in names:
#     print(greeting, name)

# my_function("Hello", "Emil", "Tobias", "Linus")




# import re

# p = input()

# P_escaped = re.escape(P)
# matches = re.findall(P_escaped, S)

# print(len(matches))



# import re

# S = input()
# P = input()

# if re.search(P, S):
#     print("Yes")
# else:
#     print("No")


# 501
# import re

# text = input()

# if re.match("Hello", text):
#     print("Yes")
# else:
#     print("No")





# 421
# import importlib

# # Считываем количество запросов
# q = int(input().strip())

# for _ in range(q):
#     # Считываем путь к модулю и имя атрибута
#     module_path, attr_name = input().strip().split()
    
#     try:
#         # Пытаемся импортировать модуль по его строковому имени
#         # importlib нужен, потому что обычный import не работает со строками
#         module = importlib.import_module(module_path)
        
#         # Проверяем, есть ли такой атрибут в модуле
#         if not hasattr(module, attr_name):
#             print("ATTRIBUTE_NOT_FOUND")
#         else:
#             # Если атрибут есть, получаем его
#             attr = getattr(module, attr_name)
            
#             # Проверяем, можно ли его "вызвать" (является ли он функцией/классом)
#             if callable(attr):
#                 print("CALLABLE")
#             else:
#                 # Если вызвать нельзя (например, это просто число или строка)
#                 print("VALUE")
                
#     except ImportError:
#         # Если при импорте произошла ошибка (модуль не найден)
#         print("MODULE_NOT_FOUND")



# 415
# from datetime import datetime, timezone
# import math

# def parse_date_tz(line):
#     """Разбирает строку с датой и часовым поясом"""
#     date_str, tz_str = line.split(' UTC')
#     y, m, d = map(int, date_str.split('-'))
    
#     # Определяем знак часового пояса и высчитываем смещение в секундах
#     sign = 1 if tz_str[0] == '+' else -1
#     hh, mm = map(int, tz_str[1:].split(':'))
#     offset_seconds = sign * (hh * 3600 + mm * 60)
    
#     return y, m, d, offset_seconds

# def get_utc_timestamp(y, m, d, offset_sec):
#     """Получает время в секундах (UTC) для местной полночи"""
#     dt = datetime(y, m, d, tzinfo=timezone.utc)
#     return dt.timestamp() - offset_sec

# def is_leap_year(year):
#     """Проверяет, является ли год високосным"""
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# # Считываем данные
# birth_line = input().strip()
# curr_line = input().strip()

# by, bm, bd, b_off = parse_date_tz(birth_line)
# cy, cm, cd, c_off = parse_date_tz(curr_line)

# # Время "сейчас" в секундах
# curr_ts = get_utc_timestamp(cy, cm, cd, c_off)

# # Ищем день рождения в текущем году
# target_y = cy
# target_d = bd

# # Обработка 29 февраля для невисокосных годов
# if bm == 2 and bd == 29 and not is_leap_year(target_y):
#     target_d = 28

# bday_ts = get_utc_timestamp(target_y, bm, target_d, b_off)

# # Если день рождения в этом году уже прошел, берем следующий год
# if bday_ts < curr_ts:
#     target_y += 1
#     target_d = bd
#     if bm == 2 and bd == 29 and not is_leap_year(target_y):
#         target_d = 28
#     bday_ts = get_utc_timestamp(target_y, bm, target_d, b_off)

# # Считаем разницу в секундах и переводим в дни с округлением вверх
# delta = bday_ts - curr_ts
# days_left = math.ceil(delta / 86400)

# # Выводим результат (не меньше 0)
# print(max(0, days_left))


# 420
# g = 0

# def outer():
#     # Переменная n, локальная для outer, но "nonlocal" для inner
#     n = 0
    
#     def inner(commands):
#         global g    # Говорим Python, что будем менять глобальную g
#         nonlocal n  # Говорим Python, что будем менять n из функции outer
#         l = 0       # Локальная переменная только для inner
        
#         for scope, value in commands:
#             if scope == "global":
#                 g += value
#             elif scope == "nonlocal":
#                 n += value
#             elif scope == "local":
#                 l += value  # Меняется только внутри inner, ни на что не влияет
                
#     # Считываем количество команд
#     m = int(input())
#     commands_list = []
    
#     # Считываем сами команды
#     for _ in range(m):
#         parts = input().split()
#         commands_list.append((parts[0], int(parts[1])))
        
#     # Запускаем внутреннюю функцию для обработки команд
#     inner(commands_list)
    
#     # Выводим финальные значения g и n
#     print(f"{g} {n}")

# # Запускаем программу
# outer()


# 419
# import sys
# import math

# def dist(x1, y1, x2, y2):
#     return math.hypot(x2 - x1, y2 - y1)

# def shortest_path(R, x1, y1, x2, y2):
#     OA = math.hypot(x1, y1)
#     OB = math.hypot(x2, y2)
#     AB = dist(x1, y1, x2, y2)

#     # Check if straight segment intersects circle
#     # Distance from center to segment
#     dx = x2 - x1
#     dy = y2 - y1
#     if AB == 0:
#         return 0.0

#     t = -(x1*dx + y1*dy) / (dx*dx + dy*dy)
#     t = max(0.0, min(1.0, t))
#     px = x1 + t*dx
#     py = y1 + t*dy
#     d_center = math.hypot(px, py)

#     if d_center >= R:
#         return AB

#     # Tangent lengths
#     lenA = math.sqrt(OA*OA - R*R)
#     lenB = math.sqrt(OB*OB - R*R)

#     # Angles
#     angleA = math.acos(R / OA)
#     angleB = math.acos(R / OB)

#     thetaA = math.atan2(y1, x1)
#     thetaB = math.atan2(y2, x2)

#     # Angle between radii
#     dtheta = abs(thetaA - thetaB)
#     dtheta = min(dtheta, 2*math.pi - dtheta)

#     arc_angle = dtheta - angleA - angleB
#     arc_length = R * arc_angle

#     return lenA + lenB + arc_length

# # Input
# R = float(sys.stdin.readline())
# x1, y1 = map(float, sys.stdin.readline().split())
# x2, y2 = map(float, sys.stdin.readline().split())

# result = shortest_path(R, x1, y1, x2, y2)

# print("{:.10f}".format(result))

# 418
# import sys

# x1, y1 = map(float, sys.stdin.readline().split())
# x2, y2 = map(float, sys.stdin.readline().split())

# # Reflect B across Ox
# x2r = x2
# y2r = -y2

# # Parametric line A + t(B' - A)
# dx = x2r - x1
# dy = y2r - y1

# # Find t where y = 0
# # y1 + t * dy = 0  →  t = -y1 / dy
# t = -y1 / dy

# x_reflect = x1 + t * dx
# y_reflect = 0.0

# print("{:.10f} {:.10f}".format(x_reflect, y_reflect))

# 417
# import sys
# import math

# def segment_length_inside_circle(R, x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     length = math.hypot(dx, dy)

#     # If segment is a point
#     if length == 0:
#         return 0.0

#     # Quadratic coefficients
#     a = dx*dx + dy*dy
#     b = 2*(x1*dx + y1*dy)
#     c = x1*x1 + y1*y1 - R*R

#     discriminant = b*b - 4*a*c

#     def inside(x, y):
#         return x*x + y*y <= R*R

#     inside1 = inside(x1, y1)
#     inside2 = inside(x2, y2)

#     if discriminant < 0:
#         if inside1 and inside2:
#             return length
#         else:
#             return 0.0

#     sqrt_d = math.sqrt(discriminant)
#     t1 = (-b - sqrt_d) / (2*a)
#     t2 = (-b + sqrt_d) / (2*a)

#     t_min = min(t1, t2)
#     t_max = max(t1, t2)

#     start = max(0.0, t_min)
#     end = min(1.0, t_max)

#     if inside1:
#         start = 0.0
#     if inside2:
#         end = 1.0

#     if start >= end:
#         return 0.0

#     return length * (end - start)

# # Read input in correct order
# R = float(sys.stdin.readline())
# x1, y1 = map(float, sys.stdin.readline().split())
# x2, y2 = map(float, sys.stdin.readline().split())

# result = segment_length_inside_circle(R, x1, y1, x2, y2)

# print("{:.10f}".format(result))
# 416
# from datetime import datetime, timedelta
# import sys

# def parse_datetime(line):
#     # Format: YYYY-MM-DD HH:MM:SS UTC±HH:MM
#     date_part, time_part, tz_part = line.strip().split()
    
#     dt = datetime.strptime(date_part + " " + time_part, "%Y-%m-%d %H:%M:%S")
    
#     sign = 1 if tz_part[3] == '+' else -1
#     hours, minutes = map(int, tz_part[4:].split(':'))
#     offset = sign * (hours * 3600 + minutes * 60)
    
#     # convert to UTC
#     return dt - timedelta(seconds=offset)

# start_line = sys.stdin.readline().strip()
# end_line = sys.stdin.readline().strip()

# start_utc = parse_datetime(start_line)
# end_utc = parse_datetime(end_line)

# duration = (end_utc - start_utc).total_seconds()

# print(int(duration))



# 415




# 414
# from datetime import datetime, timezone, timedelta

# def parse_datetime(line):
#     # Формат: "2025-01-01 UTC+00:00"
#     parts = line.split()
#     date = parts[0]  # "2025-01-01"
#     tz_str = parts[1]  # "UTC+00:00" или "UTC-05:00"
    
#     # Парсим дату
#     year, month, day = map(int, date.split('-'))
    
#     # Парсим timezone
#     if tz_str.startswith("UTC"):
#         tz_offset = tz_str[3:]  # "+00:00" или "-05:00"
        
#         # Парсим offset
#         sign = 1 if tz_offset[0] == '+' else -1
#         hours, minutes = map(int, tz_offset[1:].split(':'))
        
#         # Создать timezone
#         offset = timedelta(hours=sign * hours, minutes=sign * minutes)
#         tz = timezone(offset)
#     else:
#         tz = timezone.utc
    
#     # Создать datetime (полночь в этом timezone)
#     dt = datetime(year, month, day, 0, 0, 0, tzinfo=tz)
    
#     return dt

# # Считать две даты
# dt1 = parse_datetime(input())
# dt2 = parse_datetime(input())

# # Вычислить разницу
# diff = abs((dt2 - dt1).total_seconds())

# # Перевести в дни
# days = int(diff / 86400)

# print(days)


# 413
# import json
# import re

# def parse_path(path):
#     path = re.sub(r'\[(\d+)\]', r'.\1', path)
#     tokens = path.split('.')
    
#     # Убрать пустые токены!
#     tokens = [t for t in tokens if t]  # ← добавить эту строку!
    
#     result = []
#     for token in tokens:
#         if token.isdigit():
#             result.append(int(token))
#         else:
#             result.append(token)
#     return result

# def resolve_query(data, path):
#     tokens = parse_path(path)
#     current = data
    
#     try:
#         for token in tokens:
#             current = current[token]
#         return (True, current)
#     except (KeyError, IndexError, TypeError):
#         return (False, None)

# data = json.loads(input())
# q = int(input())

# for _ in range(q):
#     query = input()
#     success, result = resolve_query(data, query)
    
#     if success:
#         print(json.dumps(result, separators=(',', ':')))
#     else:
#         print("NOT_FOUND")






# 412
# import json

# def find_differences(obj1, obj2, path=""):
#     differences = []
    
    
#     if isinstance(obj1, dict) and isinstance(obj2, dict):
#         all_keys = set(obj1.keys()) | set(obj2.keys())
        
#         for key in all_keys:
#             new_path = f"{path}.{key}" if path else key
            
#             if key not in obj1:
                
#                 differences.append((new_path, "<missing>", json.dumps(obj2[key], separators=(',', ':'))))
#             elif key not in obj2:
                
#                 differences.append((new_path, json.dumps(obj1[key], separators=(',', ':')), "<missing>"))
#             else:
                
#                 if isinstance(obj1[key], dict) and isinstance(obj2[key], dict):
                    
#                     differences.extend(find_differences(obj1[key], obj2[key], new_path))
#                 elif obj1[key] != obj2[key]:
                    
#                     differences.append((new_path, 
#                                       json.dumps(obj1[key], separators=(',', ':')), 
#                                       json.dumps(obj2[key], separators=(',', ':'))))
#     else:
        
#         if obj1 != obj2:
#             differences.append((path, 
#                               json.dumps(obj1, separators=(',', ':')), 
#                               json.dumps(obj2, separators=(',', ':'))))
    
#     return differences


# obj1 = json.loads(input())
# obj2 = json.loads(input())


# differences = find_differences(obj1, obj2)


# if differences:
   
#     differences.sort(key=lambda x: x[0])
#     for path, old, new in differences:
#         print(f"{path} : {old} -> {new}")
# else:
#     print("No differences")



# 411
# import json

# def apply_patch(source, patch):
   
#     if isinstance(source, dict) and isinstance(patch, dict):
#         result = source.copy()
        
#         for key, value in patch.items():
#             if value is None:  
                
#                 if key in result:
#                     del result[key]
#             elif key in result and isinstance(result[key], dict) and isinstance(value, dict):
                
#                 result[key] = apply_patch(result[key], value)
#             else:
                
#                 result[key] = value
        
#         return result
#     else:
#         return patch


# source = json.loads(input())
# patch = json.loads(input())


# result = apply_patch(source, patch)


# print(json.dumps(result, separators=(',', ':'), sort_keys=True))


# 402
# n = int(input())
# for i in range(0, n + 1, 2):
#     if i < n - 1:
#         print(i, end=",")
#     else:
#         print(i)


# 410
# def cycle_list(lst, k):
#     for _ in range(k):
#         for item in lst:
#             yield item

# lst = input().split()
# k = int(input())

# print(' '.join(cycle_list(lst, k)))



# 409
# def powers_of_two(n):
#     power = 1
#     for i in range(n + 1):
#         yield power
#         power *= 2  

# n = int(input())
# print(' '.join(map(str, powers_of_two(n))))




# 408
# def primes(n):
#     for num in range(2, n + 1):
#         is_prime = True
        
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
        
#         if is_prime:
#             yield num

# n = int(input())
# for prime in primes(n):
#     print(prime)




# 407
# class Reverse:
#     def __init__(self, text):
#         self.text = text
#         self.index = len(text)
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index -= 1
#         return self.text[self.index]

# s = input()
# for char in Reverse(s):
#     print(char, end='')

# 406
# def fibanochi(n):
#     a, b = 0, 1
#     count = 0

#     while count < n:
#         yield a
#         a, b = b, a + b
#         count += 1

# n = int(input())
# print(','.join(map(str, fibanochi(n))))



# 405
# def countdowns(n):
#     for i in range(n, -1, -1):
#         yield i

# n = int(input())

# for countdown in countdowns(n):
#     print(countdown)



# 404
# def squares(a, b):
#     for i in range(a, b+1):
#         yield i**2

# a, b = map(int, input().split())

# for square in squares(a, b):
#     print(square)




# 403
# def checks(n):
#     for i in range(0, n+1):
#         if i % 3 == 0 and i % 4 == 0:
#             yield i

# n = int(input())
# for check in checks(n):
#     print(check)


# 402
# def evenNumbers(n):
#     for i in range(0, n+1):
#         if i % 2 == 0:
#             yield i

# n = int(input())
# print(','.join(map(str, evenNumbers(n)))) 



# 401
# def squares(n):
#     for i in range(1, n+1):
#         yield i**2

# n = int(input())
# for square in squares(n):
#     print(square)



# title = input()
# author = input()
# year = int(input())
# remove_key = input()

# item = {
#     "title": title,
#     "author": author,
#     "year": year 
# }

# item.pop(remove_key, None)

# for key, value in item.items():
#     print(f"{key}: {value}")







# product = input()
# price = int(input())
# search_key = input()

# item = {
#     "product": product,
#     "price": price
# }

# if search_key in item:
#     print(item[search_key])
# else:
#     print("Key not found")

# name = input()
# age = int(input())
# city = input()

# person = {
#     "name": name,
#     "age": age,
#     "city": city
# }

# print("Name:", person["name"])
# print("Age:", person["age"])
# print("City:", person["city"])


# text = input()

# count = {}

# for char in text:
#     if char in count:
#         count[char] += 1
#     else:
#         count[char] = 1

# for char, frequency in count.items():
#     print(char, frequency)



# n = int(input())
# list1 = list(map(int, input().split()))

# m = int(input())
# list2 = list(map(int, input().split()))


# set1 = set(list1)
# set2 = set(list2)

# result = set1 - set2

# print(result)




# n = int(input())
# list1 = list(map(int, input().split()))

# m = int((input()))
# list2 = list(map(int, input().split()))

# b = int(input())
# list3 = list(map(int, input().split()))

# set1 = set(list1)
# set2 = set(list2)
# set3 = set(list3)

# result = set1 & set2 & set3

# print(len(result))





# n = int(input())
# list1 = list(map(int, input().split()))

# m = int(input())
# list2 = list(map(int, input().split()))

# set1 = set(list1)
# set2 = set(list2)

# if set1.issubset(set2):
#     print("YES")
# else:
#     print("NO")



# n = int(input())
# list1 = list(map(int, input().split()))

# m = int(input())
# list2 = list(map(int, input().split()))

# set1 = set(list1)
# set2 = set(list2)

# result = set1 ^ set2
# print(result)





# n = int(input())
# pairs = []  

# for i in range(n):
#     a, b = map(int, input().split())
#     new_pair = (b, a)
#     pairs.append(new_pair)  

# for pair in pairs:  
#     print(pair[0], pair[1])



# n = int(input())

# pairs = []

# for i in range(n):
#     a, b = map(int, input().split())
#     pair = (a, b)
#     pairs.append(pair)

# pairs.sort(reverse = True)
# print(pairs)


# x1, y1 = map(int, input().split())
# x2, y2 = map(int, input().split())

# firstStep = (x2 - x1) ** 2
# secondStep = (y2 - y1) ** 2

# thirdStep = firstStep + secondStep
# fourthStep = thirdStep ** 0.5

# print(round(fourthStep, 2))




# n1 = int(input())
# numbers1 = list(map(int, input().split()))

# n2 = int(input())
# numbers2 = list(map(int, input().split()))

# result = []

# if num in numbers2 and num not in result:
#     result.append(num)


# n = int(input())
# numbers = list(map(int, input().split()))

# result = []

# for num in numbers:
#     if num in result:
#         continue
#     else:
#         result.append(num)
# print(*result)


# claude
# n = int(input())
# numbers = list(map(int, input().split()))

# first = numbers.pop(0)

# numbers.append(first)

# print(*numbers)


# claude
# n = int(input())
# numbers1 = list(map(int, input().split()))
# numbers2 = list(map(int, input().split()))

# result = []

# for i in range(n):
#     total = numbers1[i] + numbers2[i]
#     result.append(total)

# print(*result)


# claude
# n = int(input())
# numbers = list(map(int, input().split()))
# sumEven = 0

# for num in numbers:
#     if num % 2 == 0:
#         sumEven += num

# print(sumEven)





# claude
# n = int(input())
# numbers = list(map(int, input().split()))
# k = int(input())

# result = numbers.count(k)

# print(result)


# claude
# n = int(input())
# numbers = list(map(int, input().split()))

# numbers.reverse()
# print(*numbers)



# claude
# n = int(input())
# numbers = list(map(int, input().split()))

# result = []

# for num in numbers:
#     if num in result:
#         continue
#     else:
#         result.append(num)
# print(*result)



# claude
# n = int(input())
# numbers = list(map(int, input().split()))

# numbers.sort()
# print(numbers[-2])

# 302




# 301
# def is_valid(n):
#     for digit_char in n:
#         digit = int(digit_char)
#         if digit % 2 != 0:
#             return False
#     return True

# n = input()

# if is_valid(n):
#     print("Valid")
# else:
#     print("Not valid")


# 220
# n = int(input())
# document = {}

# for _ in range(n):
#     command = input().split()
    
#     if command[0] == "set":
#         key = command[1]
#         value = command[2]
#         document[key] = value
#     elif command[0] == "get":
#         key = command[1]
#         if key in document:
#             print(document[key])
#         else:
#             print(f"KE: no key {key} found in the document")



# 219
# n = int(input())
# episodes = {}

# for _ in range(n):
#     dorama, count = input().split()
#     count = int(count)
#     if dorama not in episodes:
#         episodes[dorama] = 0
#     episodes[dorama] += count

# # Сортируем по названию дорамы
# for dorama in sorted(episodes):
#     print(dorama, episodes[dorama])



# 218
# n = int(input())
# arr = [input().strip() for _ in range(n)]

# first_occurrence = {}

# for i, s in enumerate(arr):
#     if s not in first_occurrence:
#         first_occurrence[s] = i + 1  # индексация с 1

# for s in sorted(first_occurrence):
#     print(s, first_occurrence[s])


# 217
# n = int(input())
# numbers = [input().strip() for _ in range(n)]

# freq = {}

# for num in numbers:
#     freq[num] = freq.get(num, 0) + 1

# count = 0
# for v in freq.values():
#     if v == 3:
#         count += 1

# print(count)



# 216
# n = int(input())
# arr = list(map(int, input().split()))

# seen = set()

# for x in arr:
#     if x in seen:
#         print("NO")
#     else:
#         print("YES")
#         seen.add(x)


# 215
# n = int(input())
# surnames = set()

# for _ in range(n):
#     surnames.add(input().strip())

# print(len(surnames))


# 214
# n = int(input())
# arr = list(map(int, input().split()))

# freq = {}

# for x in arr:
#     freq[x] = freq.get(x, 0) + 1

# max_freq = max(freq.values())

# candidates = [k for k, v in freq.items() if v == max_freq]

# print(min(candidates))



# 213
# x = int(input())

# if x < 2:
#     print("NO")
# else:
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             print("NO")
#             break
#     else:
#         print("YES")




# 212
# n = int(input())
# arr = list(map(int, input().split()))

# for x in arr:
#     print(x * x, end=" ")



# 211
# n, l, r = map(int, input().split())
# arr = list(map(int, input().split()))

# l -= 1
# r -= 1

# arr[l:r+1] = arr[l:r+1][::-1]

# print(*arr)





# 210
# n = int(input())
# arr = list(map(int, input().split()))

# arr.sort()
# arr.reverse()

# print(*arr)



# 209
# n = int(input())
# arr = list(map(int, input().split()))

# mn = min(arr)
# mx = max(arr)

# for i in range(n):
#     if arr[i] == mx:
#         arr[i] = mn

# print(*arr)




# 208
# N = int(input())

# power = 1
# while power <= N:
#     print(power, end=" ")
#     power *= 2


# 207
# n = int(input())
# numbers = list(map(int, input().split()))

# biggestPos = 0
# biggestValue = numbers[0]

# for index, value in enumerate(numbers):
#     if value > biggestValue:
#         biggestPos = index
#         biggestValue = value

# print(biggestPos + 1)




# 206
# n = int(input())
# numbers = list(map(int, input().split()))
# biggestNum = numbers[0]
# for i in numbers:
#     if i >= biggestNum:
#         biggestNum = i
# print(biggestNum)


# 205
# n = int(input())
# is_power = True  

# while n > 1:
#     if n % 2 == 0:
#         n = n // 2  
#     else:
#         is_power = False  
#         break

# if is_power:
#     print("YES")
# else:
#     print("NO")



# 204
# n = int(input())
# numbers = list(map(int, input().split()))
# amount = 0
# for num in numbers:
#     if num > 0:
#         amount = amount + 1
    

# print(amount)

# defence
# num = int(input())
# overall = 0
# for i in range(1, 11):
#     overall = num * i
# print(num)


# 203
# n = int(input())
# numbers = list(map(int, input().split()))
# sum = 0
# for num in numbers:
#     sum = sum + num

# print(sum)


# 202
# n = int(input())
# sum = 0
# for i in range(1, n+1):
#     sum = sum + i
# print(sum)

)
# 201
# year = int(input())
# if year % 400 == 0:
#     print("YES")
# elif year % 100 == 0:
#     print("NO")
# elif year % 4 == 0:
#     print("YES")
# else:
#     print("NO")
        




# 120
# a = int(input())
# b = int(input())

# if a == b:  
#     print("equal")
# elif a > b:  
#     print(a)
# else:  
#     print(b)


# 119
# sentence = input()
# target = input()
# replacement = input()

# result = sentence.replace(target, replacement)

# print(result)


# 118
# n = int(input())  

# if n % 2 == 0:
#     print("even")
# else:
#     print("odd")

# 117
# long_string = input()
# short_string = input()

# result = short_string in long_string 

# print(result)


# name = input()
# age = int(input())
# print(f"Hello, {name}. You are {age} years old.")



# 116
# a = input()
# b = input()

# print(b, a)


# 115
# a = input()
# b = input()

# print(a+b)

# 114
# name = input()
# age = int(input())



# 113
# a = input()
# s = a[::-1]
# print(s)

# 112
# a = input()
# string = a[2:5]
# print(string)


# 111
# a = input()
# first = a[0]
# last = a[-1]

# print(first + " " + last)


# 110
# a = input()
# upper = a.upper()
# lower = a.lower()
# print(upper)
# print(lower)


# 109
# a = input()
# lenght = len(a)
# print(lenght)


# 108
# a = input()
# num1 = int(input())

# print(a*num1)



# 107
# a = int(input())
# b = int(input())

# result = a % b

# print(result)


# 106
# num1 = int(input())
# num2 = int(input())

# result = num1 ** num2

# print(result)


# 105
# num1 = int(input())
# num2 = int(input())

# result1 = num1 // num2 
# result2 = num1 / num2
# print(result1)
# print(result2)


# 104
# num1 = int(input())
# num2 = int(input())

# print(num1 + num2)


# 103
# a = input().isdigit()

# if a == True:
#     print("int")
# elif a == False:
#     print("str")

# 102
# a = input()
# b = input()

# print(a, b, sep="***")



# 101
# name = input()
# y = "Hello, "
# a = "!"

# print(y + name + a)