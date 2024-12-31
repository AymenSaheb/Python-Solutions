
def get_positive_integer():
    while True:
        
            N = int(input("Please enter a positive integer: "))
            
            if N <= 0:
                print("The number must be positive. Please try again.")
            else:
                return N
        
N = get_positive_integer()


for i in range(-N, N + 1):
    if i != 0:
        print(i)
