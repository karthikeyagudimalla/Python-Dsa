# Arrays using Arrays...

import array as arr

#creating an array
a=arr.array('i',[1,2,3,4,5])

#printing the array we declared
print("The Original Array is: ",a)

#inserting an element at the end of the array
a.append(50)
print("After appending array is: ",a)

#removing an element at specific positon
removed_element=a.pop(1)
print(f"Removing last element: {removed_element}")
print("Array after removing last element: ",a)

#inserting an element at a specific position
a.insert(2,15)
print("adding 5 at positon 2: ",a)

#length of the array
print("The length of the array is ",len(a))