# vehicle class
class Automobile:
    def __init__(self, Make, Model, Year, Mileage , Price):
        self.Makename = Make
        self.Modelname = Model
        self.Yearr = Year
        self.Mileagee = Mileage
        self.Pricee = Price
    # method to get values
    def getValues(self):
        return self.Makename + " " + self.Modelname + " " + self.Yearr + " " + self.Mileagee + " " + self.Pricee
    # method to display values
    def Display(self):
        print("Inventory Unit: Car \n Make: " + self.Modelname + "\n Model: " + self.Modelname + "\n Year: " + self.Yearr + 
        "\n Miles: " + self.Mileagee + "\n Price: " + self.Pricee)

# car class
class Car(Automobile):
    def __init__(self, Make, Model, Year, Mileage, Price, numOfDoors):
        Automobile.__init__(self, Make, Model, Year, Mileage, Price)
        self.numOfDoorss = numOfDoors
    # method to get values
    def GetCar(self):
        return self.getValues() + ", " + self.numOfDoorss
    # method to display values
    def Display(self):
        print("Inventory Unit: Car \nMake: " + self.Modelname + "\nModel: " + self.Modelname + "\nYear: " + self.Yearr + 
        "\nMiles: " + self.Mileagee + "\nPrice: " + self.Pricee + "\nNumber of doors: " + self.numOfDoorss)

x = Automobile("Mitsuibishi","Eclipse","2012","40000","255000")
y = Car("Mitsuibishi","Eclipse","2012","40000","255000","2")
y.Display()