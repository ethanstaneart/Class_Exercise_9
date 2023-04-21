class Students:
    # the keyword (self) is used to access variables that belong to that class.
    def GetInformation(self):
        print("student Lastname name is " + self.Lastname)
        print("student Firstname name is " + self.Firstname)
        print("student Address name is " + self.Address)
        print("student City name is " + self.City)
        print("student state name is " + self.State)
        print("student Zipcode name is " + self.Zipcode)

# creates the Student1 object
Student1 = Students()
Student1.Lastname = "Doe"
Student1.Firstname = "Jane"
Student1.Address = "111 St"
Student1.City = "Santa Ana"
Student1.State = "CA"
Student1.Zipcode = "12345"

# creates the Student2 object
Student2 = Students()
Student2.Lastname = "Cantor"
Student2.Firstname = "Mike"
Student2.Address = "222 St"
Student2.City = "Garden Grove"
Student2.State = "CA"
Student2.Zipcode = "67890"

# creates the Student3 object
Student3 = Students()
Student3.Lastname = input("Enter student's lastname: ")
Student3.Firstname = input("Enter student's firstname: ")
Student3.Address = input("Enter student's address: ")
Student3.City = input("Enter student's city: ")
Student3.State = input("Enter student's state: ")
Student3.Zipcode = input("Enter student's zipcode: ")

# Calling the function
Student1.GetInformation()
Student2.GetInformation()
Student3.GetInformation()
