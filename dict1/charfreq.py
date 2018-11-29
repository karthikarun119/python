def char_freq(word):
   # chr=word.split('')

    chr=[word[i:i+1] for i in range(0, len(word), 3)]
    print(chr)
    d={}
    for i in chr:
      d[i]=d.get(i,0)+1
    print(d)


char_freq("abbabcbdbabdbdbabababcbcbab")

