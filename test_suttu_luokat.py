# Testataan suttuluokkia

# Kirjastojen ja moduline lataukset
import suttu_luokat

def test_lintu():
    uusi_lintu = suttu_luokat.Lintu('Huuhkaja', 'bubo bubo', 'pikkujyrsijät')
    assert uusi_lintu.nimi == 'Huuhkaja'
    assert uusi_lintu.tieteellinen_nimi == 'bubo bubo'
    assert uusi_lintu.ravinto == 'pikkujyrsijät'