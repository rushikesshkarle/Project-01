class cal:

    def addition(self,a,b):
      return a+b
      
    
    def subtract(self,a,b):
      return a-b
      

    def multiply(self,a,b):
      return a*b
     

    def divide(self,a,b):
      return a/b
      
      
    def modulus(self,a,b):
      return a%b
      

    def floordivision(self,a,b):
      return a//b
      

    def exponention(self,a,b):
      return a**b
      


obj=cal()



while True:
    print("""
<<<<<< CALCI >>>>>>
1. Addition
2. Subtract
3. Multiply
4. Divide
5. Modulus
6. Floor Division
7. Exponention
8. Exit
""")

    try:
        choice=int(input("ENTER YOUR CHOICE :- "))
        if choice==8:
                 print("Exiting......")
                 break

        a=int(input("Enter first number:- "))
        b=int(input("Enter second number:- "))  
        if choice==1:
                print("Ans is :-",obj.addition(a,b))
        elif choice==2:
                print("Ans is :-",obj.subtract(a,b))
        elif choice==3:
               print("Ans is :-",obj.multiply(a,b))
        elif choice==4:
               print("Ans is :-",obj.divide(a,b))
        elif choice==5:
               print("Ans is :-",obj.modulus(a,b))
        elif choice==6:
               print("Ans is :-",obj.floordivision(a,b))
        elif choice==7:
               print("Ans is :-",obj.exponention(a,b))
        else:
               print("Invalid number")

    except ValueError:
        print("value error")
         
    except ZeroDivisionError:
        print("Cannot divide by 0")
    