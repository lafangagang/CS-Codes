Name=()
Age=()
Mobile_Number=() 

def Input(N,A,MN):
    for i in range(5):
        N=N+(input("Enter Your Name "),)
        A=A+(int(input("Enter Your Age ")),)
        MN=MN+(int(input("Enter Your Mobile Number ")),)
    return [N,A,MN]   
       
Ar=Input(Name,Age,Mobile_Number)
Name=Ar[0]
Age=Ar[1]
Mobile_Number=Ar[2]

for i in range(5):
    print("\nName of the Employee is %s \nAge of the Employee is %d \nMobile Number of the Employee is %d \n"%(Name[i],Age[i],Mobile_Number[i]))
