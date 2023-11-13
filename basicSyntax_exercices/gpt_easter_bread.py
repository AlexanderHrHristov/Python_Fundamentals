import math

budget = float(input())
flour_price_per_kg = float(input())

eggs_price_per_pack = 0.75 * flour_price_per_kg
milk_price_per_liter = 1.25 * flour_price_per_kg

loaves_count = 0
colored_eggs = 0

while budget >= flour_price_per_kg + eggs_price_per_pack + (0.25 * milk_price_per_liter):
    budget -= flour_price_per_kg
    budget -= eggs_price_per_pack
    budget -= 0.25 * milk_price_per_liter

    loaves_count += 1
    colored_eggs += 3

    if loaves_count % 3 == 0:
        lost_eggs = loaves_count - 2
        colored_eggs -= lost_eggs

money_left = round(budget, 2)

print(f"You made {loaves_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")
