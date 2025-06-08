Id=int(input("Enter Id: "))
Name=(input("Enter Name: "))
Address=(input("Enter Address: "))
Qualification1=(input("Enter Qualification : "))
Passing_Year1=(input("Enter Passing_Year : "))
Qualification2=(input("Enter Qualification : "))
Passing_Year2=(input("Enter Passing_Year : "))

Id1=int(input("Enter Id: "))
Name1=(input("Enter Name: "))
Address1=(input("Enter Address: "))
Qualification3=(input("Enter Qualification : "))
Passing_Year3=(input("Enter Passing_Year : "))
Qualification4=(input("Enter Qualification : "))
Passing_Year4=(input("Enter Passing_Year : "))

listdata=[]

Studentdetails={}
Studentdetails["Id"] = Id
Studentdetails["Name"] = Name
Studentdetails["Address"] = Address
Studentdetails["Qualification"] =[
{"Name": Qualification1,"Passing_Year": Passing_Year1},
{"Name": Qualification2,"Passing_Year": Passing_Year2},
]
listdata.append(Studentdetails)

Studentdetails1={}
Studentdetails1["Id"] = Id1
Studentdetails1["Name"] = Name1
Studentdetails1["Address"] = Address1
Studentdetails1["Qualification"] =[
{"Name": Qualification3,"Passing_Year": Passing_Year3},
{"Name": Qualification4,"Passing_Year": Passing_Year4}
]
listdata.append(Studentdetails1)

print(listdata)
