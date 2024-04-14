weight = 4.8
# Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6 > 2:
  cost_ground = weight * 3 + 20
elif weight > 6 <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20
premium_ground_cost = 125
print("Ground Shipping Standard $", cost_ground)
print("Ground Shipping Premium $", premium_ground_cost)
# Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.5
elif weight <= 6 > 2:
  cost_drone = weight * 9
elif weight > 6 <= 10:
  cost_drone = weight * 12
else:
  cost_drone = weight * 14.25
print("Drone Shipping $", cost_drone)