n=5
for i in range(1, n+1):
    for j in range(1, n+1): 
        if i<j:
            print(n - i + 1, end = ""); 
        else:
            print(n - j + 1, end = "");
    print();
