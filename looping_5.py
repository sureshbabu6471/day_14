# for row in range(5):
#     temt=1
#     for col in range(row+1):
#         print(temt,end=" ")
#         temt+=2
#     print()




# for row in range(0,10,1):
#     temt=1
#     for col in range(row+1):
#         print(temt,end=" ")
#         temt+=temt
#     print()

# for row in range(0,5,1):
#       for col in range(5):
#         if col==1 or row==4:
#           print("*",end=" ")
#       print()
    
    


# temt=0
# for row in range(5):
#     print("*")
#     if row==4:
#          for col in range(7):
#               print("*",end=" ")
#     print()



# for row in range(5):
#      l=row-0
#      for col in range(l):
#           print("*",end=" ")
#      print()

# temp=1
# for row in range(5):
#     for col in range(7):
#         if row==0 or row==4 or col==0 or col==6:
#             print(temp,end="  ")
#         else:
#             print("",end="   ")
#     print()
#     temp=temp+1



# temp=1
# for row in range(5):
#     for col in range(5):
#         if row==0 or row==4 or col==0 or col==4:
#             print(temp,end="  ")
#         else:
#             print("",end="   ")
#     print()
#     temp=temp+2


# for row in range(5):
#     temp=1
#     for col in range(row+1):
#             print(temp,end=" ")
#             temp=temp+2
#     print()
temp=0
for row in range(5):
    for col in range(5):
        if row>=col:
            print("A",end=" ")
        else:
            print("",end="  ")
            temp=temp-1
    print()


# for row in range(5):
#     for col in range(5):
#         if row>col:
#             print(" ",end=" ")
#         else:
#             print("*",end=" ")
#     print()


        
        
    
