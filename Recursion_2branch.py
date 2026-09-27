class Fibonacci:
    def __init__(self):
        self.n=int(input("Enter the number of terms: "))
        for i in range(self.n):
            print(self.fibo(i),end=" ")
        

    def fibo(self,num):
        if(num<=1):
            return num
        return self.fibo(num-1)+self.fibo(num-2)

obj=Fibonacci()