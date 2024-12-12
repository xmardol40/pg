def dec_to_bin(cislo):
    # funkce prevede cislo na binarni reprezentaci (cislo muze byt str i int!!!)
    # 7 -> "111"
    # 5 -> "101"

    vysledek = ""
    number = int(cislo)

    if number  == 0:
        return vysledek + "0"

    while number > 0:
        vysledek = str(number % 2) + vysledek
        number = number // 2
            

    return vysledek


def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"


test_bin_to_dec()
