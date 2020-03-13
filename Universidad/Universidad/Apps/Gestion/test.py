import psycopg2;

def miCalendario(request):
    if request.user.is_authenticated:
        user = request.user
        conexion = psycopg2.connect(database="tfg_db", user="tfg", password="12Septiembre")
        cursor1 = conexion.cursor()
        cursor1.execute("select * from Gestion_calendario")
        for fila in cursor1:
            print(fila)
            print("hola")
        conexion.close()
