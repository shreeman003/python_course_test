#study of functions

#1.write a function to check the number is odd or even and display

# def check(num):
#     if(num%2==0):
#         print(num ,"is even")
        
#     print(num ,"is odd")
# x=input("enter the number")
# check(int(x));    



#2.x args
# def multiply(*numbers):
#     res=1
#     for num in numbers:
#         res=num*res
#     return res

# print(multiply(1,2,3,4,5))

#data structures
#lists
#1 accessing items in list
# letters=["a","b","c"]
# print(letters[0])   #accesing via index
# letters[0]="A"

# #2
# letter=list(range(10))
# print(letter[0:3])     # accesing via slicing
# print(letter[0:])      # accesing via slicing
# print(letter[:])       # accesing via slicing
# print(letter[::2])     # accesing via slicing by 2 steps
# print(letter[::-1])    # reverse the list


# #3 List unpacling
# number=list(range(10))
# first,second ,*other,last =number
# print("The first number is",first)
# print("The second number is",second)
# print("The last number is",last)

# #4 loops over list
# letters=["a","b","c"]
# for letter in enumerate(letters):
#     print (letter)  


#  #5 adding or removing item in a list
# letters=["a","b","c"]
# letters.append("d")
# letters.insert(0,"5")
# #removing item in a list
# letters.pop(1)
# letters.remove("c")
# print(letters)
# del(letters[0:2])
# print("after deleting",letters)
# letters.clear()   #clear entire list

# #Finding element in list
# lst=["a","c","b","b","a","e"]
# print("count of a in the list is:",lst.count("a"))
# if "a" in lst:
#     print(lst.index("a"))


#6 sorting list using lambda 
item1=[("product 1",50),
    ("product 2",10),
    ("product 3",20)]

item1.sort(key=lambda items:items[1])
print(item1)

# mapping get the price of each itemr
item2=[("product 1",50),
    ("product 2",10),
    ("product 3",20)]
prices=list(map(lambda item:item[1],item2))
print("the prices of item2 are:",prices)

#Filtering item based on the cost and display the item which is greater than or equal to 20
item3=[("product 1",50),
    ("product 2",10),
    ("product 3",20)]
filteed_lst=list(filter(lambda item:item[1]>=20,item3))
print("The item which is greater than or equal to 20 are:",filteed_lst)
