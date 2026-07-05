print("Student Information System")
class student:
    def __init__(self,name,rollno,deparment,year):
        self.name = name
        self.rollno = rollno
        self.deparment = deparment
        self.year = year
    def display(self):
        print("Name : ",self.name)
        print("Roll Number : ",self.rollno)
        print("Deparment : ",self.deparment)
        print("Year : ",self.year)
print("STUDENT-1")
student1 = student("Radha",121,"AI & DS","2nd year")
student1.display()
print("STUDENT-2")
student2 = student("Krishna",131,"AIML","3RD YEAR")
student2.display()