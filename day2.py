DAY2;
*VARABLES

--swapping of variables
a=7
b=5

#eg:1
 temp=a
 b=a
 # a=5,b=7
 print(a,b)
 
#eg:2
 # a=a+b #a=12
 # b=a-b #b=12-7=5
 # a=a-b #a=12-5=7
 # print(a,b)


 
 # a,b=b,  a # only in python
 # print(a,b)

 
 # a=a*b #a=35/7 =5.0
 # b=a/b #b=35/7 = 7.0
 # print (int(a),int(b))

  # id()--> used to find the memory address of the varabile
  # a=7
  # b=8
  # print(id(a))
  # print(id(b))



  # keywords are reserverd words which provide special meaning to
  # complier or interpretor





  import keyword
  # print(keyword.KWlist)
  # print(len(keyword.KWlist))
  # print(type(keyword.KWlist))



  # to check if the string is keyword or not
  # print (keyword.is keyword("sid")) # false

  # if =8
  # print(if) # error coz if is keyword



  # !----> literals
   # literial is the constant value assigned to a variable
   # variable is considers to be constant when it is defines
   # in caps


   # a=78 # a is variable
   # A=78 # A is constant


   hash() --> it creates a hash value for constant datatypes and
   # provides error for non constant datatypes
   n1=89+7j
   print(hash(n1))
   


   f1 = [7,8,9]
   print(hash(f1)) --> list is non-constant or mutable datatype





#! ----> OPERATORS
   # OPERATORS are symbols which is used to perform various operations
   # ? between 2 or more operands



   # arithmatic
   # assignment
   # logical
   # relational or comparison
   # bitwise
   # identity
   # membership


   # * ------> arithamatic ---> +,-,*,/,%,//,**
   #eg:1
   # a=8
   # b=6
   # c=9
   # print(a+b+c)


   # input ()---> used to get the runtime input
   #n1= input("enter the value:")
   #print(type(n1))



   # a=4
   # b=2
   # print(a/b)# is used to get the quotient value
   # print(a%b) # is used to get the remainder value

   # ! // --> floor devision

   # a=7654332
   # b=19
   # print (a//b)#--->the output will be interger & the output #will be based on the floor value


   # ! bitwise operation ---> &,|,^,~,<<,>>
   a = 7
   b = 4
   print(a&b)





   # 2^4 2^3 2^2 2^1 2^0
   8 4 2 1
   0 1 1 1  #--->7
   0 1 0 0   #--->4 &
# -------------
  # 0 1 0 0
  # 256 128 64 32 16 8 4 2 1
  # 0 0  0 0 0 0 0 0 1 0 0

  # a = 9
  # 0 0 0 0 1 0 0 1 #----> 9
  # 1 1 1 1 0 1 0 1 ---> 10
  # -------------------
  # 1 1 1 1 0 1 1 0 --> - 10

  # 256 128 64 32 16 8 4 2 1
  # 0 0 0 0 0 0 1 0 1 3<<
  #  0 0 0 1 0 1 0 0 0 --->     

  # 107
  # <<,>>
  # print (5<<3)


  #16>4


  # ! logical
  # and ,or,not
  # a=6
  # print (a>3 and a<10)
  # print (a>7 or a<30)
  # print (not(a>8and a<10))

  # identity operator
  # is ,is not
  print (a is b)
  # print (a==b)

  # a =[1,2,3]
  # b=[1,2,3]
  # print(a is not b)

  # ! membership operator
  # in,not in

  # 11 =[7,8,9,0,6,5]
  # num = 55
  # print(num in 11)
  # print (not num in 11)


  # num=678
  # print (8 in num) # error


  # ! conditional statement
  # if,elif,else


  #eg:1
  # ---> c  syntax
  # if (condition){
  #     statement
   #     statement
   #     statement
  #    statement



  # eg1
  # a = 6

  # if a:
  #      print("hello")


  # eg 2
  a = 6
  if a>3
 #  print("yes")
 #  else:
 #  print("no")



  # eg 4:
  # a = 0
  # a = none
  # a = false
  # a=  ""
  # if a:
  #    print("yes")
  #   else:
  # print ("n0")
  
# ex 5:
# a number is even or odd
num=int(input("enter a number"))
if("num%2)==0
   printf(num,"is even")
   else:
       print(num, "is odd")

  









  





































  [












  
   




   

  
  
