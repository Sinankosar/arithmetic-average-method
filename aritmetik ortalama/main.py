def FirstFactorial(num):
    for a in num:
        if not a.isdigit():
            return False
    num = int(num)
    if 1<=num <= 18 :
        for i in range(1,num):
            num*=i
    elif num ==0:
        num =1



  # code goes here
    return num

# keep this function call here
print(FirstFactorial("0"))