from collections import defaultdict
colors=["blue","blue","red","green","red","blue"]
d={}
for color in colors:
    if color not in d:
        d[color]=0
    d[color]+=1
print(d)
d={}
for color in colors:
    d[color]=d.get(color,0)+1
print(d)
d=defaultdict(int)
for color in colors :
    d[color]+=1
print(d)
