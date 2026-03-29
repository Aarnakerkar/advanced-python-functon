set1={1,2,3,4,5,6}
set2={"a","b","c","d","e","f"}
set3=list(zip(set1,set2))
print(set3)
list1=[1,2,3,4,5,6,7,8]
list2=[11,22,33,44,55,66,77,88]
for x,y in zip (list1,list2[::-1]):
    print(x,y)
