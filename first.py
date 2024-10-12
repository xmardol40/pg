def sudy_nebo_lichy(cislo):
    if cislo % 2 == 0:
        print(f"{cislo} je sudé")
    else:
        print(f"{cislo} je liché")
    


if __name__ == "__main__":
    sudy_nebo_lichy(5)
    sudy_nebo_lichy(1000000)