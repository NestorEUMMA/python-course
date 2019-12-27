#IMPORTAR LIBRERIAS DE FLASK, RENDER_TEMPLATE ES PARA MOSTRAR EL TEMPLATE, REQUEST ES PARA EL POST, REDIRECT  ES PARA REDIRECCIONAR CON LA URL
#FLASH ES PARA MANDAR MENSAJES
from flask import Flask, render_template, request, redirect, url_for, flash
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

#CONFIGURACIONES
app.secret_key = 'mysecretkey'

#RUTA DEL INDEX
@app.route('/')
def Index():
    #LLAMAMOS EL CURSOR OBTENER LA CONEXCION
        cur = mysql.get_db().cursor()
        #CARGAMOS EL QUERY, LOS PORCENTAJES LOS PONEMOS PARA DESPUES METER UNA TUPLA CON LOS VALORES QUE CAPTURAMOS CON EL METODO POST
        cur.execute('SELECT * FROM contacts')
        #OBTENER LOS DATOS EN UNA LISTA
        data = cur.fetchall()
        return render_template('index.html', contacts = data)

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
        flash('Contact Added successfully')
        return redirect(url_for('Index'))
    

@app.route ('/edit/<id>')
def edit_contact(id):
     cur = mysql.get_db().cursor()
        #CARGAMOS EL QUERY, LOS PORCENTAJES LOS PONEMOS PARA DESPUES METER UNA TUPLA CON LOS VALORES QUE CAPTURAMOS CON EL METODO POST
     cur.execute('SELECT * FROM contacts WHERE id = %s',(id))
     data = cur.fetchall()
     return render_template('edit-contact.html', contact = data[0])

@app.route ('/update/<id>', methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.get_db().cursor()
            #CARGAMOS EL QUERY, LOS PORCENTAJES LOS PONEMOS PARA DESPUES METER UNA TUPLA CON LOS VALORES QUE CAPTURAMOS CON EL METODO POST
        cur.execute("""
            UPDATE contacts 
            SET fullname = %s,
                email = %s,
                phone = %s
            WHERE id = %s
        """, (fullname, phone, email, id))
        mysql.get_db().commit()
        flash('Contact Updated Successfully')
        return redirect(url_for('Index'))


@app.route ('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.get_db().cursor()
    #CARGAMOS EL QUERY, LOS PORCENTAJES LOS PONEMOS PARA DESPUES METER UNA TUPLA CON LOS VALORES QUE CAPTURAMOS CON EL METODO POST
    cur.execute('DELETE FROM contacts where id = {0}'.format(id))
    mysql.get_db().commit()
    flash('Contact Removed successfully')
    return redirect(url_for('Index'))       

#CONFIGURAMOS EL PUERTO, LEVANTAMOS EL SERVIDOR Y EL MODO DEBUG
if  __name__ == '__main__':
    app.run(port = 3000, debug = True)