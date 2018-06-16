from tkinter import *               # Tk(), Label, Canvas, Photo
from threading import Thread        # p.start()
import threading                    # 
import winsound                     # Playsound
import os                           # ruta = os.path.join('')                       # time.sleep(x)
from tkinter import messagebox # AskYesNo ()
from random import *                # randint()
import pygame
from pygame.locals import *
from time import *
import serial

#______________/Sección de funciones a usar a lo largo del programa
def cargarImg(nombre): # carga una imagen de la carpeta adyacente al archivo img a una variable
    ruta=os.path.join('img',nombre)
    imagen=PhotoImage(file=ruta)
    return imagen

def inn(el,li): # devuelve True si "el" se haya en "li", similar a la keyword "in"
    if li==[]:
        return False
    if el==li[0]:
        return True
    return inn(el,li[1:])

def innli(li1,li2): #aplica el "inn" a todos los elementos de ambas listas
    if li1==[]:
        return False
    if inn(li1[0],li2):
        return True
    else:
        return innli(li1[1:],li2)
        
def lenn(li): #len
    if li==[] or li=="":
        return 0
    return 1+lenn(li[1:])

#______________/Sección de manejo de archivos\______________

#_________________/Generar lista aleatoria de jugadores
def escribir_1(arch):
    from random import randint
    file=open(arch,"w")

    def gen(lon,res):
        v="aaeeuio"
        c="qwrrtypssdfghjklzxcvbnm"
        punt_max=20
        if lon==0 or lon==1:
            i=randint(0,punt_max)
            return res.capitalize()+","+str(i)
        else:
            i=randint(0,len(c)-1)
            j=randint(0,len(v)-1)
            return gen(lon-2,res+c[i]+v[j])

    def gen_mult(cant,res):
        if cant==0:
            return res
        else:
            i=randint(2,8)
            return gen_mult(cant-1,res+gen(i,"")+"\n")

    nom=gen_mult(19,"")
    file.write(nom)
    file.close()

#_________________/Leer lista de jugadores

def leer(arch):
    file=open(arch,"r")

    def agrupar(file):
        c=0
        l=[]
        while(c!=""):
            c=file.readline()
            c=c[:-1]
            l+=[c]
        l.pop(-1)
        return l

    def trad(st):
        t=["",0]
        for i in range(len(st)):
            if st[i]==",":
                t[1]=int(st[i+1:])
                break
            else:
                t[0]+=st[i]
        return tuple(t)

    l=[]
    for i in agrupar(file):
        l+=[trad(i)]

    file.close()
    return l

#_________________/Mostrar lista de jugadores
def imprimir(nom,datos,i): #mostrar en columnas
    if i==len(leer(nom)):
        return dic_trad[21]+datos
    temp=str(leer(nom)[i][1])
    if len(leer(nom)[i][0])>7:
        temp=leer(nom)[i][0]+"\t"+temp
    else:
        temp=leer(nom)[i][0]+"\t\t"+temp
        datos+=(temp+"\n")
    return imprimir(nom,datos,i+1)


def asignar(li): #toma la lista de jugadores aleatorios y les asignauna puntuacion aleatoria
    temp=[]
    for i in li:
        temp+=[(i[0],randint(0,10)*25)]
    return temp



#_________________/Ordenar lista de jugadores
def ordenar(li): #ordenamiento de la lsita de jugadores a través de quick sort
    li1=li+[]
    def quicksort(L, first, last,i,j,pivote):
        if i <=j:
            if L[i][1] < pivote:
                return quicksort(L, first, last,i+1,j,pivote)
            if L[j][1] > pivote:
                return quicksort(L, first, last,i,j-1,pivote)
            if i <= j:
                L[i],L[j]=L[j],L[i]
                i+=1
                j-=1
                return quicksort(L, first, last,i,j,pivote)
        if first < j:
            return quicksort(L, first, last,first,j,(L[first][1]+L[j][1])/2)
        if last > i:
            return quicksort(L, i, last,i,last,(L[i][1]+L[last][1])/2)
        return L

    return quicksort(li1, 0, len(li1)-1,0,len(li1)-1,(li1[0][1]+li1[-1][1])/2)
def ordenar2(): #ordena una lista entera leida de un archiv detexto y lo sobreescribe
    a=leer("Jug.txt")
    if a==[]:
        return
    a=ordenar(a)
    b=""
    for i in range(1,6):
        b+=(a[-i][0]+","+str(a[-i][1])+"\n")
    file=open("Jug.txt","w")
    file.write(b)





#______________/Sección de funciones de música y sonidos
def off():
    winsound.PlaySound(None, winsound.SND_ASYNC)

    
def play1():
    off()
    def Song1():
        winsound.PlaySound('song1.wav', winsound.SND_ASYNC)
    ''''imagen = cargarImg("img1.gif")
    imagenc.config(image=imagen)'''
    p1=Thread(target=Song1,args=())
    p1.start()
    root.mainloop()

def play2():
    off()
    def Song2():
        winsound.PlaySound('song2.wav', winsound.SND_ASYNC)
    '''imagen2 = cargarImg("img2.gif")
    imagenc.config(image=imagen2)'''
    p2=Thread(target=Song2,args=())
    p2.start()
    root.mainloop()



#______________/Sección de variables predefinidas con uso en todo el programa
global vent #indicador de ventana
vent=0

global i_back #indicador de backear
i_back=False

global dft
dft="1" #1: asteroides 0:aros

global i_per #índice de los personajes
i_per=0

global li_per #lista de personajes
li_per=[('Ba', 0), ('Gibo', 0), ('Cukigi', 0), ('Hu', 0), ('Heva', 0), 
('Pera', 0),('Lovedum', 0), ('Ku', 0), ('Pedazoja', 0), ('We', 0),
('Ri', 0), ('Saroyat', 0),('Vulipas', 0), ('Xu', 0), ('Kimuje', 0), 
('Qu', 0), ('Seye', 0), ('Surupe', 0),('Xi', 0),('Notlim',0)] #lista predefinida de jugadores


#______________/Sección de idomas

global dic_trad,dic_trad_es,dic_trad_en

