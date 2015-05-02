# chart

w= [['124.53']]
w=str(w)
for word in w:
    word=[l.replace("'[","") for l in word]
    word=[l.replace("]'","") for l in word]
print w
