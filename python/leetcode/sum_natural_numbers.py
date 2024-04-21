# sum of N natural number 
# example if n is 3 then sum =  1 + 2 + 3 
# example if n is 5 then sum = 1 + 2 + 3 + 4 + 5 
def method1(n: int ) -> int:
    sum = 0
    for value in range(1, n+1):
        sum = sum + value
    return sum

def method2(n: int ) -> int: 
    sum = n * (n + 1 ) // 2
    return sum

def method3(n:int) -> int:
    sum = 0
    left, right = 1, n 
    while left <= right:
        sum += left + right
        left = left + 1 
        right = right - 1
    # find the bug and fix it
    return sum 

   
n = 3
sum = method1(n)
print(f"sum of {n} is {sum} - by method1")
sum = method2(n)
print(f"sum of {n} is {sum} - by method2")
sum = method3(n)
print(f"sum of {n} is {sum} - by method3")


