# Define a class that represents black Software Pioneers
class SoftwarePioneer:

    # The class attribute expertise has the same value for all class objects
    # New objects will be assigned this attribute upon creation
    expertise = "Software";

    # Initialise each new instance of the SoftwarePioneer class
    # New objects will be assigned these attributes upon creation
    def __init__(self, full_name, profession, creation, date_created, date_recognised, recognition_body):
        self.full_name = full_name
        self.profession = profession
        self.creation = creation
        self.date_created = date_created
        self.date_recognised = date_recognised
        self.recognition_body = recognition_body

    # Define the Instance method change_the_world that returns a string
    def change_the_world(self):
        print(f"{self.full_name} changed the world in {self.date_created} with the creation of the {self.creation}");

    # Define the Instance method recognition that returns a string
    def recognition(self):
        print(f"{self.full_name}'s work was recognised in {self.date_recognised} by The {self.recognition_body}. This was approximately {self.date_recognised - self.date_created} years after their work pioneered {self.creation}.");

# Create (Instantiate) a new object from the SoftwarePioneer class and assign to a variable
mark = SoftwarePioneer("Mark E. Dean", "Computer Scientist and engineer", "Coloured Computer Monitor", 1980, 1997, "National Inventors Hall of Fame");
marian = SoftwarePioneer("Marian Croak", "Computer Scientist and engineer", "Voice Over Internet Protocol (VoIP)", 1995, 2013, "Women in Technology International hall of fame");

#Call methods and variables
mark.change_the_world();
marian.recognition();
print(mark.expertise);
    



# Define a child class that represents Black Hardware Pioneers that inherits from the software pioneer class
class HardwarePioneer(SoftwarePioneer):

    # The class attribute expertise has been overridden for the child class
    expertise = "Hardware";

    # Define a private variable age that can only be accessed within the method setage
    __age = 0;

    # Define a public method setage that updates the private variable __age
    def setage(self, age):
        self.__age = age
    
    # Define a public method getage that retrieves the private variable __age
    def getage(self):
        return self.__age

    # Define the Instance method change_the_world that returns a string
    def change_the_world(self):
        print(f"{self.full_name} changed the world in {self.date_created}, at the age of {self.getage()} with the creation of the {self.creation}");

# Create (Instantiate) a new object from the HardwarePioneer class and assign to a variable
marie = HardwarePioneer("Marie Van Brittan Brown", "Computer Scientist and engineer", "Home Security System", 1966, 1969, "National Scientists Committee");

#Call methods and variables
print(marie.expertise);
marie.setage(21);
marie.change_the_world();
print(isinstance(marie, SoftwarePioneer)); #All objects created from a child class are instances of the parent class.
