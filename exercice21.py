from typing import List
from numbers import Number

def validate_numeric_list(lst: List[Number]) -> None:
    
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("Tous les éléments de la liste doivent être des nombres.")

def length(lst: List[Number]) -> int:
    
    return len(lst)

def mean(lst: List[Number]) -> float:
    
    validate_numeric_list(lst)
    return sum(lst) / len(lst)

def range_of_list(lst: List[Number]) -> float:
    
    validate_numeric_list(lst)
    return max(lst) - min(lst)


numbers = [1, 2, 3, 4, 5]
print(length(numbers))  
print(mean(numbers))    
print(range_of_list(numbers))  

