print(5 * 2 - 3 + 4 / 2)     # Uitkomst: 10.0
print(5 * 2 - 3 + 4 / 2)     # Uitkomst: 10.0 (dezelfde uitkomst als de vorige regel)

print((5 * 2) - (3 + 4) / 2) # Uitkomst: 8.0
print(((5 * 2) - (3 + 4)) / 2) # Uitkomst: 3.5

# Verklaring van de uitkomsten:

# In de eerste twee regels wordt dezelfde expressie gebruikt, 
# waarbij de volgorde van de operaties wordt gevolgd: 
# eerst vermenigvuldigen en delen, dan optellen en aftrekken. 
# Daarom is de uitkomst in beide regels hetzelfde.

# In de derde regel worden haakjes gebruikt om de volgorde van operaties te bepalen. 
# Eerst worden de expressies binnen de haakjes berekend en vervolgens wordt de rest 
# van de berekening uitgevoerd. Dit resulteert in een andere uitkomst dan de eerste twee regels.

# In de vierde regel worden extra haakjes toegevoegd om ervoor te zorgen dat de aftrekking
# binnen de haakjes wordt uitgevoerd voordat de deling plaatsvindt. Dit leidt tot een andere uitkomst.
