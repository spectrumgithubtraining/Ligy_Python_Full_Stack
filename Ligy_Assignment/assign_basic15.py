num = int(input("Enter a number: "))
x = 0
t = num

while t > 0:
    d = t % 10
    x += d ** 3
    t //= 10
if num == x:
    print(num,"IS AN ARMSTRONG NUMBER")
else:
   
    print(num,"IS NOT AN ARMSTRONG NUMBER") 