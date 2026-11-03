def sum_down(n):
    if n==0:
        return 0
    return n + sum_down(n - 1)

n = int(input("Enter a number: "))
guess = input("What is the sum down(" + str(n) + ")?" )
input("sum down adds n to sum_down(n-1) until it reaches 0, press enter")
print("Sum down(" + str(n) + ") =", sum_down(n),"your guess: ", guess )