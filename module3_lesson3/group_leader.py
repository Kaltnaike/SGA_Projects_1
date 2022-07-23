#Parent Class
class Students:
    def __init__(self):
       self.classes = [] 


 #Create a class called 'Group_leader' that inherits from the Parent class 'Students'       
class Group_leader(Students):
    def __init__(self):
        super().__init__() #incase you add anything not defined in the Students class
        self.students = []

#Define a method that adds students to list of students under Group_leader
    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student} added to student list {self.students}")

#Define a method that removes students from the list of students under the Group_leader
    def remove_students(self, student):
        for i in self.students:
            if i == student:
                self.students.remove(i)
                print(f"Student {student} removed from student list {self.students}")

#Define a method that prints full names of students
    def print_students(self):
        for i in self.students:
            print(f"\nFull Name for Student: {i}")
    
    def fullname(self):
        for i in self.students:
              print(f'{i}@stutern.com')
        

#Create 3 more instances of the Parent class
class_rep1 = Students()
class_rep2 = Students()
class_rep3 = Students()

#Create 2 instances of the Sub class you created
first_lead = Group_leader()
second_lead = Group_leader()

#Add 2 students each to the list of students under the instance of the sub class
first_lead.add_student("Awonaike Ganiat")
first_lead.add_student("Asade Dara")

second_lead.add_student("Osuagwu Victor")
second_lead.add_student("Umeh Miriam")


#Remove 1 student each from the instance of the sub class
first_lead.remove_students("Awonaike Ganiat")
second_lead.remove_students("Osuagwu Victor")


#Print the fullname of the students in the sub classes
first_lead.print_students()
second_lead.print_students()


#print the email of the instance of the subclass
first_lead.fullname()
second_lead.fullname()