# 0, 1, 1, 2, 3, 5, 8, 13, 21... 

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1 or n ==2:
        return 1
    
    else:
        return fibonacci(n-1) + fibonacci(n-2)

while True:
    userInput = int(input('Enter the value of n: \n'))
    print(fibonacci(userInput))

    userSaysNo = input('Do you want to continue? (yes/no): \n')
    if userSaysNo == 'no' or userSaysNo == 'No' or userSaysNo == 'NO':
        print('OVER')
        break
    elif ( userSaysNo != 'yes'):
        print('OVER')
        break


