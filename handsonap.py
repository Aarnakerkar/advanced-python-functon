list1=[1,2,3]
list2=[4,5,6]
result=map(lambda x,y:x+y,list1,list2)
print(list(result))
list3=[12,13,14]
def square(n):
    return n*n
result2=list(map(square,list3))
print(result2)