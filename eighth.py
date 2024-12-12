def bin_to_dec(binarni_cislo):
    # funkce spocita hodnotu predavaneho binarniho cisla (binarni_cislo muze byt str i int!!!)
    # 111 -> 7
    # "101" -> 5
    binarni_cislo = str(binarni_cislo)
    bin_cislo_int = int(binarni_cislo)
    cislo = 0
    if binarni_cislo == "0":
        return 0
    elif bin_cislo_int < 0:
        return f"Toto není binární číslo"
    else:
        for i in range(0, len(binarni_cislo)):
          index = len(binarni_cislo)-1-i
          vypocet = int(binarni_cislo[index])*(2**i)
          cislo += vypocet
        return cislo



def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128

