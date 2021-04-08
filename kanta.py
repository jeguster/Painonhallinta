# Tietokantamoduli

# Modulien ja kirjastojen lataukset
import sqlite3

# Luodaan uusi tietokanta projektin hakemistoon
tietokannan_nimi = 'painonhallinta.db'

def luo_tietokanta(tiedosto):
    """Luo tietokannan huom. tiedostotyypin po. .db

    Args:
        tiedosto (string): SQLite tietokantatiedoston nimi
    """
    yhteys = sqlite3.connect(tiedosto)
    yhteys.close()

def luo_taulut(tiedosto):
    """Luo SQLite tietokantaan tarvittavat taulut
    """
    # Muodostetaan yhteys tietokantaan, luodaan kanta tarvittaessa
    yhteys = sqlite3.connect(tiedosto)

    # Luodaan Henkilö-taulu
    yhteys.execute('''CREATE TABLE henkilo
        (henkilo_id INTEGER PRIMARY KEY NOT NULL,
        etunimi TEXT NOT NULL,
        sukunimi TEXT NOT NULL,
        sukupuoli INTEGER NOT NULL,
        spaiva DATE NOT NULL);''')

    # Luodaan Mittaukset-taulu
    yhteys.execute('''CREATE TABLE mittaus
        (mittaus_id INTEGER PRIMARY KEY NOT NULL,
        henkilo_id INTEGER NOT NULL,
        pituus REAL NOT NULL,
        paino REAL NOT NULL);''')

    # Suljetaan yhteys
    yhteys.close()

# Luodaan testidataan
# TODO: luo rutiinit henkilön ja mittauksen tietojen syöttämiseen

# TODO: luo rutiini tietojen lukemiseksi molemmista tauluista

# Paikallinen testaus
if __name__ == "__main__":
    luo_tietokanta(tietokannan_nimi)
    luo_taulut(tietokannan_nimi)