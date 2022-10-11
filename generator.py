import random

def generate_nonesense(n):
    ml = [' ', '。', '，', '？', '！', '—', '', '…', '~', '\n', '：','）']
    lines = open('spliced.txt', 'r', encoding='utf-8').readlines()
    target = []
    for i in range(0,len(lines)-1):
        target.append(i)
    mstr = ''
    while len(mstr) < n:
        x = random.choice(target)
        mstr += lines[x].strip('\n')
        if mstr[-1] not in ml:
            mstr += '，'
        target.remove(x)
    while mstr[0] in ml:
        mstr=mstr[1:]
    if mstr[-1] == '，':
        print(mstr[:-1] + '！')
    else:
        print(mstr)

n = 100
while n != '-1':
    try:
        n = int(input('生成乱语长度（打-1退出）：'))
    except:
        print('【您打的不是数字吧？先按默认100算了。】')
        n = 100
    generate_nonesense(n)
    print()