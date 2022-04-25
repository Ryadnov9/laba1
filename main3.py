""""За довжинами двох сторін деякого трикутника
і кутом між ними знайти довжину третьої сторони і площу цього трикутника."""
import math
a = int(input(""
              "Enter number : "))
b = int(input("Enter number : "))
y = int(input("Enter number for cut: "))
c = math.sqrt(math.pow(a, 2)+math.pow(b, 2)-2*a*b*math.cos(y))
p = (a+b+c)/2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print("довжинa третьої сторони:", c, ",", "площa:", s)
