import random
import turtle

def akasztofagecis(hibaszamlalo):
    wn = turtle.Screen()
    wn.clear()  # Új képernyő minden hibaszámhoz
    t = turtle.Turtle()
    
    t.hideturtle()
    t.speed(0)
    turtle.setup(400, 400)
    if hibaszamlalo >= 1:
        t.left(90)
        t.forward(150)
        t.right(90)
    if hibaszamlalo >= 2:
        t.forward(50)
        t.right(90)
    if hibaszamlalo >= 3:
        t.forward(20)
    if hibaszamlalo >= 4:
        t.penup()
        t.right(90)
        t.forward(10)
        t.left(90)
        t.forward(10)
        t.pendown()
        t.circle(10)
        t.penup()
    if hibaszamlalo >= 5:
        t.forward(10)
        t.left(90)
        t.forward(10)
        t.right(90)
        t.pendown()
        t.forward(20)
    if hibaszamlalo >= 6:
        t.right(40)
        t.forward(20)
        t.backward(20)
        t.left(80)
        t.forward(20)
        t.backward(20)
    if hibaszamlalo >= 7:
        t.right(40)
        t.forward(30)
        t.right(20)
        t.forward(40)
        t.backward(40)
    if hibaszamlalo >= 8:
        t.left(40)
        t.forward(40)
        
        

szavak = []
hely = "szavak.txt"
with open(hely, "r", encoding="utf-8") as fajl:
    for sor in fajl:
        szavak.append(sor.strip().lower())

szavak = random.choice(szavak)
talalt_betuk = []
nemtalalt_betuk = []
hibaszamlalo = 0

while hibaszamlalo < 8:
    segitseg = " ".join([betu if betu in talalt_betuk else "_" for betu in szavak])
    print(segitseg)

    if "_" not in segitseg:
        print("GG ez go next")
        break

    tipp = input("mondj egy betűt: ").lower()

    if len(tipp) == 1:
        if tipp in szavak:
            talalt_betuk.append(tipp)
        else:
            if tipp not in nemtalalt_betuk:
                hibaszamlalo += 1
                nemtalalt_betuk.append(tipp)
                akasztofagecis(hibaszamlalo)
            print("Nem nyert")
    else:
        if tipp == szavak:
            print("GG ez go next")
            break
        else:
            hibaszamlalo = 8
            akasztofagecis(hibaszamlalo)
            print("noob")
            break

if hibaszamlalo == 8:
    print("jó szar vagy a szó:", szavak)
