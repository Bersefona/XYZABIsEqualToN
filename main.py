n = 1056
tmpl1, tmpl2 = [], []
final = []
for i in range(71, 100):
    c = i
    if str(i // 10) not in '0156' and str(i % 10) not in '0156':
        tmpl1.append(c)
for i in range(100, 988):
    c = i
    if str(i % 10) in '0156':
        continue
    else:
        i //= 10
        if i > 0:
            if str(i % 10) in '0156':
                continue
            else:
                i //= 10
                if i > 0:
                    if str(i % 10) in '0156':
                        continue
                    else:
                        tmpl1.append(c)                        
for j in range(len(tmpl1)):
    d = tmpl1[j]
    if d < 100:
        if d % 10 != d // 10:
            tmpl2.append(d)
    else:
        d1 = d // 100
        d2 = (d % 100) // 10
        d3 = d % 10
        if d1 == d2 or d2 == d3 or d1 == d3:
            continue
        else:
            tmpl2.append(d)
#print(tmpl2)

for i in range(len(tmpl2)):
    for j in range(len(tmpl2)):
        if tmpl2[i] + tmpl2[j] == n:
            final.append([tmpl2[i], tmpl2[j]])

for i in range(len(final)):
    c = final[i][0]
    b = final[i][1]
    if c < 100:
        d1, d2 = c // 10, c % 10
        a1, a2, a3 = b // 100, (b % 100) // 10, b % 10
        if d1 == a1 or d1 == a2 or d1 == a3 or \
        d2 == a1 or d2 == a2 or d2 == a3:
            continue
        else:
            print(f'{c} + {b} = {c + b}')
    elif b < 100:
        d1, d2 = b // 10, b % 10
        a1, a2, a3 = c // 100, (c % 100) // 10, c % 10
        if d1 == a1 or d1 == a2 or d1 == a3 or \
        d2 == a1 or d2 == a2 or d2 == a3:
            continue
        else:
            print(f'{c} + {b} = {c + b}')
    else:
        a1, a2, a3 = c // 100, (c % 100) // 10, c % 10
        d1, d2, d3 = b // 100, (b % 100) // 10, b % 10
        if d1 == a1 or d1 == a2 or d1 == a3 or \
           d2 == a1 or d2 == a2 or d2 == a3 or \
           d3 == a1 or d3 == a2 or d3 == a3:
            continue
        else:
            print(f'{c} + {b} = {c + b}')
#print(*final, sep = '\n')