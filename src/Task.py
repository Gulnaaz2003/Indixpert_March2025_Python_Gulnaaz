Id=int(input("plz enter ID: "))
Name=(input("plz enter Name: "))
Address=(input("plz enter Address: "))
Contact_number=(input("plz enter Contact_number: "))
Qualification=(input("plz enter Qualification: "))
Passing_Year=(input("Plz Enter Passing_Year: "))
Qualification2=(input("plz enter Qualification: "))
Passing_Year2=(input("Plz Enter Passing_Year: "))
Qualification3=(input("plz enter Qualification: "))
Passing_Year3=(input("Plz Enter Passing_Year: "))
Qualification4=(input("plz enter Qualification: "))
Passing_Year4=(input("Plz Enter Passing_Year: "))

print("~"*50)

#Id1=int(input("plz enter ID: "))
#Name1=(input("plz enter Name: "))
#Address1=(input("plz enter Address: "))
#Contact_number1=(input("plz enter Contact_number: "))
#print("~"*50)

#Id2=int(input("plz enter ID: "))
#Name2=(input("plz enter Name: "))
#Address2=(input("plz enter Address: "))
#Contact_number2=(input("plz enter Contact_number: "))
#print("~"*50)

Data=[
    {"id":id ,
    "Name":Name , 
     "Address": Address , 
     "Contact_number": Contact_number , 
     "Qualification":[
         {"name": Qualification},
        {"Passing_Year" : Passing_Year },
        {"name": Qualification2},
        {"Passing_Year" : Passing_Year2 },
        {"name": Qualification3},
        {"Passing_Year" : Passing_Year3 },
        {"name": Qualification4 },
        {"Passing_Year" : Passing_Year4 }
       ]
        
    }
    ]
#Data=[{"id1":id , "Name1":Name , "Address1": Address , "Contact_number1": Contact_number }]
#Data=[{"id2":id , "Name2":Name , "Address2": Address , "Contact_number2": Contact_number }]

print(Data)




