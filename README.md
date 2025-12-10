# Akasztofa_jatek 🪢

## Rövid leírás  
**Akasztofa_jatek** egy Pythonban írt klasszikus „Akasztófa” szójáték.  
A játék célja, hogy kitaláld a véletlenszerűen kiválasztott szót betűről betűre, miközben a hibáidat nyomon követi a program és grafikus akasztófa ábrával jeleníti meg a hibákat.

## 🎮 Játékmenet
- A program betölt egy szólistát a `szavak.txt` fájlból és véletlenszerűen kiválaszt egy szót.  
- A játékos tippel betűket:  
  - Ha a betű benne van a szóban, megjelenik a megfelelő helyen.  
  - Ha nincs benne, nő a hibák száma és kirajzolódik a hibás akasztófa része a `turtle` modul segítségével.  
- A játék véget ér, ha:  
  - A játékos kitalálja az egész szót → **nyer**  
  - 8 hibát követ el → **vesztett**, a szó felfedésre kerül.  

## 🛠️ Hogyan működik
1. A szólista a `szavak.txt` fájlból kerül betöltésre.  
2. Véletlenszerűen kiválaszt egy szót (`random.choice`).  
3. A program folyamatosan kéri a játékostól a tippelt betűt (vagy az egész szót).  
4. Hibás tippek esetén a `akasztofagecis()` függvény rajzolja a hóhér figurát lépésről lépésre a `turtle` modul segítségével.  
5. Konzolon látható az aktuális állapot: kitalált betűk és az üres helyek `_`-ként.  
6. Ha kitaláltad az egész szót, a játék kiírja a győzelmet, különben a program felfedi a helyes szót.  

## 🚀 Indítás / futtatás

1. Győződj meg róla, hogy Python 3 telepítve van, valamint a `turtle` modul elérhető.  
2. Helyezd a `szavak.txt` fájlt ugyanabba a mappába, mint a `main.py`.  
3. Futtasd a játékot:  
```bash
python main.py
📦 Projekt felépítése
main.py – a játék teljes logikája (szó kiválasztás, tippelés, hibák kezelése, akasztófa rajzolás).

szavak.txt – a szólista, amelyből a játék véletlenszerűen választ.

👤 Készítette
mekercs
