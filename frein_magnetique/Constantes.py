"""
Ce module contient les constantes utilisées dans la librairie de simulation.

Constantes:
    - mu_terre (float): Paramètre gravitationnel standard de la Terre en m^3/s^2.
    - rayon_terre (float): Rayon moyen de la Terre en mètres.
    - densite_cuivre (float): Densité du cuivre en kg/m^3.
    - resistance_linéaire_cuivre (float): Résistance linéaire du cuivre en ohms par mètre.
    - densite_alu (float): Densité de l'aluminium en kg/m^3.
    - resistance_linéaire_alu (float): Résistance linéaire de l'aluminium en ohms par mètre.

Enumérations:
    - Type_manoeuvre: Types de manoeuvres possibles.
    - Position_manoeuvre: Positions de manoeuvres possibles.
"""

from enum import Enum

# Constante représentant le paramètre gravitationnel standard de la Terre en m^3/s^2
mu_terre = 3.986e14
# Constante représentant le rayon moyen de la Terre en mètres
rayon_terre = 6.371e6

densite_cuivre = 933.0
resistance_linéaire_cuivre = 0.000000017
densite_alu = 2700.0
resistance_linéaire_alu =0.0000000274

# Enumération des types de manoeuvres possibles
class Type_manoeuvre(Enum):
    """
    Enumération des types de manoeuvres possibles.

    Les types de manoeuvres possibles sont:
        - 'prograde': Manoeuvre dans le sens direct de l'orbite.
        - 'retrograde': Manoeuvre dans le sens rétrograde de l'orbite.
        - 'radiale': Manoeuvre radiale, orientée vers ou à partir du centre de la Terre.
    """
    prograde = 'prograde',   # Manoeuvre dans le sens direct de l'orbite
    retrograde = 'retrograde',  # Manoeuvre dans le sens rétrograde de l'orbite
    radiale = 'radiale'   # Manoeuvre radiale, orientée vers ou à partir du centre de la Terre

# Enumération des positions de manoeuvres possibles
class Position_manoeuvre(Enum):
    """
    Enumération des positions de manoeuvres possibles.

    Les positions de manoeuvres possibles sont:
        - 'apogee': Manoeuvre effectuée à l'apogée de l'orbite.
        - 'perigee': Manoeuvre effectuée au périgée de l'orbite.
    """
    apogee = 'apogee',   # Manoeuvre effectuée à l'apogée de l'orbite
    perigee = 'perigee'   # Manoeuvre effectuée au périgée de l'orbite