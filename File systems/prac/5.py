words=['donkey', 'fuck', 'stupid', 'dumb']

with open('donkey.txt', 'r') as f:
    content= f.read()
    
for word in words:
    content= content.replace(word, '######')
    with open('donkey.txt', 'w') as f:
        f.write(content)