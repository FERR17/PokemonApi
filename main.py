from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def index():
     return "Hola a todos, quieres saber de pokemon"

@app.get("/MCU/Phase1/{num}")
def MCU(num):
    peliculas={
    "1":"Iron Man",
    "2":"The Incredible Hulk",
    "3":"Iron Man 2",
    "4":"Thor",
    "5":"Captain America: The First Avenger",
    "6":"The Avengers"
         
    }
    return (peliculas[num])

@app.get("/MCU/Phase2/{num}")
def MCU(num):
    peliculas={
    "1":"Iron Man 3",
    "2":"Thor The Dark World",
    "3":"Captain America: The Winter Soldier",
    "4":"Guardians Of The Galaxy",
    "5":"The Avengers: Age Of Ultron",
    "6":"Ant-Man"
         
    }
    return (peliculas[num])

@app.get("/MCU/Phase3/{num}")
def MCU(num):
    peliculas={
    "1":"Captain America: Civil War",
    "2":"Doctor Strange",
    "3":"Guardians Of The Galaxy Vol.2",
    "4":"Spiderman: Homecoming",
    "5":"Thor Ragnarok",
    "6":"Black Panther",
    "7":"Avengers: Infinity War",
    "8":"Ant_Man And The Wasp",
    "9":"Captain Marvel",
    "10":"Avengers Engame",
    "11":"Spiderman: Far From Home"
         
    }
    return (peliculas[num])

@app.get("/MCU/Phase4/{num}")
def MCU(num):
    peliculas={
    "1":"WandaVision",
    "2":"Falcon And The Winter Soldier",
    "3":"Black Widow",
    "4":"What If...?",
    "5":"Shang-Chi And The Legend Of The Ten Rings",
    "6":"Eternals",
    "7":"Hawkeye",
    "8":"Spiderman: No Way Home",
    "9":"Moonknight",
    "10":"Doctor Strange: In The Multiverse Of Madness",
    "11":"Ms. Marvel",
    "12":"Thor: Love And Thunder",
    "13":"She-Hulk Attorney At Law",
    "14":"Werewolf By Night",
    "15":"Black Panther Wakanda Forever",
    "16":"Guardians Of The Galaxy Holiday Special",
    "17":"Ant-Man And The Wasp: Quantumania",
    "18":"Guardians Of The Galaxy Vol.3"
         
    }
    return (peliculas[num])

@app.get("/Conversor_CaF/{C}")
def conversorCaF(C):
    try:
            C=float(C)
            TF=C*(9/5) + 32
            return f"La temperatura es de {TF} grados Farenheit"
    except:
            return "Entrada invalida"
@app.get("/RevisarEdad/{E1}/{E2}")
def revisar_edades(E1,E2):
    E1=int(E1)
    E2=int(E2)
    if E1>E2+30:
     return "Podria ser su abuelo"
    elif E1>E2+15:
     return "Podrias ser su padre"
    elif E1>E2:
     return "Eres mayor"
    elif E2>E1+30:
     return "Podria ser tu abuelo"
    elif E2>E1+15:
     return "Podria ser tu padre"
    elif E2>E1:
     return "Es mayor que tu"
    else:
     return "Tienen la misma edad"
