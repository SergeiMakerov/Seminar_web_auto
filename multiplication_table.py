for i in range(2, 10):
    for j in range(2, 11):
        for k in range(i, i + 4):
            print(f'{k:>3} *{j:>3} ={k * j:>3}', end='\t')
        print()
    print()
