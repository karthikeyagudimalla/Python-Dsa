# list as an array

#creating an array
arr=[10,20,60,40]
for i in arr:
    print(i)
print("\n")
#adding an element at the end
arr.append(50)
print("arr[5] is",arr[4])
print("\n")
#inserting an element at a particular position: arr.insert(position,value)
arr.insert(2,2)
for i in arr:
    print(i)
print("\n")
#removing an element from the end
arr.pop()
for i in arr:
    print(i)
print("\n")
#removing a particular value from an array
arr.remove(2)
for i in arr:
    print(i)
print("\n")
#sorting the array in ascending order
arr.sort()
for i in arr:
    print(i)