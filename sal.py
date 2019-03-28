def cost_of_ground_shipping(weight):
  if weight <= 2 and weight >0:
    cost = 20+ weight * 1.5
  elif weight <=6:
    cost = 20+weight *3
  elif weight <=10:
    cost = 20+weight*4
  else:
    cost = 20+weight*4.75
  return cost

cost_of_premium_ground_shipping = 125
  
def cost_of_drone_shipping(weight):
  if weight <= 2 and weight >0:
    cost = weight * 4.5
  elif weight <=6:
    cost = weight *9
  elif weight <=10:
    cost = weight*12
  else:
    cost = weight*14.25
  return cost


def cheapest_shipping(weight):
  cheapest_shipping = cost_of_ground_shipping(weight)
  if cost_of_premium_ground_shipping < cheapest_shipping:
    cheapest_shipping = cost_of_premium_ground_shipping
  if cost_of_drone_shipping(weight)< cheapest_shipping:
    cheapest_shipping = cost_of_drone_shipping(weight)
  if cheapest_shipping == cost_of_ground_shipping(weight):
     return "The cheapest is ground shipping with price "+ str(cheapest_shipping)
  elif cheapest_shipping == cost_of_premium_ground_shipping:
     return "The cheapest is premium ground shipping with price "+ str(cheapest_shipping)
  else:
     return "The cheapest is drone shipping with price"+ str(cheapest_shipping)

"""
============= RESTART: C:/Users/t908586/test/git_practice/sal.py =============
>>> cheapest_shipping(4.8)
'The cheapest is ground shipping with price 34.4'
>>> cheapest_shipping(41.5)
'The cheapest is premium ground shipping with price 125'
>>> cost_of_drone_shipping(41.5)
591.375
>>> cost_of_ground_shipping(41.5)
217.125
>>>
"""
