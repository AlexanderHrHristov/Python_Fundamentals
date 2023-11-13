neededExperience = float(input())
battleCount = int(input())
totalExperience = 0

for battle in range(1, battleCount + 1):
    experience_per_battle = float(input())

    if battle % 3 == 0:
        experience_per_battle += experience_per_battle * 0.15
    if battle % 5 == 0:
        experience_per_battle -= experience_per_battle * 0.10
    if battle % 15 == 0:
        experience_per_battle += experience_per_battle * 0.05

    totalExperience += experience_per_battle

    if totalExperience >= neededExperience:
        break

if totalExperience >= neededExperience:
    print(f"Player successfully collected his needed experience for {battle} battles.")
else:
    needed = neededExperience - totalExperience
    print(f"Player was not able to collect the needed experience, {needed:.2f} more needed.")
