from multipledispatch import dispatch

# class Students:
#     @dispatch(str, int)
#     def __init__(self, name, rno):
#         self.name = name
#         self.rno = rno
    
#     @dispatch(bool, float)
#     def __init__(self, absent, age):
#         self.age = age
#         self.absent = absent
    
#     def disp(self):
#         if hasattr(self, 'name'):
#             print("Name:", self.name)
#             print("Roll Number:", self.rno)
#         elif hasattr(self, 'absent'):
#             print("Absent:", self.absent)
#             print("Age:", self.age)

# s1 = Students("sahil", 33)
# s1.disp()

# s2 = Students(True, 12.5)
# s2.disp()




@dispatch(int,int)
def disp(val1,val2):
    print("INT METHOD",val1*val2)

@dispatch(str,str)
def disp(val1,val2):
    print("INSIDE STR",val1,val2)

disp(2,2)
disp("sahil","kotekar")






















class Sample:
    @dispatch(str)
    def __init__(self,name):
        self.name=name

    @dispatch(int)
    def __init__(self,age):
        self.age=age

s1=Sample("sahil")
s2=Sample(25)
print(s1.name)
print(s2.age)



@dispatch(int,int)
def product(first,second):
    result=first*second
        