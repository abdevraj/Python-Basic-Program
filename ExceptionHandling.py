a=5
b=2

try:
    print('Recource Open')
    print(a/b)

    k=int(input('Enter a Number \n'))
    print(k)

except ValueError as e:
    print('Invalid Input',e)
    
except ZeroDivisionError as e:
    print('Hey, You Cannot divide a Number by zero',e)

except Exception as e:
    print("Somting went wrong !", e)
    
    
finally:
    print('Recource Closed')