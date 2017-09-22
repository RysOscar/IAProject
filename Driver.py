from pyke import knowledge_engine,goal
import time

banamex = True
busqueda = knowledge_engine.engine(__file__)
v_Text = goal.compile('mostrar_txt.show_txt($campo,$tipo)')
v_Date = goal.compile('mostrar_date.show_date($campo,$tipo)')
v_Int = goal.compile('mostrar_int.show_int($campo,$tipo)')
v_server = goal.compile('mostrar_server.show_server($campo,$tipo)')
v_user = goal.compile('mostrar_user.show_user($campo,$tipo)')
v_pass = goal.compile('mostrar_pass.show_pass($campo,$tipo)')
v_table = goal.compile('mostrar_table.show_table($campo,$tipo)')
v_BD = goal.compile('mostrar_bd.show_bd($campo,$tipo)')


def Activarbanamex():
    global banamex
    banamex = True

def iniciar_html():#funcion para la creacion de la pagina
    iniciohtml = """<!DOCTYPE html>
                    <html>
                    <head>
                    <title>IA</title>
                    </head>
                    <body>"""

    Archivohtml = open('pagina.html','a')#si no existe crea el archivo y si esiste sobreeescribe la pagina
    #'a' lectura y escritura
    Archivohtml.write(iniciohtml)#pasa como parametro la variable iniciohtml
    Archivohtml.close()
    #query para insertar campos

    Archivoins = open('Firstinsert.txt','a')#crea el archivo del query
    Archivoins.write("""$query = "Insert into""")#primera parte del query
    Archivoins.close()
    #inserción de values
    Archivovalues = open('Secondinsert.txt','a')#crea la segunda parte del query
    Archivovalues.write(") values (")#concatena values
    Archivovalues.close()

    #insercion en php
    Archivoinsertphp = open('Insertar.php','a')#crea php solo con el inicio del formato php
    Archivoinsertphp.write("<?php")
    Archivoinsertphp.close()

    #Archivo de insercion del JavaScript
    ArchivoJsinsertar = open('insertar.js','a')
    contenidojs = """
                    function NuevoUsuario()
                        {
                            var url = "Insertar.php";
                            $.post(url,
                            {"""
    ArchivoJsinsertar.write(contenidojs)
    ArchivoJsinsertar.close()

def comprobar(dato):
    busqueda.reset()#variable con el motor de inteligencia
    busqueda.activate('regla')#usa el archivo de reglas

    with v_server.prove(busqueda,campo = dato)as gen:#campo es la segunda variable de v_server
        for vars,plan in gen:
            if vars['tipo']=='servidor':
                contenido = """
                            $servidor = """+chr(34)+dato+chr(34)+";" #codigo ascii chr(34) comillas
                Archivoinsertphp = open('Insertar.php','a')
                Archivoinsertphp.write(contenido)
                Archivoinsertphp.close()

    with v_BD.prove(busqueda,campo = dato)as gen:#inserta el dato
        for vars,plan in gen:
            if vars['tipo']=="bd":
                contenido = """
                            $database = """+chr(34)+dato+chr(34)+";"
                Archivoinsertphp = open('Insertar.php', 'a')
                Archivoinsertphp.write(contenido)
                Archivoinsertphp.close()

    with v_user.prove(busqueda,campo = dato)as gen:#inserta el dato = echo que se quiera definir
        for vars,plan in gen:
            if vars['tipo']=="user":
                contenido = """
                            $usuario = """+chr(34)+dato+chr(34)+";"
                Archivoinsertphp = open('Insertar.php', 'a')
                Archivoinsertphp.write(contenido)
                Archivoinsertphp.close()



































