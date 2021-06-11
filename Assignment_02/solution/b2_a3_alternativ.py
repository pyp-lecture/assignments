def sieb_des_eratosthenes(n):
    array = []
    for i in range(2, n+1):
        if i not in array:
            print (i)
            for j in range(i*i, n+1, i):
                array.append(j)

sieb_des_eratosthenes(1000)