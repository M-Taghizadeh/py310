# union => python3.9 => |, |= 
dict1 = {
    1: 'a',
    2: 'b', 
    3: 'c', 
    4: 'in both',
}
dict2 = {
    4: 'but different', 
    5: 'd', 
    6: 'e'
}

print(dict1 | dict2) 
dict1 |= dict2
print(dict1)

######################################################

def square(number: int | float):
    print(type(number))
    return number ** 2

# Instead of 
from typing import Union
def old_square(number: Union[int, float]):
    return number ** 2

print(square(2.2))
print(square(2))