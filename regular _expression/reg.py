import re
print(re.search('[abc]','bby'))
res=re.sub('[abc]','o','boy')
print(res)

def plural(noun):
    if re.search('[sxz]$', noun):
        return re.sub('$', 'es', noun) 
    elif re.search('[^aeioudgkprt]h$', noun):
        return re.sub('$', 'es', noun) 
    elif re.search('[^aeiou]y$', noun):
        return re.sub('y$', 'ies', noun)
    else:
        return noun + 's'
print(plural('slient'))
print(re.sub('([^aeiou])y$',r'\1ies','vacancy'))