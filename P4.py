# First Class
class PI:
    # passing parameters
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

# The Second Class
class Customer:
    def __init__(self, name, address, phone, city, zipcode, age):
        self.name = name
        self.address = address
        self.phone = phone
        self.city = city
        self.zipcode = zipcode
        self.age = age

    def get_info(self):
        return f"Hello {self.name}, your address is {self.address}, your city is {self.city}, your zip code is {self.zipcode}, your age is {self.age}, and your phone number is {self.phone}."


def main():
    name = input('Enter the name: ')
    address = input('Enter the address: ')
    phone = input('Enter the phone: ')
    city = input('Enter the city: ')
    zipcode = input('Enter the zip code: ')
    age = int(input('Enter the age: '))

    customer = Customer(name, address, phone, city, zipcode, age)
    print(customer.get_info())

main()
