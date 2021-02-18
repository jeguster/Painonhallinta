# Tämä on painonhallintasovelluksen pääohjelma

# Kirjastojen ja modulien käyttöönotot
import sanity
from laskenta import *

# Varsinaisen pääohjelman alku

# Komponenttien alustukset

# Työsilmukka, ikuinen silmukka, jossa poistumistoiminto

uusi = 'K'
while True:

    # Kysytään käyttäjältä paino
    paino_str = input('Paino (kg)? ')
    paino = sanity.on_jarkeva(paino_str, 20, 300)

    pituus_str = input('Pituus (m)? ')
    pituus = sanity.on_jarkeva(pituus_str, 1, 3)

    print('painoindeksisi on', bmi(paino, pituus))
    # Poistuminen ikuisesta silmukasta
    uusi = input('Lasketaanko uuden henkilön rasvaprosentti? (K/E)')
    if uusi == 'E':
        break

