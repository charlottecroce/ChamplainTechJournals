# Input the data
cupcake_dollars = int(input())
cupcake_cents = int(input())
num_cupcakes = int(input())

# Your code here

total_cost_cents = (((cupcake_dollars * 100) + cupcake_cents) * num_cupcakes)
total_cost_dollars = total_cost_cents // 100
total_cost_cents = total_cost_cents % 100
print(total_cost_dollars, total_cost_cents)