#1
a = (101 + 0) / 3
print(a)

b = 3.0e-6 * 10000000.1
print(b)

c = True & & True
print(c)

d = False & & True
print(d)

e = (False & & False)(True & & True)
print(e)

f = (False False) & & (True & & True)

# 2
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == b:
    if b == c:
        if c == d:
            print("равно")

else:
    print("не равно")

# 3
spisok = [1, 5, 6, 7, 200, 70, 154, 365]
max1 = max(spisok)
print(max1)

# 4
spisok = [1, 5, 6, 7, 200, 70, 154, 365]
min1 = min(spisok)
print(min1)

# 5
mass = [1, 3, 5, 213, 534, 23, 56, 13 ,4, 5, 65, 43,2 ,234, 25,52, 452, 12,43,242, 3 ,4,23 ]
for i in range(len(mass)):
  if mean(mass) < mass[i]:
    print(mass[i])

# 6
a = int(input())
b = int(input())
rezult = 0
z = 0

while z != (abs(b)):
    rezult = rezult + (abs(a))
    z = z + 1
print(rezult)

# 7
mass = [1, 3, 5, 213, 534, 23, 56, 13 ,4, 5, 65, 43,2 ,234, 25,52, 452, 12,43,242, 3 ,4,23 ]
chet = []
nechet = []
for i in range(8):
  if mass[i] % 2 == 0:
    chet.append(mass[i])
  else:
    nechet.append(mass[i])
print("Четные ", chet[:])
print("Нечетные", nechet[:])

# 8
F = float(input())
C = ((F - 32) * 0.555)
print(C)

# 9
ves = float(input("Вес: "))
rost = float(input("Рост: "))

IMT = ves / rost
print(IMT)

# 10
a = int(input())

print("kvadrat")
a1 = a ** 2
print(a1)
print("kyb")
b1 = a ** 3
print(b1)
print("v chetvertoy")
c1 = a ** 4
print(c1)

# 11
a = int(input("боковая сторона: "))
b = int(input("боковая сторона: "))
c = int(input("гипотенуза: "))
d = int(a + b)

if ((a + b) > c):
    print("NO")
else:
    print("YES")

if (d == c):
    print("YES")