# ////////////////////////////////
# try:
#     number = int(input('Enter a Number: '))
#     print(number)
# except:
#     print('Invalid Input')

# ////////////////////////////////
try: 
    result = 10/0 
    number = int(input('Enter a Number: '))
    print(number)
except ZeroDivisionError as err:
    print(err)

except ValueError as err:
    print(err)