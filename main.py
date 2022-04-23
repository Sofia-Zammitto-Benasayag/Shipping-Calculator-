#Shipping Calculator 

#Variables 
weight = 20

#Ground shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20 
elif weight <= 10:
  cost_ground = weight * 4 + 20  
elif weight > 10:
  cost_ground = weight * 4.75 + 20   

print("You're total is $" + str(cost_ground))