dict={  "merry":"god", 
        "christmas":"jul",
        "and":"och", 
        "happy":"gott",
        "new":"nytt",
        "year":"år"}
def getstring1(s):
    
    if s in dict:
        return dict.get(s)
    else:
        return s

def translate (s):
    newstring=""
    for i in  s.split(" "):
        newstring=newstring+ getstring1(i)
       
    print(newstring)
inputstring="merry christmas and happy new year"

translate(inputstring)