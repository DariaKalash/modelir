print("Задание 6")

string = input("Введите строку: ")

palindrome = True
if string[::-1] != string:
    palindrome = False
# for i in range(len(string)//2):
#     if string[1] != string[-i -1]:
#         palindrome = False
#         break
if palindrome:
    print("Строка является палиндромом")
else:
    print("Строка не палиндром")