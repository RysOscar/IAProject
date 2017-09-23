from pyke import knowledge_engine,goal
import time

eliminar = False
banamex = False
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

def procedimientoeliminar():
    global eliminar
    eliminar = True

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

    #eliminar del query (campo)
    eliminarquery = open('eliminarcampo.txt','a')
    eliminarquery.write("""$query = "Delete from """)
    eliminarquery.close()

    # eliminar del query (values)
    eliminarquery = open('eliminarvalues.txt', 'a')
    eliminarquery.write(" where (")
    eliminarquery.close()

    #Archivo php eliminar
    Archivophpeliminar = open('eliminar.php','a')
    Archivophpeliminar.write("<?php")
    Archivophpeliminar.close()

    #creando archivo de eliminar de js
    Archivoeliminarjs = open('eliminar.js','a')
    contenido = """
                function EliminarFuncion()
                {
                var url = "eliminar.php";
                $.post(url,
                {"""
    Archivoeliminarjs.write(contenido)
    Archivoeliminarjs.close()






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

                #php delete-----------------------------------------------
                Archivoeliminarphp = open('eliminar.php','a')
                Archivoeliminarphp.write(contenido)
                Archivoeliminarphp.close()





    with v_BD.prove(busqueda,campo = dato)as gen:#inserta el dato
        for vars,plan in gen:
            if vars['tipo']=="bd":
                contenido = """
                            $database = """+chr(34)+dato+chr(34)+";"
                Archivoinsertphp = open('Insertar.php', 'a')
                Archivoinsertphp.write(contenido)
                Archivoinsertphp.close()

                Archivoeliminarphp = open('eliminar.php', 'a')
                Archivoeliminarphp.write(contenido)
                Archivoeliminarphp.close()






    with v_user.prove(busqueda,campo = dato)as gen:#inserta el dato = echo que se quiera definir
        for vars,plan in gen:
            if vars['tipo']=="user":
                contenido = """
                            $usuario = """+chr(34)+dato+chr(34)+";"
                Archivoinsertphp = open('Insertar.php', 'a')
                Archivoinsertphp.write(contenido)
                Archivoinsertphp.close()

                Archivoeliminarphp = open('eliminar.php', 'a')
                Archivoeliminarphp.write(contenido)
                Archivoeliminarphp.close()



    with v_pass .prove(busqueda, campo=dato)as gen:  # inserta el dato = echo que se quiera definir
        for vars, plan in gen:
            if vars['tipo'] == "password":
                contenido = """
                            $password = """ + chr(34) + dato + chr(34) + ";"
                Archivoinsertphp = open('Insertar.php', 'a')
                Archivoinsertphp.write(contenido)
                Archivoinsertphp.close()

                Archivoeliminarphp = open('eliminar.php', 'a')
                Archivoeliminarphp.write(contenido)
                Archivoeliminarphp.close()



    with v_table.prove(busqueda,campo=dato)as gen: #insertar el dato
        for vars,plan in gen:
            if vars['tipo']=="tabla":
                contenido = """
                            $tabla = """+chr(34)+dato+chr(34)+";"

                Archivoinsertphp = open('Insertar.php','a')
                Archivoinsertphp.write(contenido)
                Archivoinsertphp.close()

                #query eliminar
                Archivoeliminarphp = open('eliminarcampo.txt','a')
                Archivoeliminarphp.write(dato)
                Archivoeliminarphp.close()


    with v_Text.prove(busqueda,campo=dato)as gen: #extructura html con primer campo
        for vars,plan in gen:
            if vars['tipo']=="text":
                contenido = """<center>"""+dato+"""</center>
                                <p><center><input id = "texto"""+dato+chr(34)+""" type = "text" maxlength = "50"></center></p>"""

                Archivopaginahtml = open('pagina.html','a')
                Archivopaginahtml.write(contenido)
                Archivopaginahtml.close()

                #php insert
                contenido = """
                            $"""+dato+"= $_POST["+chr(34)+dato+chr(34)+"];"

                Archivoinsertphp = open('Insertar.php','a')
                Archivoinsertphp.write(contenido)
                Archivoinsertphp.close()

                #PHP DELETE
                Archivoeliminarphp = open('eliminar.php','a')
                Archivoeliminarphp.write(contenido)
                Archivoeliminarphp.close()


                if(eliminar == False):
                    Archivoeliminarvalues = open('eliminarvalues.txt','a')
                    Archivoeliminarvalues.write("""'".$"""+dato+"""."' = """+dato+""")";""")
                    Archivoeliminarvalues.close()
                    #funcion
                    procedimientoeliminar()




                #query insertar campos
                if(banamex == True):
                    primerpartequery = open('Firstinsert.txt','a')
                    primerpartequery.write(",")
                    primerpartequery.close()


                    #Insertar Valores
                    insertarvalores = open('Secondinsert.txt','a')
                    insertarvalores.write(",")
                    insertarvalores.close()

                    #insertar en js

                    insertarenjs = open('insertar.js','a')
                    insertarenjs.write(",")
                    insertarenjs.close()


                    #eliminar del js
                    Archivoeliminarjs = open('eliminar.js','a')
                    Archivoeliminarjs.write(",")
                    Archivoeliminarjs.close()


                primerpartequery = open('Firstinsert.txt','a')
                primerpartequery.write(dato)
                primerpartequery.close()

                #query insertar valores
                insertarvalores=open('Secondinsert.txt','a')
                insertarvalores.write("""'".$"""+dato+"""."'""")
                insertarvalores.close()
                #insertar js
                insertarenjs = open('insertar.js', 'a')
                insertarenjs.write(dato+":$("+chr(34)+"#texto"+dato+chr(34)+").val()")
                insertarenjs.close()

                #eliminar js
                Archivoeliminarjs = open('eliminar.js','a')
                Archivoeliminarjs.write(dato+":$("+chr(34)+"#texto"+dato+chr(34)+").val()")
                Archivoeliminarjs.close()

                if(banamex == False):#SI LA VARIABLE ES FALSA
                    Activarbanamex()#FUNCION ACTIVAR BANDERA


