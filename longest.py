def longest(list):
    a=find_path(list,0,0)
    height,path=a
    print(path)

def find_path(list,height,maxi):
    if list != []:
        if list[0]==[] and list[2] == []:
            return height,maxi
        elif list[0] !=[] and list[2] !=[]:
            left_height, left_maxi = find_path(list[0],height,maxi)
            right_height, right_maxi = find_path(list[2],height,maxi)
            height=max(left_height,right_height)+1
            maxi=max(left_height+right_height+2,left_maxi,right_maxi)
            return height, maxi
        elif list[0]==[]:
            right_height, right_maxi = find_path(list[2], height, maxi)
            height=right_height+1
            maxi=max(maxi,right_height+1,right_maxi)
            return height,maxi
        else:
            left_height, left_maxi = find_path(list[0], height, maxi)
            height = left_height + 1
            maxi = max(maxi, left_height + 1,left_maxi)
            return height, maxi
