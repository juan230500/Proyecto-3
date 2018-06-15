
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



#_________________/Ordenar lista de jugadores
def ordenar(li):
    def quicksort(L, first, last):
        # definimos los índices y calculamos el pivote
        i = first
        j = last    
        pivote = (L[i][1] + L[j][1]) / 2

        # iteramos hasta que i no sea menor que j
        while i < j:
            # iteramos mientras que el valor de L[i] sea menor que pivote
            while L[i][1] < pivote:
                # Incrementamos el índice
                i+=1
            # iteramos mientras que el valor de L[j] sea mayor que pivote
            while L[j][1] > pivote:
                # decrementamos el índice
                j-=1
            # si i es menor o igual que j significa que los índices se han cruzado
            if i <= j:
                # creamos una variable temporal para guardar el valor de L[j]
                x = L[j]
                # intercambiamos los valores de L[j] y L[i]
                L[j] = L[i]
                L[i] = x
                # incrementamos y decrementamos i y j respectivamente
                i+=1
                j-=1

        # si first es menor que j mantenemos la recursividad
        if first < j:
            L = quicksort(L, first, j)
        # si last es mayor que i mantenemos la recursividad
        if last > i:
            L = quicksort(L, i, last)

        # devolvemos la lista ordenada
        return L

    return quicksort(li,0,len(li)-1)

escribir_1("t.txt")
a=leer("t.txt")
a=ordenar(a)
print(a)



