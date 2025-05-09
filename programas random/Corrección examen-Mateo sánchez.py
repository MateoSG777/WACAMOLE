def registro(rcoci, rcont_ca, rcont_po, rcont_pe, rind):
    print("Registro del día de hoy")
    c = int(input("¿Cuántos cocineros desea registrar? "))
    r=1
    while rind < c:
        rcoci[rind] = input(f"Ingrese el nombre del cocinero:{r} ")
        rind += 1
        r=r + 1
    print("Registro de porciones de proteina en nevera")
    rcont_ca = int(input("¿Cuántas porciones de carne desea? "))
    rcont_po = int(input("¿Cuántas porciones de pollo desea? "))
    rcont_pe = int(input("¿Cuántas porciones de pescado desea? "))
    return rcoci, rcont_ca, rcont_po, rcont_pe

def cocineros (ccoci,ccarne,cpollo,cpesc,ccont_ca,ccont_po,ccont_pe,cind, ccom):
    nc = 0
    npo = 0
    npe = 0
    nom = ""
    print("Vamos a cocinar")
    nom = input ("Ingrese el nombre del cocinero: ")
    i = 0
    while i < cind:
        if nom == ccoci [i]:
            print(f"Disponibilidad de: carne: {ccont_ca}, pollo: {ccont_po}, pescado: {ccont_pe}")
            print("¿Cuántas porciones de carne desea? ")
            nc = int(input("    \t\t\t\t\tcarne: "))    
            npo = int(input("    \t\t\t\t\tpollo: "))
            npe = int(input("    \t\t\t\t\tpescado: "))
            if nc <= ccont_ca and npo <= ccont_po and npe <=ccont_pe:
                ccarne[i] = ccarne [1] + nc
                cpollo[i] = cpollo [1] + npo
                cpesc[i] = cpesc [1] + npe
                ccont_ca = ccont_ca - nc
                ccont_po = ccont_po - npo
                ccont_pe = ccont_pe - npe
            else:
                print("No hay suficientes porciones de proteína")
            i = cind
        else:
            i = i + 1
    return ccoci,ccarne,cpollo,cpesc,ccont_ca,ccont_po,ccont_pe,ccom

def cierre(tcoci,tcarne,tpollo,tpesc,tcont_ca,tcont_po,tcont_pe,tind,tcomanda):
    i=0
    cc=0
    cp=0
    ce=0
    print("Estado cartera")
    print("Proteina reitrada de nevera:")
    print("cocinero\tcarne\tpollo\tpescado")
    while i < tind:
        print(tcoci[i],"\t",tcarne[i],"\t",tpollo[i],"\t",tpesc[i])
        cc = cc + tcarne[i]
        cp = cp + tpollo[i]
        ce = ce + tpesc[i]
        i = i + 1
    print(f"Total carne: {cc}, pollo: {cp}, pescado: {ce}")
    print(f"Total de porciones de carne: {tcont_ca}, pollo: {tcont_po}, pescado: {tcont_pe}")

def main():
    porciones = [[0]*3 for i in range(5)] 
    coci = [""]*5  
    carne = [row[0] for row in porciones]   
    pollo = [row[1] for row in porciones]   
    pescado = [row[2] for row in porciones]
    ind = 0
    resp = "s"
    comanda = 0
    cont_ca = 0  
    cont_po = 0  
    cont_pe = 0  
    coci, cont_ca, cont_po, cont_pe = registro(coci, cont_ca, cont_po, cont_pe, ind)
    resp = input("¿Hay un cocinero que requiera retirar proteina de la nevera? (s/n):")
    while resp == "s" and comanda < 50:
        coci, carne, pollo, pescado, cont_ca, cont_po, cont_pe, comanda = cocineros(coci, carne, pollo, pescado, cont_ca, cont_po, cont_pe, ind, comanda)
        resp = input("¿Hay otro cocinero que requiera retirar proteina de la nevera? (s/n): ")
        comanda = comanda + 1
    cierre(coci, carne, pollo, pescado, cont_ca, cont_po, cont_pe, ind, comanda)
    print(" FIN DEL PROGRAMA")
main()


