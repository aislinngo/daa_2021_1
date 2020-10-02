import xlrd
from arrays import *
def main():
    a3=Array3D(34,33,14)
    for anio in range(2017,2018,1):
        ruta="./Precipitacion/"+str(anio)+"Precip.xls"
        archivo=xlrd.open_workbook(filename=ruta)
        hoja=archivo.sheet_by_index(0)
        for r in range(1,34,1):
            for c in range(0,14,1):
                a3.set_item(anio-2017,r-1,c,hoja.cell_value(r,c))
    """a=int(input("anio(2017-2018)"))
    e=int(input("estado(1-32)"))
    m=int(input("mes(1-12)"))"""
    a=2017
    e=7
    m=3
    #1
    print("En el año",a,"en el mes de",a3.get_item(a-2017,0,m),"en el estado",a3.get_item(a-2017,e,0),"promedio",a3.get_item(a-2017,e,m))
    print()
    #2
    suma=0.0
    for i in range(2017,2018,1):
        
        suma+=a3.get_item(i-2017,e,m)
    print("promedio: ",suma/34)
    print()
    #3
    suma=0.0
    for j in range(2017,2018,1):
        for i in range(0,13,1):
            
            if i!=0:
                suma+=a3.get_item(j-2017,e,i)
        #print()
    print("promedio",suma/408)
    #4
    suma=0.0
    for k in range(2017,2018,1):
        for i in range(1,33,1):
            for j in range(0,13,1):
                if j!=0:

                    suma+=a3.get_item(k-2017,i,j)
    print(suma/12410)
                    
main()
