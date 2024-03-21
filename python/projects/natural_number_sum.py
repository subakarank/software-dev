#find a Sum of N natural number

def sum_of_natural_numbers_loop(n: int) -> int:
    sum = 0 
    for i in range(1, n+1):
        sum += i
    return sum


def sum_of_natural_numbers_formula(n: int) -> int:
    sum = n * (n +1)  // 2 
    return sum


input = 10
print(f"Sum of {input} natural number - using loop ", sum_of_natural_numbers_loop(input))

input = 10 
print(f"Sum of {input} natural number - using formula ", sum_of_natural_numbers_formula(input))

