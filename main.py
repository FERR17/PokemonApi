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
    "3":"Loki",
    "4":"Black Widow",
    "5":"What If...?",
    "6":"Shang-Chi And The Legend Of The Ten Rings",
    "7":"Eternals",
    "8":"Hawkeye",
    "9":"Spiderman: No Way Home",
    "10":"Moonknight",
    "11":"Doctor Strange: In The Multiverse Of Madness",
    "12":"Ms. Marvel",
    "13":"Thor: Love And Thunder",
    "14":"She-Hulk Attorney At Law",
    "15":"Werewolf By Night",
    "16":"Black Panther Wakanda Forever",
    "17":"Guardians Of The Galaxy Holiday Special",
    "18":"Ant-Man And The Wasp: Quantumania",
    "19":"Guardians Of The Galaxy Vol.3"
         
    }
    return (peliculas[num])

@app.get("/Conversor_CaK/{C}")
def conversorCaK(C):
    try:
            C=float(C)
            TF=C + 273.15
            return f"La temperatura es de {TF} grados Kelvin"
    except:
            return "Entrada invalida"
@app.get("/Marcador/{E1}/{E2}")
def marcador(E1,E2):
    E1=int(E1)
    E2=int(E2)
    if E1>E2:
     return "Ganaste"
    elif E2>E1:
      return "Perdiste"
    else:
      return "Empataste"
@app.get("/Pokemon/{num}")
def pokemon(num):
    pokemons={
    "1":"Bulbasaur",
    "2":"Ivysaur",
    "3":"Venasaur",
    "4":"Charmander",
    "5":"Charmeleon",
    "6":"Charizard"
    }
    return (pokemons[num])
