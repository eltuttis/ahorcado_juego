import random
#inutiles, pero necesarias
#utiles
b=[]
letras_ingresadas=[]
vida=[]
interfaz=[]
palabras_ingresadas=[]

animales = ['perro', 'gato', 'conejo', 'raton', 'tigre', 'elefante', 'jirafa', 'leon', 'pantera', 'cebra', 'hipopotamo', 'mono', 'oso', 'aguila', 'cocodrilo', 'serpiente', 'tortuga', 'pinguino', 'ballena', 'delfin']
comidas = ['pizza', 'hamburguesa', 'tacos', 'sushi', 'pollo frito', 'ensalada', 'pasta', 'arroz con pollo', 'costillas', 'ceviche', 'paella', 'lasaña', 'cordero asado', 'parrillada', 'ramen', 'curry', 'guacamole', 'arepas', 'empanadas', 'quesadillas']
paises = ['estados unidos', 'canada', 'mexico', 'brasil', 'argentina', 'francia', 'espana', 'italia', 'alemania', 'reino unido', 'japon', 'china', 'india', 'australia', 'nueva zelanda', 'sudafrica', 'egipto', 'nigeria', 'kenia', 'rusia']
objetos = ['telefono', 'computadora', 'televisor', 'refrigerador', 'lavadora', 'secadora', 'horno microondas', 'tostadora', 'licuadora', 'aspiradora', 'cepillo de dientes', 'espejo', 'llaves', 'paraguas', 'libreta', 'boligrafo', 'lapiz', 'tijeras', 'cinta adhesiva', 'caja de herramientas']

def escogedor_palabra(categoria):
    if categoria ==1:
        palabra_categoria= animales[random.randrange(len(animales))]
    elif categoria ==2:
        palabra_categoria= comidas[random.randrange(len(comidas))]
    elif categoria ==3:
        palabra_categoria= paises[random.randrange(len(paises))]
    elif categoria ==4:
        palabra_categoria= objetos[random.randrange(len(objetos))]
    funcionamiento(palabra_categoria)
           
# escogedor_palabra={
#     "animales": animales[random.randrange(len(animales))],
#     "comidas": comidas[random.randrange(len(comidas))],
#     "paises": paises[random.randrange(len(paises))],
#     "objetos": objetos[random.randrange(len(objetos))]
# }
def salir():
     print("gracias por jugar")
def inicio():
        print("Menú\n 1. Jugar\n 2. Como Jugar\n 3. Cerrar")
        r=int(input("Introduzca un número: "))
        if r==1:
            dificultad_categoria()
        elif r==2:
            como_jugar()
        elif r==3:
             salir()
def dificultad_categoria():
    print("Dificultades\n 1. Facil\n 2. Medio\n 3. Dificil\n 4. Master")
    p =int(input("ingrese dificultad: "))
    if p ==1:
        g=0
        for f in range(9):
            vida.append("♥")
    elif p==2:
        g=2
        for f in range(7):
            vida.append("♥")
    elif p==3:
        g=4
        for f in range(5):
            vida.append("♥")
    elif p==4:
        g=6
        for f in range(3):
            vida.append("♥")
    print("Categorias\n 1. animales\n 2. comidas\n 3. paises\n 4. objetos")
    escogedor_palabra(int(input("ingrese una categoria: ")))
    print(" ".join(vida))       
    
def como_jugar():
    print("El juego consta principalmente de unas categorias y unos niveles de Dificultad, irás colocando letras hasta completar la palabra sin que se te acaben las vidas, cuando se te acaben las vidas será un GameOver")
    inicio()
def vidas():
    vida.pop()    
    print(" ".join(vida))
def funcionamiento(j):
    count2=0
    poner_quitar_letras = list(j)
    palabra= list(j) 
    while count2 != len(poner_quitar_letras):
            interfaz.append("_")
            count2+=1
    print(" ".join(interfaz))
    while palabra != interfaz and vida!=b:
        ingreso_de_letra=input("ingrese una letra: ")
        count=0
        if interfaz.count(ingreso_de_letra) > 0:
            print("esta letra ya está aguebado")
        else:
            for cosa in range(poner_quitar_letras.count(ingreso_de_letra)):
                count+=1
                poner_quitar_letras.insert(poner_quitar_letras.index(ingreso_de_letra),"-")
                interfaz.insert(poner_quitar_letras.index(ingreso_de_letra)-1,ingreso_de_letra)
                interfaz.pop(poner_quitar_letras.index(ingreso_de_letra))
                poner_quitar_letras.pop(poner_quitar_letras.index(ingreso_de_letra))
            letras_ingresadas.append(ingreso_de_letra)
        if count == 0:
            vidas()
            g = g+1
            grafica(g)    
            return g

        print(" ".join(interfaz))
        print("letras ya ingresadas:"," ,".join(letras_ingresadas))
    print("la palabra era:","".join(palabra))
    interfaz.clear()
    vida.clear()
    letras_ingresadas.clear()
    inicio()
