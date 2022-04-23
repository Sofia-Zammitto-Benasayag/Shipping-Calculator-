#Shipping Calculator 
print("Welcome to Sally's Shippers.")
print("Find the most afforable rate to ship.")
#Variables 
weight = float(input("Insert package weight: "))
cost_ground_premium = 125.00

#Ground shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20 
elif weight <= 10:
  cost_ground = weight * 4 + 20  
elif weight > 10:
  cost_ground = weight * 4.75 + 20   

print("Your total for ground shipping is $" + str(cost_ground))
print("Your total for ground premium is $ " + str(cost_ground_premium))

#Drone shipping
if weight <= 2:
  cost_drone = weight * 4.5 + 0
elif weight <= 6:
  cost_drone = weight * 9 + 0
elif weight <= 10:
  cost_drone = weight * 12 + 0
elif weight > 10:
  cost_drone = weight * 14.25 + 0    

print("Your total for drone shipping is $" + str(cost_drone))

if cost_ground < cost_drone and cost_ground < cost_ground_premium:
  print("Ground shipping is most affortable.")  
  
if cost_ground_premium < cost_ground and cost_ground_premium < cost_drone:
  print("Ground Premium is most affortable.")
  print("Become a premium member today!")

if cost_drone < cost_ground and cost_drone > cost_ground_premium:
  print("Drone shipping is most affortable.")
  print("Try our newest shipping today!")

#print(21.5 < 4.5)

#So far working for everything but weight between 1 and 10!