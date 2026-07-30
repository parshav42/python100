# # #Write a program which will find all such numbers which are
# # # divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
# # # The numbers obtained should be printed in a comma-separated sequence on a single line.
# #
# # #Hints: Consider use range(#begin, #end) method
# # '''l = []
# # for i in range(2000,3000):
# #     if i % 7 == 0 and i % 5 != 0:
# #         l.append(str(i))
# #
# # print(','.join(l))'''
# #
# #
# #
# # #Square of a number
# # '''
# # user = int(input("Enter numbers\n"))
# #
# #
# # print(f"squire of number{user} is \n",user * user)
# # '''
# #
# # # Cube of a number
# #
# # '''user = int(input("Enter numbers\n"))
# #
# #
# # print(f"squire of number{user} is \n",user * user* user)'''
# #
# # #Sum of two numbers
# # '''user = int(input("Enter numbers\n"))
# # user1 = int(input("Enter numbers\n"))
# #
# # print(f"sum of {user} & {user1} is ", user + user1)'''
# #
# # #Difference of two numbers
# # '''user = int(input("Enter numbers\n"))
# # user1 = int(input("Enter numbers\n"))
# #
# # print(f"sum of {user} & {user1} is ",-( user - user1))'''
# #
# #
# # #Check positive, negative, or zero
# #
# # '''user1 = int(input("Enter numbers\n"))
# #
# # if user1 < 0:
# #     print("negative number")
# # elif user1 > 0:
# #     print("positive number")
# # else:
# #     print("zero")'''
# #
# # #Find the largest of two numbers
# #
# # '''user1 = int(input("Enter numbers\n"))
# # user = int(input("Enter numbers\n"))
# #
# # if user1 < user:
# #     print(f"{user}")
# # else:
# #     print(f"{user1} ")'''
# #
# #
# # #vFind the largest of three numbers
# #
# # def count(fanc):
# #
# #     count = 0
# #
# #     def wrapper():
# #         nonlocal count
# #         count += 1
# #         print(count)
# #         fanc()
# #     return wrapper
# #
# # @count
# # def hey():
# #     print("hello parshav")
# #
# #
# # hey()
# # hey()
# # hey()
# # hey()
# # hey()
# # hey()
#
def fun():
    n = int(input("enter number you want until table"))

    for i in range(1, 11):
        for p in range(1,n+1,1):
            print(p * i , end='\t')
        print()






p = fun()
