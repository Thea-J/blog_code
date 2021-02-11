# Define a class that represents black Software Pioneers
class SoftwarePioneer:

    # The class attribute expertise has the same value for all class objects
    # New objects will be assigned this attribute upon creation
    expertise = "Software";

    # Initialise each new instance of the SoftwarePioneer class
    # New objects will be assigned these attributes upon creation
    def __init__(self, fullName, profession, creation, dateCreated, dateRecognised, recognitionBody):
        self.fullName = fullName
        self.profession = profession
        self.creation = creation
        self.dateCreated = dateCreated
        self.dateRecognised = dateRecognised
        self.recognitionBody = recognitionBody

    # Define the Instance method changeTheWorld that returns a string
    def changeTheWorld(self):
        print(f"{self.fullName} changed the world in {self.dateCreated} with the creation of the {self.creation}");

    # Define the Instance method recognition that returns a string
    def recognition(self):
        print(f"{self.fullName}'s work was recognised in {self.dateRecognised} by The {self.recognitionBody}. This was approximately {self.dateRecognised - self.dateCreated} years after their work pioneered {self.creation}.");

 # Create (Instantiate) a new object from the SoftwarePioneer class and assign to a variable
mark = SoftwarePioneer("Mark E. Dean", "Computer Scientist and engineer", "Coloured Computer Monitor", 1980, 1997, "National Inventors Hall of Fame");
Marian = SoftwarePioneer("Marian Croak", "Computer Scientist and engineer", "Voice Over Internet Protocol (VoIP)", 1995, 2013, "Women in Technology International hall of fame");
mark.changeTheWorld();
Marian.recognition();
print(mark.expertise);
    



# Define a child class that represents Black Hardware Pioneers that inherits from the software pioneer class
class HardwarePioneer(SoftwarePioneer):

    # The class attribute expertise has been overridden for the child class
    expertise = "Hardware";

# Create (Instantiate) a new object from the HardwarePioneer class and assign to a variable
mary = HardwarePioneer("Mary Van Brittan Brown", "Computer Scientist and engineer", "Home Security System", 1966, 1997, "National Inventors Hall of Fame");
mary.changeTheWorld();
print(mary.expertise);
print(isinstance(mary, SoftwarePioneer)); 