dic_trad_es=["Ventana principal","Introduzca el nombre \n (máx 10 caracteres)","Puntuaciones",'Atrás',"Juego",
             "Balas restantes: ","Enemigos restantes: ","arriba: w \nabajo: s \nizquierda: a \nderecha: d \n disparo: espaciadora",
             "Nombre debe ser menor de 10 caracteres","Introduzca nombre","Jugador: ","Opciones","Puntaje máximo: ",
             "Nivel ","Mapa ","Aleatorio", "Reiniciar puntuaciones","Clave","Clave érronea","Reiniciar puntajes (requiere clave)","Dificultad",
             "Nombre\t\tPts\tDificultad\tFecha\n", "Juego de Naves", "Puntuación alcanzada= ","Canción ","Parar","""******************************************************************
Instituto: Tecnológico de Costa Rica
Carrera :Ing. Computadores 
Curso: Introducción a la programación
País de Producción: Costa Rica
Profesor: Milton Villegas Lemus
Como implementar: Se invoca con F5 desde el Idle del código
Programa: II Proyecto
Autores: Juan Pablo Alvarado Villalobos, Sebastián Calderón, Julian Aguilera
Carné: 2018135360,2018161630,2018135658
Lenguaje: Python 3.6
Versión: 6.1
Ult.Fecha de mod: 3/6/18
******************************************************************""","Hacer clic en la pantalla para usar el teclado",
"Elegir modo de juego\nAros/Enemigos", "Puntaje: ", "Energía: "]

dic_trad_en=["Main window","Enter the name \n (max 10 characters)","Scores",'Back',"Game",
             "Remaining bullets: ", "Remaining enemies: ", " up: w \n down: s \n left: a \n right: d \n shot: space",
             "Name must be less than 10 characters", "Enter name", "Player: ", "Settings","Highscore: ",
             "Level ","Map ","Random","Restart scores","Key","Wrong key","Restart scores (requires password)","Difficulty",
             "Name\t\tPts\tDifficulty\t\tDate\n", "Game of Space", "Score reached= ","Song ","Stop", """******************************************************************
Institute: Tecnológico de Costa Rica
Career :Ing. Computadores 
Course: Introducción a la programación
Country of Production: Costa Rica
Teacher: Milton Villegas Lemus
How to implement: It is invoked with F5 from the Idle of the code
Program: II Proyecto
Authors: Juan Pablo Alvarado Villalobos, Sebastián Calderón, Julian Aguilera
Cardé: 2018135360,2018161630,2018135658
Language: Python 3.6
Version: 6.1
Last modified date: 3/6/18
******************************************************************""","Click on the screen to use the keyboard",
"Choose game mode\nHoops / Enemies", "Score: ","Energy: "]


dic_trad=dic_trad_en #lista con todas las palabras que se leerá en todo el programa

def inter(): #función para intercambiar los idiomas
    """
******************************************************************
Instituto: Tecnológico de Costa Rica
Carrera :Ing. Computadores 
Curso: Intro a la programación
Como implementar: se invoca con inter()
Módulo : intercambio de idiomas
Autores : Juan Pablo Alvarado, Sebastián Calderón, Julian
Lenguaje: Python 3.6
Version : 1.0
Ult.Fecha de mod: 3/6/18
Entradas : ninguna
Restricciones: ninguna
Salidas: ninguna
******************************************************************"""

    global dic_trad,dic_trad_en
    if dic_trad[0]=="Ventana principal":
        dic=dic_trad_en
        Btn4.config(text="Español")
        img_auxes=cargarImg("us.gif")
        Btn4.image=(img_auxes)
        Btn4.config(image=img_auxes)
    else:
        dic=dic_trad_es
        Btn4.config(text="English")
        img_auxen=cargarImg("mex.gif")
        Btn4.image=(img_auxen)
        Btn4.config(image=img_auxen)
        
    dic_trad=dic

    #Ajusta los labelsde la pantalla principal
    L_vr.config(text=dic[1])
    L_vr1.config(text=dic[22])
    root.title(dic[0])
    Btn1.config(text=dic[2])
    Btn3.config(text=dic[4])
    Btn6.config(text=dic[11])
    Btn_song1.config(text=dic[24]+'1')
    Btn_song2.config(text=dic[24]+'2')
    Btn_song0.config(text=dic_trad[25])

print(len(dic_trad))




ordenar2() #se ajustan las puntuaciones desde el inico

#______________/Sección de ventana principal
#Se define la ventana principal=>
root=Tk()
root.title(dic_trad[0])
root.geometry("800x600+100+50")
root.minsize(800,600)
root.resizable(NO,NO)
root.title()


C_root=Canvas(root,width=800,height=600,bg="grey")
C_root.place(x=0,y=0)
CE0=cargarImg("fon.gif")
C_root.create_image(400,300,image=CE0)

#______________/Subsección de imágenes
CE1=cargarImg("fonp.gif")
CE2=cargarImg("foni.gif")
CE3=cargarImg("fons.gif")
CE4=cargarImg("fon_sel.gif")


L_vr1=Label(C_root,text=dic_trad[22],bg="grey",fg="black",font=('Eras Bold ITC',32))
L_vr1.place(x=50,y=10)

CE=cargarImg("A.gif")
imagen_cancion=Label(C_root,bg='white')
imagen_cancion.place(x=80,y=100)
imagen_cancion.config(image=CE)


L_vr=Label(C_root,text=dic_trad[1],bg="grey",fg="black",font=('Eras Bold ITC',14))
L_vr.place(x=500,y=350)


E_nombre=Entry(C_root,width=20,font=('Eras Bold ITC',16))
E_nombre.place(x=500,y=400)

Btn_song1 = Button(C_root,text=dic_trad[24]+'1',command=play1,bg='green',fg='white',font=('Eras Bold ITC',12))
Btn_song1.place(x=100,y=550)


Btn_song2=Button(C_root,text=dic_trad[24]+'2',command=play2,bg='green',fg='white',font=('Eras Bold ITC',12))
Btn_song2.place(x=200,y=550)

Btn_song0=Button(C_root,text=dic_trad[25],command=off,bg='green',fg='white',font=('Eras Bold ITC',12))
Btn_song0.place(x=300,y=550)




