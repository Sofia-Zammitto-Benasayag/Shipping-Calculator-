#Shipping Calculator 

#Variables 
weight = float(input("Insert weight: "))
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