def grafica(g):
    if g ==1:
        print(("─"*2)+"┴"+("─"*2))
    elif g==2:
        print(" ","│")
        print(" ","│")
        print(" ","│")
        print(" ","│")
        print(" ","│")
        print(" ","│")
        print(" ","│")
        print(" ","│")
        print(" ","│")
        print(("─"*2)+"┴"+("─"*2))
    elif g==3:
        print(" ","┌",("─"*5),"┐")
        print(" ","│")
        print(" ","│")
        print(" ","│")
        print(" ","│")
        print(" ","│")
        print(" ","│")
        print(" ","│")
        print(" ","│")
        print(" ","│")
        print(("─"*2)+"┴"+("─"*2))
    elif g==4:
        print(" ","┌",("─"*5),"┐")
        print(" ","│"," "*3,"┌","┴","┐")
        print(" ","│"," "*3,"│"," ","│")
        print(" ","│"," "*3,"└","┬","┘")
        print(" ","│")
        print(" ","│")
        print(" ","│")
        print(" ","│")
        print(" ","│")
        print(" ","│")
        print(("─"*2)+"┴"+("─"*2))
    elif g==5:
        print(" ","┌",("─"*5),"┐")
        print(" ","│"," "*3,"┌","┴","┐")
        print(" ","│"," "*3,"│"," ","│")
        print(" ","│"," "*3,"└","┬","┘")
        print(" ","│",(" "*5),"│")
        print(" ","│",(" "*5),"┼")
        print(" ","│",(" "*5),"│")
        print(" ","│",(" "*5),"┴")
        print(" ","│")
        print(" ","│")
        print(("─"*2)+"┴"+("─"*2))
    elif g==6:
        print(" ","┌",("─"*5),"┐")
        print(" ","│"," "*3,"┌","┴","┐")
        print(" ","│"," "*3,"│"," ","│")
        print(" ","│"," "*3,"└","┬","┘")
        print(" ","│",(" "*5),"│")
        print(" ","│",(" "*3),"┌","┼")
        print(" ","│",(" "*5),"│")
        print(" ","│",(" "*5),"┴")
        print(" ","│")
        print(" ","│")
        print(("─"*2)+"┴"+("─"*2))
    elif g==7:
        print(" ","┌",("─"*5),"┐")
        print(" ","│"," "*3,"┌","┴","┐")
        print(" ","│"," "*3,"│"," ","│")
        print(" ","│"," "*3,"└","┬","┘")
        print(" ","│",(" "*5),"│")
        print(" ","│",(" "*3),"┌","┼","┐")
        print(" ","│",(" "*5),"│")
        print(" ","│",(" "*5),"┴")
        print(" ","│")
        print(" ","│")
        print(("─"*2)+"┴"+("─"*2))
    elif g==8:
        print(" ","┌",("─"*5),"┐")
        print(" ","│"," "*3,"┌","┴","┐")
        print(" ","│"," "*3,"│"," ","│")
        print(" ","│"," "*3,"└","┬","┘")
        print(" ","│",(" "*5),"│")
        print(" ","│",(" "*3),"┌","┼","┐")
        print(" ","│",(" "*5),"│")
        print(" ","│",(" "*3),"┌","┴")
        print(" ","│",(" "*3),"│")
        print(" ","│",(" "*3),"┘")
        print(("─"*2)+"┴"+("─"*2))
    elif g==9:
        print(" ","┌",("─"*5),"┐")
        print(" ","│"," "*3,"┌","┴","┐")
        print(" ","│"," "*3,"│"," ","│")
        print(" ","│"," "*3,"└","┬","┘")
        print(" ","│",(" "*5),"│")
        print(" ","│",(" "*3),"┌","┼","┐")
        print(" ","│",(" "*5),"│")
        print(" ","│",(" "*3),"┌","┴","┐")
        print(" ","│",(" "*3),"│"," ","│")
        print(" ","│",(" "*3),"┘"," ","└")
        print(("─"*2)+"┴"+("─"*2))
inicio()