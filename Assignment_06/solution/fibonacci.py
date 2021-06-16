def fib1(n):
  
    if n == 0:
        return 0
            
    elif n == 1:
        return 1
            
    else:
        
        z=fib1(n-1)+fib1(n-2)
        return z

if __name__ == "__main__":        
    n=input("Geben Sie ein n ein")
    m=fib1(int(n))    
    print(m)   