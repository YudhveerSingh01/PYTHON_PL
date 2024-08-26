class Constructor:
    def __init__(self,name,course):#CONSTRUCTOR
        self.name=name
        self.course=course
    def view(self):
        print("Name=",self.name)
        print("Course",self.course)

co=Constructor("AMIT","BIT") #here mc is an object of MyClass
co.view()
