print("Задание 6")
string = input("Введите строку: ")
palindrome = True
if string[::-1] != string:
    palindrome = False
if palindrome:
    print("Строка является палиндромом")
else:
    print("Строка не палиндром")


n = int(input("Введите число: "))
print("Факториал числа", n, "равен: ", fac(n))