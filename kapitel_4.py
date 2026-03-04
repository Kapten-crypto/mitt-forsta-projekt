# Skapa en lista
magiker = ['alice', 'david', 'carolina']

# En for-loop som hälsar på varje magiker
for magiker_namn in magiker:
    print(f"{magiker_namn.title()}, det där var ett bra trick!")
    print(f"Jag ser fram emot ditt nästa trick, {magiker_namn.title()}.\n")

print("Tack alla magiker, det var en fantastisk show!")

# Skapa listor med siffror (range)
siffror = list(range(1, 6))
print("\nEn lista med siffror:", siffror)

# Enkel matte med listor
print(f"Lägsta talet: {min(siffror)}")
print(f"Högsta talet: {max(siffror)}")
print(f"Summan av alla tal: {sum(siffror)}")
