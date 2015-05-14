# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.

# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
# eg. image eileen happy = "eileen_happy.png"

image eg entrada = "poster.jpg"
image eg imagetwo = "gar_odie.jpg"
image eg imagetres = "gar_jon.jpg"
image eg dormir = "durmiendo.jpg"
image eg intro = "intro.jpg"
image eg montaña1 = "everest.jpg"
image eg fallaste = "fallaste.jpg"
image eg victory = "victory.jpg"
image eg odie2 = "odie2.jpg"
image eg ganaste1 = "ganaste1.jpg"
image eg mapa = "mapamundi.jpg"
image eg lago1 = "lago1.jpg"
image eg Jon2 = "grama.jpg"
image eg Jon3 = "playa.jpg"
image eg planetas = "planetas.jpg"
image eg america = "america.jpg"
image eg cataratas = "cataratas.jpg"
image eg mozart = "mozart.jpg"
image eg canal = "canal.jpg"
image eg desierto = "desierto.jpg"
image eg nilo = "nilo.jpg"
image eg final = "garfield_amigos.jpg"

image odie = "odie.png"
image Jon = "Jon2.png"


# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el 
#   ejemplo.
define e = Character('Garfield', color="#c8ffc8")
define o = Character('Odie', color="#c8ffc8")
define j = Character('Jon Arbuckle', color="#c8ffc8")

# The game starts here.
# - El juego comienza aquí.
label start:
    play music "LoveAndBeLoved.ogg"
    scene eg entrada
    with fade
    e "Hola soy Garfield, soy un gato muy ocupado y
       me he tomado un poco de tiempo para descansar."
    e "Te presentare a unos amigos..."
    
    
    scene eg imagetwo
    with fade
    e "El es Odie; es un adorable perro, le gusta morder la alfombra y destruir
       los libros de Jon..."
    e "A proposito donde está Jon..."
    
    
    scene eg imagetres
    with fade
    e "El es Jon Arbuckle, es mi amo y yo soy su mascota.
       No es tan listo como yo, pero prepara las mejores lasañas..."
    e "Pero en esta ocación no hablaremos de comida..."
    
    
    scene eg dormir
    with fade
    e "En mi escaso tiempo libre me he dedicado a estudiar mucho sobre geografia, algunos
       lugares importantes y sobre algunos personajes que han marcado la historia..."
    
    scene eg intro
    with fade
    e "Muy bien, todo consiste en una serie de diez pregunats sobre cualquier cosa que 
       existe o sobre cualquier hecho importante que marcó la historia..."
    
    scene eg montaña1
    with fade
    e "1- ¿Cual es la altura de el monte Everest?"
    
    menu:
        "a) 9,900 metros":
            jump perdiste
        "b) 7,553 metros":
            jump perdiste
        "c) 8,848 metros":
            jump acertado
        "d) 8,957 metros":
            jump perdiste
            
label perdiste:
    scene eg fallaste
    with fade
    e "Has elegido la opcion incorrecta..."
    e "Has perdido el juego..."
    e "Tu calificacion es de 0 por ciento"
    return
    
label acertado:
    scene eg victory
    e "Has acertado..."
    e "Muy bien tu proxima pregunta es..."
    
    scene eg mapa
    show odie at right
    o "2- ¿Cual es el país mas poblado del mundo?"
    hide odie
    
    menu:
        "a) Francia":
            jump perdiste1
        "b) Estados Unidos":
            jump perdiste1
        "c) Brasil":
            jump perdiste1
        "d) China":
            jump acertado1
            
label perdiste1:
    scene eg odie2
    with fade
    o "Has elegido la opcion incorrecta..."
    o "Has perdido el juego..."
    o "Tu calificacion es de 10 por ciento"
    return
    
label acertado1:
    scene eg ganaste1
    with fade
    o "Has acertado..."
    o "Muy bien tu proxima pregunta es..."
    
    scene eg lago1
    show Jon at right
    j "3- ¿Donde se ubica el lago Titicaca?"
    hide Jon
    
    menu:
        "a) Entre Bolivia y Brasil":
            jump perdiste2
        "b) Entre Peru y Bolivia":
            jump acertado2
        "c) Entre Brasil y Colombia":
            jump perdiste2
            
label perdiste2:
    scene eg Jon2
    with fade
    j "Has elegido la opcion incorrecta..."
    j "Has perdido el juego..."
    j "Tu calificacion es de 20 por ciento"
    return
    
