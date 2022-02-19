lst = list(input("Ввидите списк:"))
print("Ваш список",lst)

input("Перемистить последний элимент списка ")
n = len(lst)
if n != 0:
    lst.insert(0,lst.pop())
    print("Ваш список", lst)
else:
    print("Ваш список", [])