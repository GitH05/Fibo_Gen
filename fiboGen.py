# fibonacci Generator
fib_cache = {} #global dictionary store result

def fibo(value):
    if value in fib_cache:
        return fib_cache[value]
    
    if value == 0:
        val = 0
    elif value < 2:
        val = 1
    else:
        val = fibo(value-1) + fibo(value-2)

    fib_cache[value] = val 
    return val
if __name__=='__main__':
    print('======Fibonacci Series======')
    for i in range(1,11):
        print(f'Fibonacci({i}):{fibo(i)}')