label acertado2:
    scene eg Jon3
    with fade
    j "Has acertado..."
    j "Muy bien tu proxima pregunta es..."
    
    scene eg planetas
    show Jon at right
    j "4- ¿Venus es el planeta más cercano a La Tierra?"
    hide Jon
    
    menu:
        "Verdadero":
            jump acertado3
        "Falso":
            jump perdiste3
            
label perdiste3:
    scene eg Jon2
    with fade
    j "Has elegido la opcion incorrecta..."
    j "Has perdido el juego..."
    j "Tu calificacion es de 30 por ciento"
    return
    
label acertado3:
    scene eg Jon3
    with fade
    j "Has acertado..."
    j "Muy bien tu proxima pregunta es..."
    
    scene eg america
    with fade
    e "5- ¿En que año se descubrió America?"
    
    menu:
        "En el año de 1502":
            jump perdiste4
        "En el año de 1510":
            jump perdiste4
        "En el año de 1492":
            jump acertado4
            
label perdiste4:
    scene eg fallaste
    with fade
    e "Has elegido la opcion incorrecta..."
    e "Has perdido el juego..."
    e "Tu calificacion es de 40 por ciento"
    return
    
label acertado4:
    scene eg victory
    e "Has acertado..."
    e "Muy bien tu proxima pregunta es..."
    
    scene eg cataratas
    with fade
    o "6- ¿Las cataratas del Niagara se ubican en el norte de Alemania?"
    
    menu:
        "Verdadero":
            jump perdiste5
        "Falso":
            jump acertado5
            
label perdiste5:
    scene eg odie2
    with fade
    o "Has elegido la opcion incorrecta..."
    o "Has perdido el juego..."
    o "Tu calificacion es de 50 por ciento"
    return
    
label acertado5:
    scene eg ganaste1
    with fade
    o "Has acertado..."
    o "Muy bien tu proxima pregunta es..."
    
    scene eg mozart
    with fade
    j "7- ¿Mozart fué un _____________?"
    
    menu:
        "Filósofo":
            jump perdiste6
        "Músico":
            jump acertado6
        "Pintor":
            jump perdiste6
        "Principe de Edimburgo":
            jump perdiste6
            
label perdiste6:
    scene eg Jon2
    with fade
    j "Has elegido la opcion incorrecta..."
    j "Has perdido el juego..."
    j "Tu calificacion es de 60 por ciento"
    return
    
label acertado6:
    scene eg Jon3
    with fade
    j "Has acertado..."
    j "Muy bien tu proxima pregunta es..."
    
    scene eg canal
    with fade
    e "8- ¿El canal de Panamá se inaguró el año de 1914?"
    
    menu:
        "Verdadero":
            jump acertado7
        "Falso":
            jump perdiste7
            
label perdiste7:
    scene eg fallaste
    with fade
    e "Has elegido la opcion incorrecta..."
    e "Has perdido el juego..."
    e "Tu calificacion es de 70 por ciento"
    return
    
label acertado7:
    scene eg victory
    e "Has acertado..."
    e "Muy bien tu proxima pregunta es..."
    
    scene eg desierto
    with fade
    o "9- ¿Cuál es el desierto mas extenso del mundo?"
    
    menu:
        "Desierto de Siria":
            jump perdiste8
        "Desierto del Sahara":
            jump acertado8
        "Desierto de Gobi":
            jump perdiste8
            
label perdiste8:
    scene eg odie2
    with fade
    o "Has elegido la opcion incorrecta..."
    o "Has perdido el juego..."
    o "Tu calificacion es de 80 por ciento"
    return
    
label acertado8:
    scene eg ganaste1
    with fade
    o "Has acertado..."
    o "Muy bien tu proxima pregunta es..."
    
    scene eg nilo
    with fade
    j "10- ¿El río Nilo se extiende por toda la selva Amazónica?"
    
    menu:
        "Verdadero":
            jump perdiste9
        "Falso":
            jump acertado9
            
label perdiste9:
    scene eg Jon2
    with fade
    j "Has elegido la opcion incorrecta..."
    j "Has perdido el juego..."
    j "Tu calificacion es de 90 por ciento"
    return
    
label acertado9:
    scene eg Jon3
    with fade
    j "Has acertado..."
    j "Tu calificacion es de 100 por ciento"
    scene eg final
    "FELICIDADES HAZ CONTESTADO TODAS NUESTRAS PREGUNTAS"
    return
