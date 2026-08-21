# Arrays using Arrays...

import array as arr

a=arr.array('i',[1,2,3,4,5])

print("The Original Array is: ",a)

a.append(50)
print("After appending array is: ",a)

removed_element=a.pop()
print(f"Removing last element: {removed_element}")
print("Array after removing last element: ",a)