#______________/Sección de ventana de puntuaciones
def Ventana1():
    global vent
    vent=3 #ventana 2 o 1

    datos=imprimir("Jug.txt","",0)
    
    root.withdraw()
    v1=Toplevel(root)
    v1.title(dic_trad[2])
    v1.geometry("800x600+100+50")
    v1.minsize(800,600)
    v1.resizable(NO,NO)

    C_v1=Canvas(v1,width=800,height=600,bg="black")
    C_v1.place(x=0,y=0)
    C_v1.create_image(400,300,image=CE1)

    fondoImg=cargarImg('top.gif')
    F_v1=Label(C_v1, image=fondoImg,bg='black')
    F_v1.photo=fondoImg
    F_v1.place(x=200,y=20)

    L_v1=Label(v1,text=datos,bg="black",fg="white",font=('Eras Bold ITC',14),justify=LEFT)
    L_v1.place(x=50,y=200)

    def reiniciar():
        """
******************************************************************
Instituto: Tecnológico de Costa Rica
Carrera :Ing. Computadores 
Curso: Intro a la programación
Como implementar: se invoca con reiniciar()
Módulo : reiniciar puntuaciones
Autores : Juan Pablo Alvarado, Sebastián Calderón, Julian
Lenguaje: Python 3.6
Version : 1.0
Ult.Fecha de mod: 3/6/18
Entradas : ninguna
Restricciones: ninguna
Salidas: ninguna
******************************************************************"""
        clave=str(E_clave.get())
        if clave!="luca":
            messagebox.showinfo(":(",dic_trad[18])
            return
        file=open("Jug.txt","w") #archivo de puntuaciones
        file.write("")
        file.close()
        ordenar2()
        
        datos=imprimir("Jug.txt","",0)
        
        L_v1.configure(text=datos)
        
    L_v1r=Label(v1,text=dic_trad[19],bg="grey",fg="black",font=('Eras Bold ITC',12),justify=LEFT)
    L_v1r.place(x=100,y=500)
    E_clave=Entry(C_v1,width=20,font=('Eras Bold ITC',12))
    E_clave.place(x=100,y=530)
    Btn_res = Button(C_v1,text=dic_trad[16],command=reiniciar,bg='grey',fg='black',font=('Eras Bold ITC',12))
    Btn_res.place(x=100,y=560)
    
    def back():
        global vent
        vent=0
        v1.destroy()
        root.deiconify()

    home=cargarImg("home.gif")
    Btn_back1 = Button(C_v1, image=home ,command=back, fg = "#000000")
    Btn_back1.image = home
    Btn_back1.place(x=650,y=500)

    def rev_back():
        global i_back
        if i_back==True:
            i_back=False
            back()
            return
        sleep(.1)
        return rev_back()

    Hilo_back=Thread(target=rev_back,args=()) #hilo
    Hilo_back.start()

#______________/Sección de ventana de about
def Ventana2():
    global vent
    vent=3 #ventana 2 o 1

    root.withdraw()
    v2=Toplevel(root)
    v2.title("About")
    v2.geometry("800x600+100+50")
    v2.minsize(800,600)
    v2.resizable(NO,NO)
    
    C_v2=Canvas(v2,width=800,height=600,bg="light green")
    C_v2.place(x=0,y=0)
    C_v2.create_image(400,300,image=CE2)
    
    tex=dic_trad[26]

    L_v2=Label(v2,text=tex,bg="white",fg="#000000",font=('Eras Bold ITC',12),justify=CENTER)
    L_v2.place(x=130,y=20)

    fondoImg=cargarImg('tec.gif')
    F_v2=Label(C_v2, image=fondoImg,bg='#000000')
    F_v2.photo=fondoImg
    F_v2.place(x=400,y=300)

    fondoImg1=cargarImg('per.gif')
    F_v21=Label(C_v2, image=fondoImg1,bg='#000000')
    F_v21.photo=fondoImg1
    F_v21.place(x=150,y=300)
    
    def back():
        global vent
        vent=0
        v2.destroy()
        root.deiconify()

    home=cargarImg("home.gif")
    Btn_back1 = Button(C_v2, image=home ,command=back, fg = "#000000")
    Btn_back1.image = home
    Btn_back1.place(x=700,y=500)

    def rev_back():
        global i_back
        if i_back==True:
            i_back=False
            back()
            return
        sleep(.1)
        return rev_back()

    Hilo_back=Thread(target=rev_back,args=()) #hilo
    Hilo_back.start()

#______________/Sección de ventana de configuración
def Ventana3():
    global vent
    vent=1
    root.withdraw()
    v3=Toplevel(root)
    v3.title(dic_trad[11])
    v3.geometry("800x600+100+50")
    v3.minsize(800,600)
    v3.resizable(NO,NO)

    C_v3=Canvas(v3,width=800,height=600,bg="black")
    C_v3.place(x=0,y=0)
    C_v3.create_image(400,300,image=CE3)
    

    
    #______________/Generación de casillas para subsecciones
    C_v31=Canvas(v3,bg="grey", width=200,height=200)
    C_v31.place(x=50,y=50)

    C_v32=Canvas(v3,bg="grey", width=300,height=250)
    C_v32.place(x=400,y=50)

    C_v33=Canvas(v3,bg="grey", width=200,height=200)
    C_v33.place(x=50,y=300)
    
    #______________/Subsección de personajes

    global li_per
    L_nom=[]
    for i in li_per:
        L_nom+=[i[0]]
    L_per=['p1.gif', 'p2.gif', 'p3.gif', 'p4.gif', 'p5.gif',
    'p6.gif', 'p7.gif', 'p8.gif', 'p9.gif', 'p10.gif', 'p11.gif',
    'p12.gif', 'p13.gif', 'p14.gif', 'p15.gif', 'p16.gif',
    'p17.gif', 'p18.gif', 'p19.gif', 'p20.gif']

    def img_der():
        global i_per
        i_per+=1
        i_per=i_per%20
        Silueta=cargarImg(L_per[i_per])
        Sh_cv.configure(image=Silueta)
        Sh_cv.photo=Silueta
        L_vd.configure(text=L_nom[i_per])
    def img_iz():
        global i_per
        i_per-=1
        i_per=i_per%20
        Silueta=cargarImg(L_per[i_per])
        Sh_cv.configure(image=Silueta)
        Sh_cv.photo=Silueta
        L_vd.configure(text=L_nom[i_per])

    def ajustar():
        try:
            sleep(.1)
            v3.title(dic_trad[11])
            global i_per
            Silueta=cargarImg(L_per[i_per])
            Sh_cv.configure(image=Silueta)
            Sh_cv.photo=Silueta
            L_vd.configure(text=L_nom[i_per])
            return ajustar()
        except:
            print("fin hilo")
            pass

    Silueta=cargarImg(L_per[i_per])
    Sh_cv=Label(C_v31, image=Silueta, bg='white')
    Sh_cv.photo=Silueta
    Sh_cv.place(x=50,y=10)

    flchi=cargarImg("flechaizquierda.gif")
    Btn_fi = Button(C_v31, image=flchi , command=img_iz,fg="#000000")
    Btn_fi.image=flchi
    Btn_fi.place(x=10,y=160)

    flchd=cargarImg("flechaderecha.gif")
    Btn_fd = Button(C_v31, image=flchd , command=img_der,fg="#000000")
    Btn_fd.image=flchd
    Btn_fd.place(x=100,y=160)

    L_vd=Label(C_v31,text=L_nom[i_per],bg="grey",fg="black",font=('Eras Bold ITC',20),justify=LEFT)
    L_vd.place(x=50,y=120)
    
        

    def back():
        global vent
        vent=0
        v3.destroy()
        root.deiconify()

        
    home=cargarImg("home.gif")
    Btn_back1 = Button(C_v3, image=home ,command=back, fg = "#000000")
    Btn_back1.image = home
    Btn_back1.place(x=650,y=500)

    Hilo_aux=Thread(target=ajustar,args=()) #hilo
    Hilo_aux.start()

    def rev_back():
        global i_back
        if i_back==True:
            i_back=False
            back()
            return
        sleep(.1)
        return rev_back()

    Hilo_back=Thread(target=rev_back,args=()) #hilo
    Hilo_back.start()

        
    
    
