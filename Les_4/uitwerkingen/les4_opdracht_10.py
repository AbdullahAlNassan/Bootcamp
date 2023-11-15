seconden_per_minuut = 60
seconden_per_uur = 60 * seconden_per_minuut

uren_per_dag = 24
uren_per_week = 7 * uren_per_dag

seconden_per_dag = uren_per_dag * seconden_per_uur
seconden_per_week = uren_per_week * seconden_per_uur
seconden_per_jaar = 365 * uren_per_dag * seconden_per_uur  # Hier gaan we uit van een niet-schrikkeljaar

print(f"Aantal seconden in een dag: {seconden_per_dag} seconden")
print(f"Aantal seconden in een week: {seconden_per_week} seconden")
print(f"Aantal seconden in een jaar: {seconden_per_jaar} seconden")
