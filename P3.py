class PI:
    # passing three parameters
    def GetInformation(self, LN, FN, Age, Address, City, State, Zipcode):
        return LN + ", " + FN + ", " + str(Age) + ", " + Address + ", " + City + ", " + State + ", " + Zipcode

PersonalInformation = PI()
PersonalInformation.Lastname = input('Enter the lastname: ')
PersonalInformation.Firstname = input('Enter the firstname: ')
PersonalInformation.Age = int(input('Enter the age: '))
PersonalInformation.Address = input('Enter the address: ')
PersonalInformation.City = input('Enter the city: ')
PersonalInformation.State = input('Enter the state: ')
PersonalInformation.Zipcode = input('Enter the zipcode: ')

print(PersonalInformation.GetInformation(
    PersonalInformation.Lastname,
    PersonalInformation.Firstname,
    PersonalInformation.Age,
    PersonalInformation.Address,
    PersonalInformation.City,
    PersonalInformation.State,
    PersonalInformation.Zipcode
))
