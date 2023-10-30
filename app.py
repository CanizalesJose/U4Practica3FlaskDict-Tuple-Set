from flask import Flask, json

app = Flask(__name__)

#-----------------Diccionarios-----------------------
@app.route("/dict/agregar/<path:diccionario>/<clave>/<valor>")
#1. Función que recibe un diccionario y agrega una clave-valor, retorna el diccionario actualizado
def agregarAlDict(diccionario, clave, valor):
    diccionario = json.loads(diccionario)

    diccionario.update({clave:valor})
    
    diccionario = json.dumps(diccionario)

    return diccionario

@app.route("/dict/eliminar/<path:diccionario>/<clave>")
#2. Función que reciba un diccionario y elimine una clave-valor, retornar el diccionario modificado
def eliminarDeDict(diccionario: dict, clave):
    diccionario = json.loads(diccionario)
    diccionario.pop(clave)
    diccionario = json.dumps(diccionario)
    return diccionario

@app.route("/dict/modificar/<path:diccionario>/<clave>/<valor>")
#3. Función que reciba un diccionario y modifique el valor de una clave, retornar verdadero si pudo modificar y falso si no pudo
def modificarDelDict(diccionario: dict, clave, valor):
    diccionario = json.loads(diccionario)
    
    if clave not in diccionario:
        return f"{False}"
    else:
        diccionario.update({clave:valor})
        diccionario = json.dumps(diccionario)
        return f"{True}, Resultado = {diccionario}"

@app.route("/dict/combinar/<path:diccionario1>/<path:diccionario2>")
#4. Función que combine dos diccionarios, regresar el diccionario resultante
def combinarDiccionarios(diccionario1: dict, diccionario2: dict):
    diccionario1 = json.loads(diccionario1)
    diccionario2 = json.loads(diccionario2)

    diccionario1.update(diccionario2)

    diccionario1 = json.dumps(diccionario1)

    return diccionario1

@app.route("/dict/imprimir/<path:diccionario>")
#12. Función que recibe un diccionario y lo imprime
def imprimirDiccionario(diccionario):
    diccionario = json.loads(diccionario)
    if isinstance(diccionario, dict):
        print(diccionario)
        return json.dumps(diccionario)
    else:
        print("No es un diccionario...")

#------------------Conjuntos------------------

@app.route("/set/agregar/<path:conjunto>/<elemento>")
#5. Función que agregue elementos a un conjunto, retornar verdadero si pudo agregar y falso si no pudo.
def agregarAlSet(conjunto: set, elemento):
    conjunto = set(conjunto.split(","))
    print(conjunto)
    if elemento in conjunto:
        return "False"
    else:    
        conjunto.add(elemento)
        print(conjunto)
        return "True, Resultado: "+ str(conjunto)

@app.route("/set/eliminar/<path:conjunto>/<elemento>")
#6. Función que elimine un elemento de un conjunto, retornar verdadero si pudo eliminar y falso si no pudo
def eliminarDelSet(conjunto: set, elemento):
    conjunto = set(conjunto.split(","))
    if elemento not in conjunto:
        return "False"
    else:
        conjunto.remove(elemento)
        return "True, Resultado: " + str(conjunto)

@app.route("/set/combinar/<path:conjunto1>/<path:conjunto2>")
#7. Función que combine dos conjuntos, regresar el conjunto resultante
def combinarSets(conjunto1: set, conjunto2: set):
    conjunto1 = set(conjunto1.split(","))
    conjunto2 = set(conjunto2.split(","))
    resultado = conjunto1.union(conjunto2)
    return str(resultado)

@app.route("/set/diferencia/<path:conjunto1>/<path:conjunto2>")
#8. función que regrese la diferencia de dos conjuntos
def diferenciasEnSets(conjunto1: set, conjunto2: set):
    conjunto1 = set(conjunto1.split(","))
    conjunto2 = set(conjunto2.split(","))
    resultado = conjunto1.symmetric_difference(conjunto2)
    return str(resultado)

@app.route("/set/imprimir/<path:conjunto>")
#14. Función que recibe un conjunto y lo imprime
def imprimirSet(conjunto):
    conjunto = set(conjunto.split(","))
    if isinstance(conjunto, set):
        print(conjunto)
        return str(conjunto)
    else:
        print("No es un conjunto...")
        return "No es un conjunto..."
    
#--------------Tuplas------------------

@app.route("/tuple/agregar/<path:tupla>/<elemento>")
#9. Función que elimine un elemento a una tupla y lo guarde los cambios en una tupla nueva, regresar la nueva tupla
def eliminarElementoTupla(tupla, elemento):
    tupla = tuple(tupla.split(","))
    if elemento in tupla:
        nuevo = list(tupla)
        nuevo.remove(elemento)
        resultado = tuple(nuevo)
        return str(resultado)
    else:
        return str(tupla)
    
@app.route("/tuple/concatenar/<path:tupla1>/<path:tupla2>")
#10. Función que concatene dos tuplas en una nueva, regresar la nueva tupla
def concatenarTuplas(tupla1: tuple, tupla2: tuple):
    tupla1 = tuple(tupla1.split(","))
    tupla2 = tuple(tupla2.split(","))
    resultado = list(tupla1) + list(tupla2)
    return str(tuple(resultado))

@app.route("/tuple/invertir/<path:tupla>")
#11. Función que revertir el orden de una tupla y lo guarde los cambios en una tupla nueva, regresar la nueva tupla
def invertirTupla(tupla: tuple):
    tupla = tuple(tupla.split(","))
    resultado = list(tupla)
    resultado.reverse()
    return str(tuple(resultado))

@app.route("/tuple/imprimir/<path:tupla>")
#13. Función que recibe un tupla y la imprime
def imprimirTupla(tupla):
    tupla = tuple(tupla.split(","))
    if isinstance(tupla, tuple):
        print(tupla)
        return str(tupla)
    else:
        print("No es una tupla...")
        return "No es una tupla..."