def terminar_html():
    endhtml = """
                <button type = "button" onclick = "NuevoUsuario()">
                Registrar
                </button>
                <button type = "button" onclick = "EliminarUsuario()">
                Eliminar Usuario
                </button>
                
                <button type = "button" onclick = "ActualizarUsuario()">
                Actualizar Usuario
                </button>
                
                <div id = "respuesta" class = "row"></div>
                
                <script type = "text/javascript" src = "insertar.js"></script>
                <script type = "text/javascript" src = "actualizar.js"></script>
                <script type = "text/javascript" src = "eliminar.js"></script>
                <script type = "text/javascript" src = "jquery.js"></script>
                </body>
                </html>
                """
    Archivopaginahtml = open('pagina.html','a')
    Archivopaginahtml.write(endhtml)
    Archivopaginahtml.close()

    #query insertar valores
    insertarvalores = open('Secondinsert.txt', 'a')
    insertarvalores.write(")"+chr(34)+")")
    insertarvalores.close()

    campo = open('Firstinsert.txt','r')#r lee los archivos
    valores = open('Secondinsert.txt', 'r')
    
    Finphp = open('eliminarcampo.txt','r')
    finphpval = open('eliminarvalues.txt','r')


    terminarinsertarphp = """
                        try
                        {
                            $conexionsql = new mysqli($servidor,$usuario,$password,$database):
                            if($conexionsql -> connect_errno){
                            ?>
                            <script type="text/javascript">window.alert("OCURRIÓ UN ERROR EN LA CONEXIÓN");</script>
                            <?php
                        }
                        else
                        {
                            """+campo.read()+valores.read()+"""
                            $ResultadoOperacion = $conexionsql -> query($query);
	 		            if($ResultadoOperacion)
	 		            {
	 		            ?>
                            <script type="text/javascript">window.alert("Listón");</script>
	 		            <?php 
	 		            }
	 		            else
	 		            {
	 		            ?>
	 		                <script type="text/javascript">window.alert("Ocurrion un error en el proceo de registro");</script>
	 		            
                        <?php
                        
                                }
                            }
                        }
                            catch (Exception $e) {throw $e;}
                        ?>
                        """
    valores.close()
    campo.close()

    Archivoinsertarphp = open('insertar.php','a')
    Archivoinsertarphp.write(terminarinsertarphp)
    Archivoinsertarphp.close()
    #termina js ingresar

    contenido = """
                },
                function (data)
                {
                    $("#respuesta").html(data);
            
                }
                };
                }"""
    Archivojsinsertar = open('insertar.js','a')
    Archivojsinsertar.write(contenido)
    Archivojsinsertar.close()




























































