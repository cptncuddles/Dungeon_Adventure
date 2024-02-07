class Sedan:
  def __init__(self, name, fuel_range, horsepower, capacity, cost):
    self.name = name
    self.fuel_range = fuel_range
    self.horsepower = horsepower
    self.capacity = capacity
    self.cost = cost
  def __repr__(self):
    return self.name
  def description(self):
    return "This {name} has room for {capacity} passengers. It comes equipped with a powerful engine putting out {horsepower} BHP, yet still acheiving {fuel_range} miles on each tank! Prices starting as low as ${cost}.".format(name=self.name, capacity=self.capacity, horsepower=self.horsepower, fuel_range=self.fuel_range, cost=self.cost)

class Truck():
  def __init__(self, name, fuel_range, horsepower, capacity, towing_capacity, cost):
    self.name = name
    self.fuel_range = fuel_range
    self.horsepower = horsepower
    self.capacity = capacity
    self.towing_capacity = towing_capacity
    self.cost = cost
  def __repr__(self):
    return self.name
  def description(self):
    return "This {name} comes equipped with a {horsepower} BHP engine capable of towing {towing_capacity} lbs., while also seating {capacity} comfortably. You will also enjoy less stops for fuel with a range of {fuel_range} miles! Prices starting at ${cost}.".format(name=self.name, horsepower=self.horsepower, towing_capacity=self.towing_capacity, capacity=self.capacity, fuel_range=self.fuel_range, cost=self.cost)

class Van():
  def __init__(self, name, fuel_range, horsepower, capacity, cost):
    self.name = name
    self.fuel_range = fuel_range
    self.horsepower = horsepower
    self.capacity = capacity
    self.cost = cost
  def __repr__(self):
    return self.name
  def description(self):
    return "You will love this {name}! Boasting seating for {capacity}, the vehicle comes equipped with a {horsepower} BHP engine with a range of {fuel_range} miles! Prices start at ${cost}.".format(name=self.name, capacity=self.capacity, horsepower=self.horsepower, fuel_range=self.fuel_range)

class Motorcycle:
  def __init__(self, name, fuel_range, horsepower, capacity, top_speed, cost):
    self.name = name
    self.fuel_range = fuel_range
    self.horsepower = horsepower
    self.capacity = capacity
    self.top_speed = top_speed
    self.cost = cost
  def __repr__(self):
    return self.name
  def description(self):
    return "Your dreams have come true! This {name} is extremely powerful for it's size! A {horsepower} BHP engine allows this machine to acheive a top speed of {top_speed} in no time at all! With such a compact fuel tank it's amazing that this motorcycle still achieves {fuel_range} miles on each tank! Prices starting as low as ${cost}.".format(name=self.name, horsepower=self.horsepower, top_speed=self.top_speed, fuel_range=self.fuel_range, cost=self.cost)

wrx = Sedan('Subaru WRX', 365, 275, 5, 30.605)
cts = Sedan('Cadillac CT5', 527 ,237, 5, 38.195)
ford = Truck('Ford F150', 483, 400, 3, 14000, 34.585)
toyota = Truck('Toyota Tundra', 428, 389, 3, 11160, 38.985)
honda = Van('Honda Odyssey', 429, 280, 8, 37.490)
crysler = Van('Crysler Pacifica', 418, 287, 7, 38.020)
kw = Motorcycle('Kawasaki Ninja', 173, 45, 117, 1, 5.700)
ic = Motorcycle('Indian Chief', 167, 111, 115, 2, 15.000)

potential_vehicles = [wrx, cts, ford, toyota, honda, crysler, kw, ic]
result = "Based on your input we have determined the best vehicle for you is the: "
intro = input("Hello! We are going to ask you a series of questions to help determine which vehicle is best for you! Please take your time to consider before answering. Please press [Enter] to continue.")

q1 = input("How much are you expecting to spend? ")
if q1 < str(16.000):
  u1 = [wrx, cts, ford, toyota, honda, crysler]
  potential_vehicles = [x for x in potential_vehicles if x not in u1]
  if q1 < str(10.000):
    u2 = [ic]
    potential_vehicles = [x for x in potential_vehicles if x not in u1]
    print(result)
    print(potential_vehicles)
  else:
    q1a = input("What top speed are you wanting to achieve? ")
    if q1a > 170:
      print(result)
      print(potential_vehicles)
    else:
      print(result)
      print(potential_vehicles)
elif q1 < str(38.000) and q1 > str(16.000):
  u3 = [cts, toyota, crysler, kw, ic]
  potential_vehicles = [x for x in potential_vehicles if x not in u3]
  q1b = input("How many people are you expecting to ride with you at any given time? ")
  if q1b <= str(3):
    u4 = [wrx, honda]
    potential_vehicles = [x for x in potential_vehicles if x not in u4]
    print(result)
    print(potential_vehicles)
  elif q1b <= str(5):
    u5 = [honda]
    potential_vehicles = [x for x in potential_vehicles if x not in u5]
    q1b1 = input("Are you looking to tow anything with this vehicle? Y/N ")
    if q1b1 == 'Y':
      u6 = [wrx]
      potential_vehicles = [x for x in potential_vehicles if x not in u6]
      print(result)
      print(potential_vehicles)
    else:
      u7 = [ford]
      potential_vehicles = [x for x in potential_vehicles if x not in u7]
      print(result)
      print(potential_vehicles)
elif q1 > str(38.000):
  u10 = [wrx, ford, honda, kw, ic]
  potential_vehicles = [x for x in potential_vehicles if x not in u10]
  q1c = input("How many people are you expecting to ride with you at any given time? ")
  if q1c <= str(3):
    u11 = [cts, crysler]
    potential_vehicles = [x for x in potential_vehicles if x not in u4]
    print(result)
    print(potential_vehicles)
  elif q1c <= str(5):
    u12 = [crysler]
    potential_vehicles = [x for x in potential_vehicles if x not in u5]
    q1c1 = input("Are you looking to tow anything with this vehicle? ")
    if q1c1 == 'Y':
      u13 = [cts]
      potential_vehicles = [x for x in potential_vehicles if x not in u13]
      print(result)
      print(potential_vehicles)
    else:
      u14 = [toyota]
      potential_vehicles = [x for x in potential_vehicles if x not in u14]
      print(result)
      print(potential_vehicles)
  elif q1c > str(5):
    u15 = [cts, toyota]
    potential_vehicles = [x for x in potential_vehicles if x not in u15]
    print(result)
    print(potential_vehicles)

result = potential_vehicles[0].description
q2 = input("Would you like to know more about the vehicle we have recommended? Y/N ")
if q2 == "Y":
  print(result)
  #I NEED TO FIGURE OUT HOW TO ADD THE CLASS METHOD TO THE LIST SO I CAN PRINT THE DESCRIPTION FOLLOWING THE SELECTION OF THE VEHICLE.
else:
  print("Thank you for trying our new automated car selection filter. Please reach out to your local sales representative with any questions you may have!")
###Things that I can add/modify to expand the program: change the algorithm so that at the end it is including all the vehicles in the price range and then pairing it all down to one through flow control, add csv integration and modify logic to work with key:value pairs not arrays, add output that directs the customer to a chat with a salesperson.