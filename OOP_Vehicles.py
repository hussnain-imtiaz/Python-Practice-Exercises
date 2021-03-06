# -*- coding: utf-8 -*-
"""Python Marlon - Assignment - 6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TvpszObtsLjypnttvsuuhTVAgvnP-mut

1. Object Oriented Programming and Inheritance - 30%
Create a Vehicle class with the attributes and functions detailed in the class diagram. - 10%
Create a Car class as a child of the Vehicle class with the attributes and functions detailed in the class diagram. - 10%
Create a Pickup class as a child of the Vehicle class with the attributes and functions detailed in the class diagram. - 10%
2. Demonstrate usage of previously studied programming constructs (functions, conditionals, loops) - 60%
Using a function, display a menu prompting the user to add a Car or a Pickup to their virtual garage. - 15%
Your program must allow the user to have multiple vehicles in their virtual garage and must have at least one Car and one Pickup. - 15 %
Your program will prompt the user to define the attributes of the vehicles in their garage. - 10%
The options attribute will be defined as a python list chosen by the user when presented with a menu of programmer chosen vehicle options that can apply to both cars and pickup trucks (i.e. power mirrors, power locks, remote start, backup camera, bluetooth, cruise control, etc) - 20%
3. When the user has finished adding and defining vehicles for their garage the program will output the vehicles with their accompanying attributes and options as specified by the user. -10 %
"""

class Vehicle:
  def __init__(self, make, model, color, fuelType, options):
    self.make = make
    self.model = model
    self.color = color
    self.fuelType = fuelType
    self.options = options

  def getMake(self):
    return self.make
  
  def getModel(self):
    return self.model
  
  def getColor(self):
    return self.color
  
  def getFuelType(self):
    return self.fuelType
  
  def getOptions(self):
    return self.options

class Car(Vehicle):
  def __init__(self, make, model, color, fuelType, options, engineSize, numDoors):
    super().__init__(make, model, color, fuelType, options)
    self.engineSize = engineSize
    self.numDoors = numDoors

  def getEngineSize(self):
    return self.engineSize
  
  def getNumDoors(self):
    return self.numDoors

class Pickup(Vehicle):
  def __init__(self, make, model, color, fuelType, options, cabStyle, bedLength):
    super().__init__(make, model, color, fuelType, options)
    self.cabStyle = cabStyle
    self.bedLength = bedLength

  def getCabStyle(self):
    return self.cabStyle
  
  def getBedLength(self):
    return self.bedLength
  

def displayMenu():
  print('What do you want to add?:')
  response = input('1. Car \n2.Pickup\n')
  return response

def print_garage(virtual_garage):
  print('----- Your Virtual Grage -------')
  for item in virtual_garage:
    if type(item) == Car:
      print('---Car---')
      print('Make:', item.getMake())
      print('Model:', item.getModel())
      print('Color:', item.getColor())
      print('FuelType:', item.getFuelType())
      print('EngineSize:', item.getEngineSize())
      print('Options:', item.getOptions())
      print('NumDoors:', item.getNumDoors())
      print()

    else:
      print('---Pickup---')
      print('Make:', item.getMake())
      print('Model:', item.getModel())
      print('Color:', item.getColor())
      print('FuelType:', item.getFuelType())
      print('CabStyle:', item.getCabStyle())
      print('Options:', item.getOptions())
      print('BedLength:', item.getBedLength())
      print()


if __name__ == '__main__':
   car_count = 0
   pickup_count = 0
   virtual_garage = []
   print('----------------Welcome to the virtual garage----------------')
   while True:
     response = displayMenu() 

     if response == '1': 
       make = int(input('Enter the make year: '))
       model = int(input('Enter the model: '))
       color = input('Enter the car color: ')
       fuelType = input('Enter the car fuelType: ')
       engineSize = input('Enter the car engineSize: ')
       numDoors = int(input('Enter the number of doors in the car: '))
       options = input('Provide other options available in car (write options separated by commas): ').split()
       car = Car(make, model, color, fuelType, options, engineSize, numDoors)
       virtual_garage.append(car)
       print()


     elif response == '2':
       make = int(input('Enter the make year: '))
       model = int(input('Enter the model: '))
       color = input('Enter the Pickup color: ')
       fuelType = input('Enter the Pickup fuelType: ')
       cabStyle = input('Enter the Pickup cabStyle: ')
       bedLength = int(input('Enter the length of bed(feet)in Pickup: '))
       options = input('Provide other options available in Pickup (write options separated by commas): ').split()
       pickup = Pickup(make, model, color, fuelType, options, cabStyle, bedLength)
       virtual_garage.append(pickup)
       print()
     
     else:
       print('[WARNING] Invalid Response - Try again')
       continue
    
     for item in virtual_garage:
        if type(item) == Car:
          car_count += 1
        else:
          pickup_count += 1

     if car_count < 1 or pickup_count < 1: 
        print()
        print('[INFO] Your Garage should must contain atleast one Pickup and atleast one Car. Try to add missing.')
        continue

     add_more = input('Do you want to add more? (y/n)')

     if add_more.lower() == 'n':
       break 
       print('Good bye!!!')

   print_garage(virtual_garage)

