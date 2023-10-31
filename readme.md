## Practica 3: Flask- Diccionarios, tuplas y conjuntos

El objetivo de esta práctica es comprender el funcionamiento de los parámetros en Flask. Se deberán recibir parámetros y convertirlos en objetos de Python para manipularlos.

Para esta manipulación se deberán implementar las funciones realizadas en la práctica 1 para trabajar con `diccionarios`, `tuplas` y `conjuntos`.

### Rutas
En Flask, se pueden generar rutas que permitan al usuario acceder al servidor. Estas rutas se definen de la siguiente manera:

    @app.route("/dict/agregar/<path:diccionario>/<clave>/<valor>")

El parámetro corresponde a la dirección aceptada por el servidor, y los elementos que asemejan a etiquetas HTML `<...>` definen parámetros.

Cuando un parámetro incluye `<path:...>`, está indicando que la cadena posee valores que pueden asemejarse a una URL.

Los valores recolectados por el programa desde la URL se tratan como cadenas, y estas pueden ser manipuladas como tal, convirtiéndolas en otros tipos de datos.

### Diccionarios (DICT)
En el caso de los objetos de tipo `diccionario`, se puede usar `JSON` para traducir una cadena de caracteres a un objeto de tipo diccionario en Python.

El método `JSON.loads()` recibe como parámetro la cadena que intenta convertir, y esta debe estar construida siguiendo la siguiente estructura:

    {
        A:2,
        B:5
    }

Después de construir estos objetos, nos interesa convertirlos de nuevo a cadenas JavaScript para alimentar la página web, por lo que el método `JSON.dumps()` nos sirve para esto.

### Tuplas (TUPLE)
Al recibir una tupla desde Flask, se recibe como cadena de caracteres, por lo que se debe traducir a objeto Flask.
Para esto se debe usar el constructor de tuplas, que recibe una cadena, la cual debemos separar por comas (`','`).
Este elemento no podemos mandarlo directamente de regreso para mostrarlo a una página, por lo que se debe usar el constructor de cadenas de caracteres para volver a convertirlo y mostrarlo de manera convencional.

    tupla = tuple(parametroRecibido.split(","))
    return str(tupla)

En conjunto a esto, las tuplas no pueden ser manipuladas de manera convencional, por lo que deben ser convertidas a elementos de tipo lista, manipularse como se desea y luego convertir nuevamente en tupla.

    resultado = list(tupla)
    #Manipular la tupla
    resultado = tuple(resultado)

### Conjuntos (SET)
Los conjuntos funcionan de manera muy similar a las tuplas, sin embargo, estas no deben pasar por el paso intermedio de ser convertidas a listas para ser manipuladas.
Sin embargo, como el parámetro recibido desde Flask es una cadena de caracteres, debe ser convertida usando el constructor de conjuntos y debe convertirse a cadena cuando se muestre el resultado para visualizarlo de manera convencional:

    conjunto = set(parametroRecibido.split(","))
    str(conjunto)

### Funciones implementadas
#### Diccionarios
Las funciones implementadas para los diccionarios incluyen agregar una clave-valor, eliminar una clave-valor, modificar el valor asociado a una clave y combinar dos diccionarios distintos.

    @app.route("/dict/agregar/<path:diccionario>/<clave>/<valor>")

    diccionario = json.loads(diccionario)
    diccionario.update({clave:valor})
    diccionario = json.dumps(diccionario)
    return diccionario

La ruta que se asigna indica que se debe mandar como parámetros, una cadena que se puede incluir elementos propios de una URL, una clave y un valor, todo separado por `/`.
`json.loads(diccionario)` toma la cadena de caracteres recibida desde la URL y la convierte en un objeto Python. Después actualiza el diccionario usando los valores en crudo de los parámetros recibidos.
`json.dumps(diccionario)` toma el objeto de python y lo convierte en una cadena valida para ser usada por JavaScript, lo que se traduce en un formato adecuado para páginas HTML.

    @app.route("/dict/eliminar/<path:diccionario>/<clave>")

    def eliminarDeDict(diccionario: dict, clave):
        diccionario = json.loads(diccionario)
        diccionario.pop(clave)
        diccionario = json.dumps(diccionario)
        return diccionario

Este método recibe dos parámetros, el diccionario y una clave. Se traduce el diccionario en objeto Python y luego se llama el método `diccionario.pop(clave)` para eliminar del diccionario el elemento que coincida con el parámetro `clave`. Se traduce en una cadena JS y se regresa como resultado de la función.

    @app.route("/dict/combinar/<path:diccionario1>/<path:diccionario2>")

    diccionario1 = json.loads(diccionario1)
    diccionario2 = json.loads(diccionario2)
    diccionario1.update(diccionario2)
    diccionario1 = json.dumps(diccionario1)
    return diccionario1

Este método acepta dos parámetros, los cuales son tomados de la ruta a la aplicación Flask. Ambos parámetros son diccionarios, los cuales se traducen a objetos Python y el segundo se agrega al primero. Acto seguido, se traduce a cadena JS y se regresa como resultado.