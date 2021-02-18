# Modulin funktioilla voidaan laskea painoindeksi (BMI) ja kehon rasvaprosentti

# Funktioiden määrittelyt

# Painoindeksi (BMI)
def bmi(paino, pituus):
    """Laskee painoindeksin kaavalla paino jaettuna pituuden neliöllä

    Args:
        paino (float): paino kilogrammoina (kg)
        pituus (float): pituus metreinä (m)

    Returns:
        float: painoindeksi
    """
    painoindeksi = paino / pituus ** 2
    return painoindeksi