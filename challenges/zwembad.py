def calculate_ground_removal(length, width, depth):
    # Bereken de hoeveelheid grond die moet worden afgevoerd voor een zwembad
    pool_volume = round(length * width * depth, 2)
    return pool_volume


def calculate_quote(length, width, depth, distance):
    # Voorrijkosten
    if distance < 50:
        if pool_volume < 20:
            travel_cost = 100 + distance * 1.25
        else:
            travel_cost = 250 + distance * 2.15
    else:
        if pool_volume < 20:
            travel_cost = 100 + distance * 1.15
        else:
            travel_cost = 250 + distance * 2.05

    # Uitgraven kosten
    excavation_cost = 25 * pool_volume

    # Afvoeren grond kosten
    removal_cost = 32.5 * pool_volume

    return travel_cost, excavation_cost, removal_cost


def calculate_finish_cost(pool_volume, price_per_m2, additional_red_price, additional_color_price):
    # Bereken de oppervlakte van het zwembad
    pool_surface_area = round(2 * (length * width + length * depth + width * depth), 2)

    # Bereken de kosten voor afwerken met beton + tegels
    if pool_volume < 20:
        finish_cost = pool_surface_area * price_per_m2
    else:
        finish_cost = pool_surface_area * (price_per_m2 - additional_red_price)

    return finish_cost + additional_color_price


# Stap 1
pool_volume = calculate_ground_removal(8, 3, 1.5)
print(pool_volume)

# Stap 2
length, width, depth = 8, 3, 1.5
distance = 0  # Geen voorrijkosten in deze stap
travel_cost, excavation_cost, removal_cost = calculate_quote(length, width, depth, distance)

print(f"Offerte voor een zwembad van {length} bij {width} bij {depth} meter (inhoud: {pool_volume} m3)")
print(f"Uitgraven:                         € {excavation_cost:.2f}")
print(f"Afvoeren grond:               € {removal_cost:.2f}")
print(f"Totaal:                               € {excavation_cost + removal_cost:.2f}")

# Stap 3
length, width, depth = 8, 3, 1.5
distance = 60
travel_cost, excavation_cost, removal_cost = calculate_quote(length, width, depth, distance)

print(f"Offerte voor een zwembad van {length} bij {width} bij {depth} meter (inhoud: {pool_volume} m3)")
print(f"Uitgraven:                          € {excavation_cost:.2f}")
print(f"Afvoeren grond:               € {removal_cost:.2f}")
print(f"Voorrijkosten                    € {travel_cost:.2f}")
print(f"Totaal:                               € {excavation_cost + removal_cost + travel_cost:.2f}")

# Stap 4
length = float(input("Voer de lengte van het zwembad in: "))
width = float(input("Voer de breedte van het zwembad in: "))
depth = float(input("Voer de diepte van het zwembad in: "))
distance = float(input("Voer de afstand tot de prospect in kilometers in: "))

travel_cost, excavation_cost, removal_cost = calculate_quote(length, width, depth, distance)

print(f"Offerte voor een zwembad van {length} bij {width} bij {depth} meter (inhoud: {pool_volume} m3)")
print(f"Uitgraven:                          € {excavation_cost:.2f}")
print(f"Afvoeren grond:               € {removal_cost:.2f}")
print(f"Voorrijkosten                    € {travel_cost:.2f}")
print(f"Totaal:                               € {excavation_cost + removal_cost + travel_cost:.2f}")

# Stap 5
price_per_m2 = 200
additional_red_price = 20
additional_color_price = 125

finish_cost = calculate_finish_cost(pool_volume, price_per_m2, additional_red_price, additional_color_price)

print(f"Offerte voor een zwembad van {length} bij {width} bij {depth} meter (inhoud: {pool_volume} m3)")
print(f"Uitgraven:                          € {excavation_cost:.2f}")
print(f"Afvoeren grond:               € {removal_cost:.2f}")
print(f"Voorrijkosten                    € {travel_cost:.2f}")
print(f"Beton + tegel ({pool_surface_area} m2)      € {finish_cost:.2f}")
print(f"Totaal:                                € {excavation_cost + removal_cost + travel_cost + finish_cost:.2f}")

