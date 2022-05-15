from math import sqrt

print("Коэффициент a:")
a = int(input())
print("Коэффициент b:")
b = int(input())
print("Коэффициент c:")
c = int(input())

d = pow(b, 2) - 4*a*c
result = [0, 0]
if (d < 0):
    print("у уравнения нет решений")
elif (d == 0):
    print(-b / (2 * a))
else:
    root1 = (-b + sqrt(d)) / (2*a)
    root2 = (-b - sqrt(d)) / (2*a)
    print(root1, root2)
