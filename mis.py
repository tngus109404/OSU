def max_wis(array):
    la=len(array)

    def fff(i,jang={-1:0, 0:0}):
        if i not in jang:
            jang[i] = max((array[i - 1] + fff(i - 2)), fff(i - 1))
        return jang[i]



    i=la
    fff(la)
    mis=[]
    while i>0:
        if fff(i)!=fff(i-1):
            mis.append(array[i - 1])
            i -= 1
        i-=1
    mis.reverse()
    return fff(la), mis

