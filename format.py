import codecs

f = codecs.open('data_zte.txt','r','utf-8')
s = f.readlines()
f.close()
target = codecs.open('strip.txt','w','utf-8')
for line in s:
    if '//' not in line:
        if '转发微博' not in line:
            if '分享图片' not in line:
                target.write(line)
target.close()