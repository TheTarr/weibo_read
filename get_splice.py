lines = open('strip.txt', 'r', encoding='utf-8').readlines()
ml = [' ','。','，','？','！','—','','…','~','\n','：','）']
# '','','','','','','','','','','','','','','','','','','','',''
f = open('spliced.txt', 'w', encoding='utf-8')

for i in lines:
    if i == '\n':
        continue
    h = len(i)
    x = 0
    temp = ''
    while x < h:
        if i[x] in ml:
            temp += i[x]
            print(temp)
            f.write(temp.strip(' ')+'\n')
            temp = ''
            x += 1
        else:
            temp += i[x]
            x += 1
f.close()
lines = open('spliced.txt', 'r', encoding='utf-8').readlines()
f = open('spliced.txt', 'w', encoding='utf-8')
for i in lines:
    if i[0] not in ml and i != '\n':
        f.write(i)
