#factorial of a given number
class Factorial:
    def __init__(self):
        n=int(input("Enter the value of n: "))
        ans=self.fact(n)
        print(f"Factorial of {n} is {ans}")
    def fact(self,n):
        if n<=1:
            return 1
        else:
            return n*self.fact(n-1)

obj=Factorial()