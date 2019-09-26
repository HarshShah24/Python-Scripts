def div42by(divBy):
    try:
        return 42/divBy
    except ZeroDivisionError:
        print('Error Dovide by Zeros')
    
print(div42by(2))
print(div42by(0))
print(div42by(4))
