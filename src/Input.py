Marks={}
Id=int(input("Please Enter Id: "))
Name=(input("Please Enter Name: "))
Address=(input("Please Enter Address: "))
Hindi=int(input("Please Enter Marks in Hindi: "))
English=int(input("Please Enter Marks in English: "))
Math=int(input("Please Enter Marks in Math: "))
Science=int(input("Please Enter Marks in Science: "))

Marks=[
    {
     "Id": Id,
     "Name": Name,
     "Address": Address,
     "Hindi": Hindi,
     "English": English,
     "Math": Math,
     "Science": Science
    }
]
#print(Marks)

Total_Marks= (Hindi+English+Math+Science)
print("Total Marks=", Total_Marks)

Percentage= (Hindi+English+Math+Science)/4
print("Percentage=", Percentage)

if Percentage>=60:
    Division= "First Divison"
elif Percentage>=45:
    Division= "Second Divion"
elif Percentage>=36:
    Division= "Third Divison"
elif Percentage<36:
    Division= "Fail"

print("Divison=", Division)