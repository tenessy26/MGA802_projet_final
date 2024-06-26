from datetime import datetime
from Astraios import *
from Astraios.LecteurYAML import LecteurYAML
import os

date = datetime(2021, 3, 28)
# ---------------------Lecture du YAML---------------------
whole_path = os.path.join(os.path.abspath(os.path.curdir), "data.yaml")
parser = LecteurYAML(whole_path)
parsed_data = parser.read_yaml()

# ---------------------Création d'orbite---------------------
altitude = parsed_data['orbite']['altitude']
inclinaison = parsed_data['orbite']['inclinaison']  # Inclinaison de l'orbite [°]
dt = parsed_data['orbite']['dt']

# ---------------------Caractéristiques du satelitte---------------------
masse_satelitte = parsed_data['satelitte_magnetique']['masse']
surface_de_trainee = parsed_data['satelitte_magnetique']['surface_de_trainee']

# ---------------------Caractéristiques du cable---------------------
longueur = parsed_data['satelitte_magnetique']['cable']['longueur']
section = parsed_data['satelitte_magnetique']['cable']['section']
masse_ballaste = parsed_data['satelitte_magnetique']['cable']['ballast_mass']

# ---------------------Propriétés des matériaux---------------------
densite_cuivre = parsed_data['materiau']['copper']['densite']
resistance_linéaire_cuivre = parsed_data['materiau']['copper']['resistance_lineaire']
densite_alu = parsed_data['materiau']['aluminium']['densite']
resistance_linéaire_alu = parsed_data['materiau']['aluminium']['resistance_lineaire']


champ_magnetique = champ_mag(date)
atmosphere_terrestre = Atmosphere()

copper = materiau(densite_cuivre, resistance_linéaire_cuivre)
alu = materiau(densite_alu, resistance_linéaire_alu)
cable_mag = cable(longueur,section,alu,mass_ballast=masse_ballaste)
satMag = satellite_magnetique(masse_satelitte,surface_de_trainee,cable_mag)
satMag.calcul_des_masses()

orbite = Orbite(altitude, inclinaison, dt=dt)

orbite.calculer_temps_desorbitation_energie(satMag, atmosphere_terrestre, champ_magnetique)
orbite.calculer_temps_desorbitation_PFD(satMag, atmosphere_terrestre, champ_magnetique)

print(f"L'altitude initiale du satellite est {altitude+rayon_terre}")
print(f'La vitesse initiale du satellite est {orbite.calculer_vitesse_initial()}')