#IMPORTAR LIBRERIAS DE FLASK
from flask import Flask, render_template, request
#IMPORTAR LIBRERIAS DE MYSQL (PARA LA CONEXION)
from flaskext.mysql import MySQL 

#INICIALIZAMOS FLASK
app = Flask(__name__)
#INGRESAMOS LA CONECCION A LA BASE DE DATOS
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'nest2015'
app.config['MYSQL_DATABASE_DB'] = 'flaskcontacts'
mysql = MySQL()
mysql.init_app(app)

#RUTA DEL INDEX
@app.route('/')
def Index():
    return render_template('index.html')

#RUTA PARA AGREGAR CONTACTOS, DEFINIMOS EL METODO
@app.route ('/add_contact', methods=['POST'])
def add_contact(): #DEFINIMOS EL ADD_CONTACT
    #SI EL REQUEST ES POST, TOMAMOS LOS VALORES DE LOS TEXTBOX
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        #LLAMAMOS EL CURSOR OBTENER LA CONEXCION
        cur = mysql.get_db().cursor()
        #CARGAMOS EL QUERY, LOS PORCENTAJES LOS PONEMOS PARA DESPUES METER UNA TUPLA CON LOS VALORES QUE CAPTURAMOS CON EL METODO POST
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)',
        (fullname, phone, email))
        #HACEMOS UN COMMIT PARA QUE LOS VALORES INGRESEN A LA BASE DE DATOS.
        mysql.get_db().commit()
        return 'received'
    

@app.route ('/edit')
def edit_contact():
    return 'edit contact'

@app.route ('/delete')
def delete_contact():
    return 'delete contact'       

#CONFIGURAMOS EL PUERTO, LEVANTAMOS EL SERVIDOR Y EL MODO DEBUG
if  __name__ == '__main__':
    app.run(port = 3000, debug = True)