#______________/Sección de ventana de de juego
def VentanaJuego(nombre):
    vj=Toplevel()
    vj.geometry("800x600+100+50")
    vj.minsize(800,600)
    vj.resizable(NO,NO)

    C_vj=Canvas(vj,width=800,height=600,bg="light green")
    C_vj.place(x=0,y=0)
    C_vj.create_image(400,300,image=CE4)

    tex=dic_trad[28]

    L_vj=Label(vj,text=tex,bg="white",fg="#000000",font=('Eras Bold ITC',32),justify=CENTER)
    L_vj.place(x=200,y=20)


    def Juego(dft):
        #           _____________________________
        #__________/Variables globales
        global in1, in2, posX_jug, posY_jug, Energia_c, Count, Puntaje
        in1=1 #indicador para que el aro se sobre ponga a la nave
        posX_jug=300
        posY_jug=300
        Energia_c=100       
        Count=0
        Puntaje=0
        C_display=9

        #           _____________________________
        #__________/Generar y reescalar imagenes
        def gen_img(img,x,y): #Generar cualquier imagen
            root_jueg.blit(img,(x,y))


        #           _____________________________
        #__________/Generar el codigo a leer por el arduino
        def gen_serial(energia,aros):
            st='leds='
            for i in range(6):
                if (100//6)*(5-i)<energia:
                    st+="1"
                else:
                    st+="0"

            st+=",display="+str(aros)+";"

            st=st.encode()

            return st



        if dft:
            pygame.init()

            #           _____________________________
            #__________/Crear pantalla
            a=1000 #ancho pantalla
            b=600 #largo pantalla

            black=(0,0,0)

            root_jueg=pygame.display.set_mode((a,b))
            pygame.display.set_caption("Atraviesa los reles")
            c=pygame.time.Clock()

            #           _____________________________
            #__________/Cargar imagenes
            Jug_w=pygame.image.load("img\\Jug_w.png") #Jugador hacia arriba
            Jug_a=pygame.image.load("img\\Jug_a.png") #Jugador hacia la izquierda
            Jug_s=pygame.image.load("img\\Jug_s.png") #Jugador hacia abajo
            Jug_d=pygame.image.load("img\\Jug_d.png") #Jugador hacia la derecha
            Jug_c=pygame.image.load("img\\Jug_c.png") #Jugador centro
            Jug=pygame.image.load("img\\Jug_c.png") #Jugador
            Aro=pygame.image.load("img\\Aro.png") #Aro
            fondo=pygame.image.load("img\\fondo.jpg") #Fondo
            Explosion=pygame.image.load("img\\explosion.png") 
            Energia=pygame.image.load("img\\energía.png")
            Energia=pygame.transform.scale(Energia, (25, 25))


            #           _____________________________
            #__________/Efectos de sonido
            colision_sonido= pygame.mixer.Sound('sonidos\\crash.wav')
            energia_sonido= pygame.mixer.Sound('sonidos\\energy.wav')


            def exp(surf,x,y,xi,yi): #Exapandir superficie (surf), se expande a x,y y se colaca siempre en xi,yi
                    global in1
                    sleep(0.001)
                    if x>500: #Si sobre pasa la medida 500x500 traspasa al jugaodr
                            in1=0
                    surf=pygame.transform.scale(surf, (x, y))
                    root_jueg.blit(surf,(xi,yi))


            def ev_choque_comp(posa,dima,posb,dimb):
                """
******************************************************************
Instituto: Tecnológico de Costa Rica
Carrera :Ing. Computadores 
Curso: Intro a la programación
Como implementar: se invoca con ev_choque_comp()
Módulo : reiniciar puntuaciones
Autores : Juan Pablo Alvarado, Sebastián Calderón, Julian
Lenguaje: Python 3.6
Version : 1.0
Ult.Fecha de mod: 3/6/18
Entradas : posicion y dimensiones de dos cuerpos
Restricciones: ninguna
Salidas: si existe el choque todo su superficie
******************************************************************"""
                if (posb[0]<=posa[0] and posa[0]+dima[0]<=posb[0]+dimb[0]) and (posb[1]<=posa[1] and posa[1]+dima[1]<=posb[1]+dimb[1]):
                    return True
                return False

            def ev_choque_punt(posa,dima,posb,dimb):
                """
******************************************************************
Instituto: Tecnológico de Costa Rica
Carrera :Ing. Computadores 
Curso: Intro a la programación
Como implementar: se invoca con ev_choque_punt()
Módulo : reiniciar puntuaciones
Autores : Juan Pablo Alvarado, Sebastián Calderón, Julian
Lenguaje: Python 3.6
Version : 1.0
Ult.Fecha de mod: 3/6/18
Entradas : posicion y dimensiones de dos cuerpos
Restricciones: ninguna
Salidas: si existe el choque en cualquier punto congruente
******************************************************************"""
                if (posb[0]<=posa[0]<=posb[0]+dimb[0] or posb[0]<=posa[0]+dima[0]<=posb[0]+dimb[0]) and (posb[1]<=posa[1]<=posb[1]+dimb[1] or posb[1]<=posa[1]+dima[1]<=posb[1]+dimb[1]):
                    return True
                return False

            def ev_aro(PosJug,PosAro):
               if not ev_choque_punt(PosJug,(150,300),PosAro,(500,500)):
                        return 2
               if PosJug[0]<(PosAro[0]+480) and (PosJug[0]+300)>=PosAro[0] and PosJug[1]+150>=PosAro[1] and (PosJug[1])<=(PosAro[1]+500):
                    if PosJug[0]>(PosAro[0]+10) and (PosJug[0]+300)<(PosAro[0]+490) and PosJug[1]>(PosAro[1]+10) and (PosJug[1]+150)<(PosAro[1]+480):
                        return
                    else:
                        exp(Aro,x_a,y_a,xi_a,yi_a)
                        gen_img(Explosion,posX_jug-150,posY_jug-75)
                        pygame.display.update()
                        return 1


            #           _____________________________
            #__________/Posiciones

            xi_a,yi_a=300,300 #posicon inicial del aro
            x_a=100
            y_a=100

            xi_e,yi_e=300,300 #posicion inicial de la energia
            x_e=20
            y_e=20

            
            #           _____________________________
            #__________/Variables relativas
            i=1 #indicador de parada del while principal
            a=6 #incremento de aro inicial
            e=1 #incremento de energia inicial
            t_inicio=time() #variable que define el momento de inicio del juego
            t_reg=1 #tiempo necesario para colocar otra energia



            #           _____________________________
            #__________/movimiento
            while i:
                if C_display==0:
                    sleep(2)
                    break

                root_jueg.fill(black)
                root_jueg.blit(fondo,(0,0))

                Count+=1

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i=0

                teclas = pygame.key.get_pressed()

                if teclas[pygame.K_LEFT] or teclas[97]:
                    if posX_jug>=10:
                        posX_jug-=10
                        Jug=pygame.transform.scale(Jug_a, (300, 150))
                elif teclas[pygame.K_RIGHT] or teclas[100]:
                    if posX_jug<=499:
                        posX_jug+=10
                        Jug=pygame.transform.scale(Jug_d, (300, 150))
                elif teclas[pygame.K_UP] or teclas[119]:
                    if posY_jug>=10:
                        posY_jug-=10
                        Jug=pygame.transform.scale(Jug_w, (300, 150))
                elif teclas[pygame.K_DOWN] or teclas[115]:
                    if posY_jug<=445:
                        posY_jug+=10
                        Jug=pygame.transform.scale(Jug_s, (300, 150))

                if x_a>600: #Si el aro mide más de 600x600 se resetean sus condiciones de inicio
                    x_a,y_a=50,50
                    in1=1
                    xi_a,yi_a=randint(100,500),randint(200,500) #Se varía un poco el eje
                    if a<14: 
                        a+=0.5 #Se limita la velocidad de incremento

                if x_e>60: #Si el la energia mide más de 60x60 se resetean sus condiciones de inicio
                    if time()-t_inicio>=t_reg:
                        x_e=0
                        y_e=0
                        xi_e,yi_e=randint(100,500),randint(200,500) #Se varía un poco el eje
                        t_inicio=time()
                        t_reg+=1
                    else:
                        xi_e,yi_e=1000,1000
                    if e<1: 
                        e+=0.5 #Se limita la velocidad de incremento

                x_a+=int(a) #aumenta el incremento de "exp"
                y_a+=int(a)
                xi_a-=a//2 #desplaza el eje de imagen para dar efecto de crecer sobre sí misma
                yi_a-=a//2
                

                x_e+=int(e) #aumenta el incremento de "exp"
                y_e+=int(e)
                xi_e-=e//2 #desplaza el eje de imagen para dar efecto de crecer sobre sí misma
                yi_e-=e//2

                if x_a>500 and in1==1:
                    salir=ev_aro((posX_jug,posY_jug),(xi_a,yi_a))
                    C_display-=1
                    arduino.write(gen_serial(Energia_c,C_display))
                    if salir==1:
                        colision_sonido.play()
                        sleep(2)
                        break
                    elif salir==2:
                        pass
                    else:
                        Puntaje+=25

                if 52>x_e>50:
                    if (ev_choque_punt((xi_e,yi_e),(y_e,x_e),(posX_jug,posY_jug),(300,150))):
                        Energia_c=Energia_c+10 if Energia_c+10<=100 else 100
                        energia_sonido.play()
                        
                if Count==10:
                    Count-=10
                    Energia_c-=1
                    arduino.write(gen_serial(Energia_c,C_display))
                    
                

                exp(Energia,x_e,y_e,xi_e,yi_e)
                if in1: #si debe traspasarlo, entonces se genera primero el aro
                    exp(Aro,x_a,y_a,xi_a,yi_a)
                    gen_img(Jug,posX_jug,posY_jug)
                else: #si no debe traspasarlo, entonces se genera primero el jugador
                    gen_img(Jug,posX_jug,posY_jug)
                    exp(Aro,x_a,y_a,xi_a,yi_a)


                Jug=pygame.transform.scale(Jug_c, (300, 150)) #El jugador siempre debe medir 300x150

                Text=pygame.font.SysFont("monospace",20)
                Txt_E=Text.render(dic_trad[30]+str(Energia_c),1,(255,255,0))
                root_jueg.blit(Txt_E,(800,100))
                Txt_A=Text.render(dic_trad[29]+str(Puntaje),1,(255,255,0))
                root_jueg.blit(Txt_A,(800,200))
                Txt_I=Text.render(nombre,1,(255,255,0))
                root_jueg.blit(Txt_I,(800,300))
               
                pygame.display.update()

                c.tick(60)
        else:
            pygame.init()

            #           _____________________________
            #__________/Crear pantalla
            a=1000 #ancho pantalla
            b=600 #largo pantalla

            black=(0,0,0)

            root_jueg=pygame.display.set_mode((a,b))
            pygame.display.set_caption("Juego")
            c=pygame.time.Clock()

            #           _____________________________
            #__________/Posiciones
            xi_e,yi_e=300,300 #posicion inicial de la energia
            x_e=20
            y_e=20

            
            #           _____________________________
            #__________/Variables relativas
            i=1 #indicador de parada del while principal
            e=1 #incremento de energia inicial
            t_inicio=time() #variable que define el momento de inicio del juego
            t_reg=1 #tiempo necesario para colocar otra energia

            #           _____________________________
            #__________/Cargar imagenes
            Jug_w=pygame.image.load("img\\Jug_w.png") #Jugador hacia arriba
            Jug_a=pygame.image.load("img\\Jug_a.png") #Jugador hacia la izquierda
            Jug_s=pygame.image.load("img\\Jug_s.png") #Jugador hacia abajo
            Jug_d=pygame.image.load("img\\Jug_d.png") #Jugador hacia la derecha
            Jug_c=pygame.image.load("img\\Jug_c.png") #Jugador centro
            Jug=pygame.image.load("img\\Jug_c.png") #Jugador
            Disp=pygame.image.load("img\\Disp_Jug.png")
            Enem1_img=pygame.image.load("img\\Enem_c.png")
            Enem2_img=pygame.image.load("img\\Enem_c.png")
            Enem3_img=pygame.image.load("img\\Enem_c.png")
            fondo=pygame.image.load("img\\fondo.jpg") #Fondo
            Explosion=pygame.image.load("img\\explosion.png") 
            Mira=pygame.image.load("img\\mira.png")
            Energia=pygame.image.load("img\\energía.png")
            Energia=pygame.transform.scale(Energia, (25, 25))
            Bala=pygame.image.load("img\\exz.gif")

            #           _____________________________
            #__________/Enemigos
            Enemigo1=[Enem1_img, 0, 0, 0, False, 0, 0, 0, 0] #0=imagen, 1=posX, 2=posY, 3=orientacion, 4=vivo o destruido, 5=tiempo aparicion, 6=ancho, 7=alto, 8=sobre o debajo del jugador
            Enemigo2=[Enem2_img, 0, 0, 0, False, 0, 0, 0, 0]
            Enemigo3=[Enem3_img, 0, 0, 0, False, 0, 0, 0, 0]

            

            def gen_enem(Selector): #generacion enemigos
                """******************************************************************
            Instituto: Tecnológico de Costa Rica
            Carrera :Ing. Computadores 
            Curso: Intro a la programación
            Como implementar: se invoca con gen_enem(Selector)
            Módulo : enemigos
            Autores : Juan Pablo Alvarado, Sebastián Calderón, Julian
            Lenguaje: Python 3.6
            Version : 1.0
            Ult.Fecha de mod: 4/6/18
            Entradas : Alguna de las tres listas de enemigos
            Restricciones: ninguna
            Salidas: lista del enemigo con valores de aparicion aleatorios
            ******************************************************************"""
                if Selector[4]==False:
                    if Selector[5]==0:
                        Selector[3]=randint(0,4)    #se escoge si va hacia el centro, izquierda, derecha, arriba o abajo
                        if Selector[3]==0:
                            Selector[0]=pygame.image.load("img\\Enem_c.png")
                            Selector[1]=randint(250,350)
                            Selector[2]=randint(250,350)
                            Selector[4]=True
                            Selector[5]=0
                            Selector[6]=20
                            Selector[7]=10
                    else:
                        Selector[5]+=1
                        if Selector==Enemigo1:
                            return  gen_enem(Enemigo1)
                        elif Selector==Enemigo2:
                            return gen_enem(Enemigo2)
                        elif Selector==Enemigo3:
                            return gen_enem(Enemigo3)
                else:
                    return

            #           _____________________________
            #__________/Efectos de sonido
            colision_sonido= pygame.mixer.Sound('sonidos\\crash.wav')
            energia_sonido= pygame.mixer.Sound('sonidos\\energy.wav')
            laser_sonido= pygame.mixer.Sound('sonidos\\Laser.wav')


            def exp_enem(Enemigo): #Exapandir superficie (surf), se expande a x,y y se colaca siempre en xi,yi
                """******************************************************************
            Instituto: Tecnológico de Costa Rica
            Carrera :Ing. Computadores 
            Curso: Intro a la programación
            Como implementar: se invoca con exp_enem(Enemigo)
            Módulo : enemigos
            Autores : Juan Pablo Alvarado, Sebastián Calderón, Julian
            Lenguaje: Python 3.6
            Version : 1.0
            Ult.Fecha de mod: 4/6/18
            Entradas : Alguna de las tres listas de enemigos
            Restricciones: ninguna
            Salidas: imagen expandida del enemigo escogido
            ******************************************************************"""
                sleep(0.001)
                if Enemigo[4]==True:
                    if Enemigo[6]>=300:
                        Enemigo[6]+=8
                        Enemigo[7]+=4
                    elif Enemigo[6]>100:
                        Enemigo[6]+=4
                        Enemigo[7]+=2
                    elif Enemigo[6]<=100:
                        Enemigo[6]+=2
                        Enemigo[7]+=1
                    if Enemigo[6]>300: #Si sobre pasa la medida 300x150 traspasa al jugador
                        Enemigo[8]=1
                    surf=pygame.transform.scale(Enemigo[0], (Enemigo[6], Enemigo[7]))
                    root_jueg.blit(surf,(Enemigo[1],Enemigo[2]))
                else:
                    gen_enem(Enemigo)
                    exp_enem(Enemigo)
                

            def exp(surf,x,y,xi,yi): #Exapandir superficie (surf), se expande a x,y y se colaca siempre en xi,yi
                """******************************************************************
            Instituto: Tecnológico de Costa Rica
            Carrera :Ing. Computadores 
            Curso: Intro a la programación
            Como implementar: se invoca con exp()
            Módulo : enemigos
            Autores : Juan Pablo Alvarado, Sebastián Calderón, Julian
            Lenguaje: Python 3.6
            Version : 1.0
            Ult.Fecha de mod: 4/6/18
            Entradas : imagen a agrandar, su tamaño en el eje X, su tamaño en el eje Y, el origen en el eje X y el origen en el eje Y, respectivamente
            Restricciones: ninguna
            Salidas: imagen expandida de de la imagen a agrandar
            ******************************************************************"""
                global in1
                sleep(0.001)
                if x>500: #Si sobre pasa la medida 500x500 traspasa al jugaodr
                    in1=0
                surf=pygame.transform.scale(surf, (x, y))
                root_jueg.blit(surf,(xi,yi))

            def ev_choque_comp(posa,dima,posb,dimb):
                if (posb[0]<=posa[0] and posa[0]+dima[0]<=posb[0]+dimb[0]) and (posb[1]<=posa[1] and posa[1]+dima[1]<=posb[1]+dimb[1]):
                    return True
                return False

            def ev_choque_punt(posa,dima,posb,dimb):
                if (posb[0]<=posa[0]<=posb[0]+dimb[0] or posb[0]<=posa[0]+dima[0]<=posb[0]+dimb[0]) and (posb[1]<=posa[1]<=posb[1]+dimb[1] or posb[1]<=posa[1]+dima[1]<=posb[1]+dimb[1]):
                    return True
                return False

            #           _____________________________
            #__________/funcion choques enemigos
            def ev_choque_enem(PosJug,Enemigo):
                """******************************************************************
            Instituto: Tecnológico de Costa Rica
            Carrera :Ing. Computadores 
            Curso: Intro a la programación
            Como implementar: se invoca con ev_choque_enem(PosJug,Enemigo)
            Módulo : enemigos
            Autores : Juan Pablo Alvarado, Sebastián Calderón, Julian
            Lenguaje: Python 3.6
            Version : 1.0
            Ult.Fecha de mod: 4/6/18
            Entradas : tupla con la posición en el eje X y Y del jugador y otra tupla con la de alguno de los enemigos seleccionados
            Restricciones: ninguna
            Salidas: booleano True si se cumple, False si no
            ******************************************************************"""
                if PosJug[0]<Enemigo[0]+300 and PosJug[0]+300>=Enemigo[0] and PosJug[1]+150>=Enemigo[1] and PosJug[1]<=Enemigo[1]+150:
                   return True
                else:
                    return False
                    
            t_reg1=1
            a_bala=2
            t_bala=time()
            indi_bala=1
            lx=2
            ly=2
            x_1=10000
            y_1=10000
            #           _____________________________
            #__________/movimiento
            while i:
                if C_display==0:
                    sleep(2)
                    break
                root_jueg.fill(black)
                root_jueg.blit(fondo,(0,0))

                Count+=1
                
                if lx>30: #Si el la energia mide más de 60x60 se resetean sus condiciones de inicio
                    if time()-t_bala>=t_reg1:
                        lx=0
                        ly=0
                        x_1,y_1=Enemigo1[1],Enemigo1[2] #Se varía un poco el eje
                        t_bala=time()
                    else:
                        x_1,y_1=1000,1000
                        lx,ly=0,0

                lx+=int(a_bala) #aumenta el incremento de "exp"
                ly+=int(a_bala)


                if 25>lx>20:
                    if ev_choque_punt((x_1,y_1),(lx,ly),(posX_jug,posY_jug),(300,150)):
                        gen_img(Explosion,posX_jug-150,posY_jug-75)
                        pygame.display.update()
                        sleep(2)
                        i=0
                exp(Bala,lx,ly,x_1,y_1)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i=0

                teclas = pygame.key.get_pressed()

                if teclas[pygame.K_LEFT] or teclas[97]:
                    if posX_jug>=10:
                        posX_jug-=10
                        Jug=pygame.transform.scale(Jug_a, (300, 150))
                        gen_enem(Enemigo2)
                elif teclas[pygame.K_RIGHT] or teclas[100]:
                    if posX_jug<=499:
                        posX_jug+=10
                        Jug=pygame.transform.scale(Jug_d, (300, 150))
                elif teclas[pygame.K_UP] or teclas[119]:
                    if posY_jug>=60:
                        posY_jug-=10
                        Jug=pygame.transform.scale(Jug_w, (300, 150))
                elif teclas[pygame.K_DOWN] or teclas[115]:
                    if posY_jug<=445:
                        posY_jug+=10
                        Jug=pygame.transform.scale(Jug_s, (300, 150))
                elif teclas[pygame.K_SPACE] or teclas[32]:
                    gen_img(Disp, posX_jug+121,posY_jug-50)
                    laser_sonido.play()
                    if posX_jug+121<=Enemigo1[1]+Enemigo1[6] and posX_jug+171>=Enemigo1[1] and posY_jug<=Enemigo1[2]+Enemigo1[7] and posY_jug-50>=Enemigo1[2]:
                        Puntaje+=25
                        Enemigo1=[Enem1_img, 0, 0, 0, False, 0, 0, 0, 0]
                        C_display-=1
                        arduino.write(gen_serial(Energia_c,C_display))
                        gen_enem(Enemigo1)
                    elif posX_jug+121<=Enemigo2[1]+Enemigo2[6] and posX_jug+171>=Enemigo2[1] and posY_jug<=Enemigo2[2]+Enemigo2[7] and posY_jug-50>=Enemigo2[2]:
                        Puntaje+=25
                        Enemigo2=[Enem2_img, 0, 0, 0, False, 0, 0, 0, 0]
                        C_display-=1
                        arduino.write(gen_serial(Energia_c,C_display))
                        gen_enem(Enemigo2)
                    elif posX_jug+121<=Enemigo3[1]+Enemigo3[6] and posX_jug+171>=Enemigo3[1] and posY_jug<=Enemigo3[2]+Enemigo3[7] and posY_jug-50>=Enemigo3[2]:
                        Puntaje+=25
                        Enemigo3=[Enem3_img, 0, 0, 0, False, 0, 0, 0, 0]
                        C_display-=1
                        arduino.write(gen_serial(Energia_c,C_display))
                        gen_enem(Enemigo3)

                if x_e>60: #Si el la energia mide más de 60x60 se resetean sus condiciones de inicio
                    if time()-t_inicio>=t_reg:
                        x_e=0
                        y_e=0
                        xi_e,yi_e=randint(100,500),randint(200,500) #Se varía un poco el eje
                        t_inicio=time()
                        t_reg+=1
                    else:
                        xi_e,yi_e=1000,1000
                    if e<1: 
                        e+=0.5 #Se limita la velocidad de incremento
                

                x_e+=int(e) #aumenta el incremento de "exp"
                y_e+=int(e)
                xi_e-=e//2 #desplaza el eje de imagen para dar efecto de crecer sobre sí misma
                yi_e-=e//2

            #           _____________________________
            #__________/Choque de naves
                if Enemigo1[6]>300:
                    if ev_choque_enem((posX_jug, posY_jug),(Enemigo1[1], Enemigo1[2]))==True:
                        gen_img(Explosion,posX_jug-150,posY_jug-75)
                        pygame.display.update()
                        sleep(2)
                        i=0
                    else:
                        Enemigo1=[Enem1_img, 0, 0, 0, False, 0, 0, 0, 0]
                        gen_enem(Enemigo1)

                if Enemigo2[6]>300:
                    if ev_choque_enem((posX_jug, posY_jug),(Enemigo2[1], Enemigo2[2]))==True:
                        gen_img(Explosion,posX_jug-150,posY_jug-75)
                        pygame.display.update()
                        sleep(2)
                        i=0
                    else:
                        Enemigo2=[Enem2_img, 0, 0, 0, False, 0, 0, 0, 0]
                        gen_enem(Enemigo2)

                if Enemigo3[6]>300:
                    if ev_choque_enem((posX_jug, posY_jug),(Enemigo3[1], Enemigo3[2]))==True:
                        gen_img(Explosion,posX_jug-150,posY_jug-75)
                        pygame.display.update()
                        sleep(2)
                        i=0
                    else:
                        Enemigo3=[Enem3_img, 0, 0, 0, False, 0, 0, 0, 0]
                        gen_enem(Enemigo3)

                if 52>x_e>50:
                    if (ev_choque_punt((xi_e,yi_e),(y_e,x_e),(posX_jug,posY_jug),(300,150))):
                        Energia_c=Energia_c+10 if Energia_c+10<=100 else 100
                        energia_sonido.play()
                        
                if Count==10:
                    Count-=10
                    Energia_c-=1
                    arduino.write(gen_serial(Energia_c,C_display))
                    

                exp(Energia,x_e,y_e,xi_e,yi_e)

                if Enemigo1[8]==1:
                    if Enemigo2[8]==1:
                        if Enemigo3[8]==1:
                            gen_img(Jug,posX_jug,posY_jug)
                            exp_enem(Enemigo1)
                            exp_enem(Enemigo2)
                            exp_enem(Enemigo3)
                        else:
                            exp_enem(Enemigo3)
                            gen_img(Jug,posX_jug,posY_jug)
                            exp_enem(Enemigo1)
                            exp_enem(Enemigo2)
                    else:
                        if Enemigo3[8]==1:
                            exp_enem(Enemigo2)
                            gen_img(Jug,posX_jug,posY_jug)
                            exp_enem(Enemigo1)
                            exp_enem(Enemigo3)
                        else:
                            exp_enem(Enemigo2)
                            exp_enem(Enemigo3)
                            gen_img(Jug,posX_jug,posY_jug)
                            exp_enem(Enemigo1)
                elif Enemigo1[8]==0:
                    if Enemigo2[8]==1:
                        if Enemigo3[8]==1:
                            exp_enem(Enemigo1)
                            gen_img(Jug,posX_jug,posY_jug)
                            exp_enem(Enemigo2)
                            exp_enem(Enemigo3)
                        else:
                            exp_enem(Enemigo1)
                            exp_enem(Enemigo3)
                            gen_img(Jug,posX_jug,posY_jug)
                            exp_enem(Enemigo2)
                    else:
                        if Enemigo3[8]==1:
                            exp_enem(Enemigo1)
                            exp_enem(Enemigo2)
                            gen_img(Jug,posX_jug,posY_jug)
                            exp_enem(Enemigo3)
                        else:
                            exp_enem(Enemigo1)
                            exp_enem(Enemigo2)
                            exp_enem(Enemigo3)
                            gen_img(Jug,posX_jug,posY_jug)
                else:
                    exp_enem(Enemigo1)
                    exp_enem(Enemigo2)
                    exp_enem(Enemigo3)
                    gen_img(Jug,posX_jug,posY_jug)

                
                gen_img(Mira,posX_jug+121,posY_jug-50)

                Jug=pygame.transform.scale(Jug_c, (300, 150)) #El jugador siempre debe medir 300x150

                Text=pygame.font.SysFont("monospace",20)
                Txt_E=Text.render(dic_trad[30]+str(Energia_c),1,(255,255,0))
                root_jueg.blit(Txt_E,(800,100))
                Txt_A=Text.render(dic_trad[29]+str(Puntaje),1,(255,255,0))
                root_jueg.blit(Txt_A,(800,200))
                Txt_I=Text.render(nombre,1,(255,255,0))
                root_jueg.blit(Txt_I,(800,300))
               
                pygame.display.update()

                c.tick(60)

        root.deiconify()
        pygame.quit()
        Ventana_aux()

        file=open("Jug.txt","a")
        file.write(str(nombre)+","+str(Puntaje)+"\n")
        file.close()
        ordenar2()

    def Ventana_aux(): #Ventana que sirve para mostrar las puntuaciones aleatorias generadasen comparacion con el jugador
        global li_per
        va=Toplevel()
        va.geometry("400x400+300+150")
        va.minsize(400,400)
        va.resizable(NO,NO)

        C_va=Canvas(va,width=400,height=400,bg="light green")
        C_va.place(x=0,y=0)

        
        li_per=asignar(li_per)
        li_per[i_per]=(nombre+"*",Puntaje)
        li_temp=ordenar(li_per)
        
        tex=""
        for i in li_temp:
            tex=str(i[0])+"\t\t"+str(i[1])+"\n"+tex
        
        L_va=Label(va,text=tex,bg="white",fg="#000000",font=('Eras Bold ITC',12),justify=CENTER)
        L_va.place(x=0,y=0)


    def aro():
        root.withdraw()
        vj.destroy()
        Juego(1) #aro
    def enemigos():
        root.withdraw()
        vj.destroy()
        Juego(0) #enemigo


    home=cargarImg("aro.gif")
    Btn_back1 = Button(C_vj, image=home ,command=aro, fg = "#000000")
    Btn_back1.image = home
    Btn_back1.place(x=200,y=120)

    home1=cargarImg("aste.gif")
    Btn_back2 = Button(C_vj, image=home1 ,command=enemigos, fg = "#000000")
    Btn_back2.image = home1
    Btn_back2.place(x=200,y=360)
    
#______________/Sección de preventana del juego
def Jugar(): #función que carga la ventana del juego
    nombre = str(E_nombre.get()).capitalize()
    if lenn(nombre)>10: #verifica largo del nombre
        messagebox.showinfo(":(",dic_trad[8])
        return
    if nombre=="": #verifica que no sea vacío
        messagebox.showinfo(":(",dic_trad[9])
        return
    else:
        VentanaJuego(nombre) #devuelve la ventana junto con el nombre introducido

#               __________________
#______________/Selector de iconos
def ajust_bot(c_i):
   global Lista_bot
   for i in range(len(Lista_bot)):
       if i==c_i:
           sel="green"
       else:
           sel="black"
       Lista_bot[i].configure(bg=sel) 

#               ____________________________
#______________/Movimiento del potenciometro y botones
def get_pot():
        a=arduino.readline()
        b=a[18:20]
        try:
            c=int(b)
        except:
            c=int(b[0])-48
        return c
def get_bot():
        a=arduino.readline()
        b2=a[12]-48
        b1=a[5]-48
        return b1,b2

arduino=serial.Serial("COM3",38400)

def mov_potenciometro_botones(c_i):
    global vent,Lista_bot,i_per,i_back
    
    sleep(.1)

    btn=get_bot()
    print(btn,vent)

    if btn[1]==0:
        if vent!=0:
            print("salir")
            i_back=True
            
    if vent==0: #ventana principal
        c=get_pot()//8
        if c_i==c:
            pass
        else:
            c_i=c
            ajust_bot(c_i)
    elif vent==1: #ventana configuracion
        try:
            c=get_pot()
            if c>60:
                c=60
            global i_per
            i_per=c//3-1
        except:
            pass
    elif vent==2: #ventana play
        c=get_pot()
    return mov_potenciometro_botones(c_i)


        


#______________/Sección de botones de la ventana principal
x1=400
mul=80
y1=500

def back ():
    root.destroy()

img_aux=cargarImg("top2.gif")
Btn1=Button(root,command=Ventana1,text=dic_trad[2],fg="black",bg="black",image=img_aux)
Btn1.place(x=x1+mul*2,y=y1)

img_aux1=cargarImg("inf.gif")
Btn2=Button(root,command=Ventana2,text="Info",fg="black",bg="black",image=img_aux1)
Btn2.place(x=x1+mul*3,y=y1)

img_aux2=cargarImg("play.gif")
Btn3=Button(root,command=Jugar,text=dic_trad[4],fg="black",bg="black",image=img_aux2)
Btn3.place(x=x1,y=y1)


img_aux3=cargarImg("set.gif")
Btn6=Button(root,command=Ventana3,text=dic_trad[11],fg="black",bg="black",image=img_aux3)
Btn6.place(x=x1+mul,y=y1)

img_aux4=cargarImg("cerr.gif")
Btn7=Button(root,command=back,text=dic_trad[11],fg="black",bg="black",image=img_aux4)
Btn7.place(x=x1+mul*4,y=y1)

img_aux5=cargarImg("us.gif")
Btn4=Button(root,command=inter,text="Español",fg="black",bg="grey",font=('Eras Bold ITC',12),image=img_aux5)
Btn4.place(x=650,y=10)

c_i=0
global Lista_bot
Lista_bot=[Btn4,Btn7,Btn2,Btn1,Btn6,Btn3,Btn_song0,Btn_song2,Btn_song1]

Hilo_poten=Thread(target=mov_potenciometro_botones,args=(c_i,)) #hilo
Hilo_poten.start()



root.mainloop()
