year = int(input("Enter the Year"))
if( ((year % 4 == 0) and (year % 100 != 0)) or (year % 400==0) ):
    print(+year, "Leap Year")
else:
    print(+year, "Not leap Year")


# def fib(n):
#     if n<=1:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)
# n=int(input("Enter the number:"))
# print(fib(n))