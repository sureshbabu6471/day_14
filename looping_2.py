# '''
# *				
# *				
# *				
# *				
# *	*	*	*	*
# '''


for row in range(5):
    for col in range(5):
        if col==0 or row==4:
           print("*",end=" ")
        else:
            print('',end=" ")
    print()
print()
print()
# for row in range(5):
#     for col in range(5):
      
#       if row==0 or col==4:
#         print("*",end=" ")
#     else:
#         print('',end=" ")
#         print()
    


# # find out the comman size list element then find fine out the difference btw two list sum? 
# l=[[1,2,3,4],[5,6,7,8],[9,10],[11,12,13,14,5]]

# a=len(l[0]) #0
# b=len(l[1]) #1
# c=len(l[2]) #2
# d=len(l[3]) #3
# sum=0
# if a==b and a==c and a==d:
#     for x in range(a):
#         sum=sum+l[0][x]
# elif b=c and b=d:

# l=[[1,2,3,4],[5,6,7,8],[9,"s"],[11,12,13,14,5]]
# a=len(l[0]) #0
# b=len(l[1]) #1
# c=len(l[2]) #2
# d=len(l[3]) #3
# sum=0
# sum_1=0
# if a==b or a==c or a==d:
#     if a==b:
#         for x in range(a):
#             sum=l[0][x]+sum_1
#     print("different two comman list is:",sum-sum_1)
#     if b==a or b==c or b==d:
#         for x in range(a):
#             sum=l[0][x]+sum_1
#     print("different two comman list is:",sum-sum_1)

# sum=0
# sum_1=0
# if a==b or a==c or a==d:
#     for x in range(a):
#         sum=sum+l[0][x]+sum_1
#     print("different two comman list is:",sum -sum_1)
# elif b==c or b==d:
#    for x in range(b):
#         sum=sum+l[1][x]+sum_1
#         print("different two comman list is:",sum-sum_1)
# elif c==a or c==b or c==d:
#     for x in range(c):
#         sum=sum+l[2][x]+sum_1
#     print("different two comman list is:",sum-sum_1)
# else:
#     for x in range(d):
#         sum=sum+l[3][x]+sum_1
#     print("different two comman list is:",sum-sum_1)
# print(sum)

