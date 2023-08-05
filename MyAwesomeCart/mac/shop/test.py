int_list=[0,1,2,3,4,5]
ch=0
element=0

while element is int_list[ch]:
    print(element,end="")
    ch=ch+1
    element=int_list[ch+1]
else:
    print(int_list[element])