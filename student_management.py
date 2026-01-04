class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Roll no:",self.roll_no)
        print("Marks:",self.marks)
   

class Studentmanagement:
    def __init__(self):
      self.students=[]
  
    def addstudent(self):
        print("Enter details of student to add : ")
        name=input("Enter name of the student: ")
        roll_no=int(input("Enter roll no of the student: "))
        marks=int(input("Enter marks of the student: "))
        student=Student(name,roll_no,marks)
        self.students.append(student)
        print("student added successfully")
  

    def viewstudents(self):
        if not self.students:
                print("no student their")
                return
        for s in self.students:
            s.display()
        return
    def searchstudent(self):
        rollno=int(input("enter roll no of student to search for :"))
        for s in self.students:
            if rollno==s.roll_no:
               s.display()
               return
        print("student not found")
    
    def deletestudent(self):
         rollno=int(input("enter roll no of student to delete for :"))
         for s in self.students:
             if rollno==s.roll_no:
                self.students.remove(s)
                print("student deleted succesfully")
                return
         print("student not found")
     


    def updatestudent(self):
          rollno=int(input("enter roll no of student to update for :"))
          for s in self.students:
            if rollno==s.roll_no:
             s.name=input("Enter name of the student : ")
             s.marks=int(input("Enter marks of the student :"))
             print("updated student data")
             return
          print("student not found")

def main():               
    obj=Studentmanagement()

    while True:
       print("""STUDENT MANAGEMENT SYSTEM
       1 . Add student 
       2 . Update student 
       3 . Delete student 
       4 . Search student
       5 . View student 
       6.  EXIT      """)
    
       choice=int(input("Enter your Choice: "))
       if choice==1:
           obj.addstudent()
       elif choice==2:
           obj.updatestudent()
       elif choice==3:
           obj.deletestudent()
       elif choice==4:
           obj.searchstudent()
       elif choice==5:
           obj.viewstudents()
       elif choice==6:
           print("Exiting")
           return
       else:
         print("Invalid input")
         return
    


if __name__=="__main__":
    main()
