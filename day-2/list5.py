def over(list1,list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True

    return False
list1=[1,2,3,4,5,6]
list2=[6,8,9,10,11]
bool =over(list1,list2)
if(bool==True):
    print("lists are  overlapped")
else:
    print("lists are not overlapped")