def somar(num1,num2):
    print (num1 + num2)
def subtrair(num1,  num2):
    return num1-num2
def imprime(**kwargs):
    for key, value in kwargs.items():
        print( "%s = %s" %(key,value))
