# Define a class that represents black Software Pioneers
class SoftwarePioneer:

    # The class attribute race has the same value for all class objects
    # New objects will be assigned these attributes upon creation
    race = "Black"

    # Initialise each new instance of the Pioneer class
    # New objects will be assigned these attributes upon creation
    def __init__(self, fullName, profession, creation, dateCreated, dateRecognized, recognitionBody):
        self.fullName = fullName
        self.profession = profession
        self.creation = creation
        self.dateCreated = dateCreated
        self.dateRecognized = dateRecognized
        self.recognitionBody = recognitionBody

    # Define the Instance method changeTheWorld that returns a string
    def changeTheWorld(self):
        return f"{self.fullName} changed the world in {self.dateCreated} with the creation of the {self.creation}"

    # Create (Instantiate) a new object from the Pioneer class and assign them to a variable
    mark = SoftwarePioneer("Mark E. Dean", "Computer Scientist and engineer", "Coloured Computer Monitor", 1980, 1997, "National Inventors Hall of Fame");
    mark.changeTheWorld()
    
    # Instantiate the class with Lisa Gelobter & Marian Croak ....



# Define a child class that represents Black Hardware Pioneers that inherits from the software pioneer class
class HardwarePioneer(SoftwarePioneer):
    pass

    # Instantiate the class with Mary Van Brittan Brown
