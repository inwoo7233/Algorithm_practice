

num = 0
bbo = 0

for i in range(1,1512265) :
    c = str(i);
    l = list(c);
    num = 0;
    for j in l:
        if (j == '3'):
            num = num + 1
    if (i % 10 == 0) :
        print("짝")
    elif (num > 0) :
        bbo = bbo + num

print(bbo)