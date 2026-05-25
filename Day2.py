'''print(input("Enter Your name: "))
_name= input("Enter your name:")
print('My name is' +" "+ _name)

_sameplelist =['Mani',35,3.14,(3,5),{5,6,7}]
print(id(_sameplelist))
print(type(_sameplelist))
print(type(_sameplelist.index(35)))
#print(_sameplelist.count)
_Employeeids={1,2,3,4,5,6,7,8,8}
print(_Employeeids)
#--------------------------------------
_firstname=input("Enter your Firstname :")
_lastname=input("Enter your Lastname :")
print("My Full Name is:"+""+_firstname+" "+_lastname)
_del=[2,3,5,6]
print()
_int=35
_name='Mani'
_float=3.14
print(_name)
print(_int)
print(type(int(_float)))
print(type(str(_int)))
print(type(_int))
print("*"*1)
print("*"*2)
print("*"*3)
print("*"*4)
print("*"*5)
print("*"*6)
print("*"*7)
_book={"title":"Mylife","author":"Mani","publication year":2026}
print(_book)
print("tittle"+ " "+_book["title"]) 
print("Author"+ " "+_book["author"]) 
print("year"+ " "+str(_book["publication year"])) '''

'''for i in range(5):
    _title=input("Enter book title :  ")
    _author=input("Enter book Author :  ")
    _year=input("Enter book year :  ")
    _book={
    "title":_title,"author":_author,"publication year":_year
    }

print(_book)

_String1=input("Enter your age :")
print(type(_String1))
print(float(_String1))
_String1=input("Enter your age :")
print(type(_String1))
print((int(_String1))+5)'''

_firstnumber=int(input("Enter your firstnumber :"))
_Secondnumber=int(input("Enter your secondnumber :"))
_operation=input("select operators from :(+,-,*,/) :")
if _operation == "+" :
 _Results=_firstnumber+_Secondnumber
 print(_Results)
elif _operation == "-":
 _Results=_firstnumber-_Secondnumber
 print(_Results)
elif _operation == "*":
 _Results=_firstnumber*_Secondnumber
 print(_Results)
elif _operation == "/":
 _Results=_firstnumber/_Secondnumber
 print(_Results)

else:
 print("invalid input")





  






