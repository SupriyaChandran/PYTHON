list1=[2,3,5,"program","berry",3]
list2=[77,65,34,23]
print("list 1 elements : ",list1)
print("list 2 elements : ",list2)
print("list operations")
print("----------------------")
print(" 1. Append\n 2.insert\n 3.extend\n 4.remove\n 5.pop\n 6.reverse\n 7.maximum\n 8.minimum\n 9.count\n 10.sorted\n 11.find index\n 12.concatenate two list\n 13.repeatation\n 14.len\n 15.clear\n")

c=int(input("enter your choice : "))

if c==1:
  list1.append("python")
  print("appended an element : ",list1)
elif c==2:
  list1.insert(1,"red")
  print("inserted an element : ",list1)
elif c==3:
  list1.extend(["dog","cat"])
  print("extent : ",list1)
elif c==4:
  list1.remove("berry")
  print("removed an element : ",list1)
elif c==5:
  list1.pop(4)
  print("poped an element : ",list1)
elif c==6:
  list1.reverse()
  print("reversed list order : ",list1)
elif c==7:
  print("maximum value in list2 : ",max(list2))
elif c==8:
  print("minimum value in list2 : ",min(list2))
elif c==9:
  print("count of 3 in list1 : ",list1.count(3))
elif c==10:
  list2.sorted()
  print("sorted list2",list2)
elif c==11:
  print("index of element 5 in list1 : ",list1.index(5))
elif c==12:
  print("concatenation of list1 and list2 : ",list1+list2)
elif c==13:
  print("repetation of list 1 (2time) : ",list1*2);
elif c==14:
  print("length of the list 1 : ",len(list1))
elif c==15:
  print("elements in list1 (cleared) : ",list1.clear())
else: 
  print("invalid number");
