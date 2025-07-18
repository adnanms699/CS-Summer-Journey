def sum(*nums):
    total = 0
    for num in nums:
        total += num
    return total
nums = (1, 2, 3, 4, 5)
total = sum(*nums)  # Unpacking the tuple
print(total)  # This will print: 15

# # can use many arguments

def display(person,*args, status = "married", **kwargs): #order mattters 
    print(f"The person name is {person}")
    print(f"The status is {status}")
    print(f"the args are {args}")
    print(f"the others are {kwargs}")

display("Adnan", 1,2,3,4,5,6,7, "purple", age = 30,case = "true")

def twice(val , lst=None):
    if lst is None:
        lst = []
    lst.append(val)
    lst.append(val)
    lst.append(val)
    lst.append(val)
    return lst
print(twice(0, [1, 2, 3]))  


