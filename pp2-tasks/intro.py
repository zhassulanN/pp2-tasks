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