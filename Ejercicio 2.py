dict1={"alg2":["alg1"],"alg1":[],"cal1":[],"fis1":[],"p2":["p1"],"p1":[],"cal2":["cal1"],"fis2":["cal1","fis1"],"algoritmos":["p2"],"ecuaciones dif":["alg2","fis2"],"geometria dif":["alg2","fis2","cal2"]}
# keys=nodos , values=lista de "llegadas"(los nodos con listas vacias son nodos sin llegadas solo salidas, es decir, no necesitan de ningun otro nodo para producirse)

dict2={"pantalones":["calzoncillos","calcetines"],"sudadera":["camiseta"],"calcetines":[],"calzoncillos":[],"zapatos":["pantalones","calcetines"],"camiseta":[]}


def ordenar(dict):
    j=0
    i=0
    list=[]

    for i in dict:
        if dict[i]==[]:
            list.append(i)
    #encolamos nodos sin llegadas
    for i in dict:
        for j in list:
            if j in dict[i]:
                dict[i].remove(j)
            #vamos eliminando llegadas (de los nodos con llegadas) recorriendo la cola
                if dict[i]==[]:
                    list.append(i)
            #vamos encolando nodos que se vallan quedando sin llegadas

    return list


print(ordenar(dict2))
print(ordenar(dict1))
