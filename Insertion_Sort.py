class Insertion_Sort:
    def __init__(self):
        n=int(input("Enter the number of values: "))
        arr=[]
        print(f"Enter the {n} values: ")
        for i in range(0,n):
            arr.append(int(input()))
        print("Original values are: ")
        for i in arr:
            print(i,end=" ")
        print()
        sorted_arr=self.insertion_sort(arr)
        print("Sorted values: ")
        for i in sorted_arr:
            print(i,end=" ")
        print()

    def insertion_sort(self,arr):
        for i in range(1,len(arr)):
            j=i-1
            while j>=0 and arr[j]>arr[j+1]:
                temp=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp
                j-=1
        return arr

sort=Insertion_Sort()