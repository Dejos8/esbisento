#coding: utf­8
def es_bisiesto (anio):
    if (anio%4==0 and anio%100!=0)or anio%400==0:
    	print"El año", str(anio), "es bisiesto"
    else:
    	print "El año ",str(anio)," no es bisiesto"

print ("iniciando....")
es_bisiesto(2010)
es_bisiesto(2030)
es_bisiesto(2020)
