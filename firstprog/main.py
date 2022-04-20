if __name__ == '__main__':
    
    x = int(input("x:\n"))
    y = int(input("y:\n"))
    z = int(input("z:\n"))
    n = int(input("n:\n"))
    
    list = []
    result = []
    a = 0
    b = 3
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k != n:
                    list.append(i)
                    list.append(j)
                    list.append(k)
                    result.append(list[a:b:1])                  
                    a += 3
                    b += 3
                    print(a,b)
           
    print(result)
   
# lis = [zip(i,j,k) for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n ]
    # print(lis)
