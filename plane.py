import os
import time

test = "Vantaa"

# Lentokoneen ASCII-kuva
plane = [
        r"         -=\`\ ",
        r"     |\ ____\_\__ ",
        r"   -=\c`OOOOOOOOOD`) ",
        r"      `~~~~~/ /~~`",
        r"        -==/ /",
        r"          '-' "
        rf"   To {test}"]

def clear_screen():
    # Tyhjennä näyttö riippuen järjestelmästä (Windows 'cls' tai Unix 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    width = 50  # Määritä terminaalin leveys (voit muuttaa tätä)
    x_pos = 0  # Lentokoneen alkuasetus

    while x_pos < width - len(plane[0]):
        clear_screen()  # Tyhjennä näyttö ennen uutta tulostusta
        
        # Piirretään lentokone rivittäin
        for row in plane:
            print(" " * x_pos + row)
        
        time.sleep(0.1)  # Aseta animaation nopeus
        x_pos += 3  # Siirrä lentokonetta oikealle
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()

      


