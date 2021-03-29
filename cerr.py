from flask import Flask, render_template, request, redirect, url_for, flash, g 
from handlers import error_pages
from flask_mysqldb import MySQL
from flask import session
import smtplib

app = Flask(__name__)

app.register_blueprint(error_pages)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/login')
def login():
    return render_template('loging.html')

@app.route('/homeusua')
def homeusua():
    if not g.user:
        return render_template('peligro.html')
    return render_template('homeusua.html')

@app.route('/consulta')
def consulta():
    if not g.user:
        return render_template('peligro.html')
    return render_template('consulta.html')

@app.route('/consulta-carro')
def conscar():
    if not g.user:
        return render_template('peligro.html')
    return render_template('consulta-carro.html')

@app.route('/consulta-casa')
def conscasa():
    if not g.user:
        return render_template('peligro.html')
    return render_template('consulta-casa.html')

@app.route('/reserva')
def reserva():
    if not g.user:
        return render_template('peligro.html')
    return render_template('reserva.html')

@app.route('/reserva-carro')
def reservacar():
    if not g.user:
        return render_template('peligro.html')
    return render_template('reserva-carro.html')

@app.route('/reserva-casa')
def reservacas():
    if not g.user:
        return render_template('peligro.html')
    return render_template('reserva-casa.html')

@app.route('/homeadmin')
def homeadmin():
    if not g.user:
        return render_template('peligro.html')
    elif session['user'] == 'admin':
        return render_template('homeadmin.html')
    else:
        return render_template('peligro.html')

@app.route('/adminres')
def adminres():
    if not g.user:
        return render_template('peligro.html')
    return render_template('adminres.html')

@app.route('/admincar')
def admincar():
    if not g.user:
        return render_template('peligro.html')

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM reservacarro')
    data = cur.fetchall()
    return render_template('adminres-car.html', contacts = data)
    

@app.route('/admincas')
def admincas():
    if not g.user:
        return render_template('peligro.html')

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM reservacasa')
    data = cur.fetchall()
    return render_template('adminres-cas.html', contacts = data)

@app.route('/admincon')
def admincon():
    if not g.user:
        return render_template('peligro.html')
    return render_template('admincon.html')

@app.route('/adminconscar')
def adminconscar():
    if not g.user:
        return render_template('peligro.html')

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM consultacarro')
    data = cur.fetchall()
    return render_template('admincons-car.html', contacts = data)

@app.route('/adminconscas')
def adminconscas():
    if not g.user:
        return render_template('peligro.html')

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM consultacasa')
    data = cur.fetchall()
    return render_template('admincons-cas.html', contacts = data)

@app.route('/usuarios')
def usuarios():
    if not g.user:
        return render_template('peligro.html')

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuario')
    data = cur.fetchall()
    return render_template('usuarios.html', contacts = data)




#--- ---- ------ ------ ------- ------- -------- --------- -------- -------- -------

#conexion MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'cerrajeria'
mysql = MySQL(app)
# ----------------- -------------------- ---------------------- ----------------------

#inicio de secion

app.secret_key ='mysecretkey'

@app.route('/')
def Index():
    return render_template('registro.html')

# ----------------- -------------------- ---------------------- ----------------------

    #agregar datos

@app.route('/add_contact', methods = ['POST'])
def add_contact():

    if request.method == 'POST':

        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        passw = request.form['passw']
        if (nombre == '' or apellido == '' or correo == '' or passw == ''):
            flash('¡ Campos vacios !')
            return render_template('registro.html')
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO usuario (nombre, apellido, correo, pass) VALUES (%s, %s, %s, %s)', (nombre, apellido, correo, passw))
        mysql.connection.commit()
        flash('Usuario registrado')
        return render_template('loging.html')

# ----------------- -------------------- ---------------------- ----------------------

    # comparacion de datos

@app.route('/loginz', methods = ['GET', 'POST'])
def loginz():
    error = None
    if request.method == 'POST':
        session.pop('user', None)

        session['user'] = request.form['correo']
        passw = request.form['pass']
        if (session['user'] == 'linacerrajeria@gmail.com' and passw == 'Asdf1234zxcv'):
            session['user']='admin'
            return redirect(url_for('protected'))
        else:
            if (session['user'] == 'linacerrajeria@gmail.com' and passw != 'Asdf1234zxcv' ):
                flash('Hola Administrador, tu contraseña es incorrecta')
                return redirect(url_for('login'))

        cur = mysql.connection.cursor()
        user = session['user']  
        filas = cur.execute(f'SELECT * FROM usuario where correo = "{user}" and pass = "{passw}"')
        session['user'] = user
        mysql.connection.commit()

        if filas == 0 :
        #request.form['Username'] != 'correo' or request.form['Password'] != 'pass':
            error = 'Datos invalido'
            flash('Correo o contraseña invalida')
        else:
            return redirect(url_for('protected1'))
        
    return render_template('loging.html', error=error)

# ----------------- -------------------- ---------------------- ----------------------

        #Sesion

@app.route('/protected')
def protected():
    if g.user:
        flash('Administrador')
        return render_template('homeadmin.html')

    return redirect(url_for('home'))

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']


@app.route('/getsession')
def getsession():
    if  'user' in session:
        return session['user']

    return 'No estas iniciando'

@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return 'Tramposo!'

@app.route('/logout')
def logout():
    if session['user'] == 'admin':
        session['admin']=''
    session.pop('user', None)
    flash('Cerro sesión')
    return redirect(url_for('home'))

@app.route('/protected1')
def protected1():
    if g.user:
        flash(g.user)
        return render_template('homeusua.html')
    return redirect(url_for('home'))

@app.route('/logout1')
def logout1():
    session.pop('user', None)
    flash('Cerro sesión')
    return redirect(url_for('home'))
#--- ---- ---- ---- ----- ------ ------- ------ ----- ------ --------- ------ ------ ------- ------ ------ 

    #Insertar datos a MYSQL

@app.route('/reservacarro', methods = ['POST'])
def reservacarro():

    if request.method == 'POST':

        Marca = request.form['Marca']
        Modelo = request.form['Modelo']
        Ubicacion = request.form['Ubicacion']
        Correo = request.form['Correo']
        Tipo_trabajo = request.form['Tipo_trabajo']
        Fecha = request.form['Fecha']
        if (Marca == '' or Modelo == '' or Ubicacion == '' or Correo == '' or Tipo_trabajo == '' or Fecha == ''):
            flash('Campos vacios')
            return render_template('reserva-carro.html')
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO reservacarro (Marca, Modelo, Ubicacion, Correo, Tipo_trabajo, Fecha) VALUES (%s, %s, %s, %s, %s, %s)', (Marca, Modelo, Ubicacion, Correo, Tipo_trabajo, Fecha))

# ----------------- -------------------- ---------------------- ----------------------

         # Aviso al correo

        message = 'Tienes una reserva para un auto, revise los datos del cliente en el sitio web'
        subject = 'RESERVA PARA AUTO'
        message = 'Subject: {}\n\n{}'.format(subject, message)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('linacerrajeria@gmail.com', 'Asdf1234zxcv')
        server.sendmail('linacerrajeria@gmail.com', 'linacerrajeria@gmail.com', message)
        server.quit()
        mysql.connection.commit()
        flash('¡Reserva registrada!')
        return render_template('homeusua.html')

@app.route('/reservacasa', methods = ['GET', 'POST'])
def reservacasa():

    if request.method == 'POST':

        Domicilio = request.form['Domicilio']
        Numero = request.form['Numero']
        Correo = request.form['Correo']
        Referencia = request.form['Referencia']
        Tipo_trabajo = request.form['Tipo_trabajo']
        Fecha = request.form['Fecha']
        if (Domicilio == '' or Numero == '' or Correo == '' or Referencia == '' or Tipo_trabajo == '' or Fecha == ''):
            flash('Campos vacios')
            return render_template('reserva-casa.html')
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO reservacasa (Domicilio, Numero, Correo, Referencias, Tipo_trabajo, Fecha) VALUES (%s, %s, %s, %s, %s, %s)', (Domicilio, Numero, Correo, Referencia, Tipo_trabajo, Fecha))
        
        # Aviso al correo
        message = 'Tienes una reserva para una casa, revise los datos del cliente en el sitio web'
        subject = 'RESERVA PARA CASA'
        message = 'Subject: {}\n\n{}'.format(subject, message)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('linacerrajeria@gmail.com', 'Asdf1234zxcv')
        server.sendmail('linacerrajeria@gmail.com', 'linacerrajeria@gmail.com', message)
        server.quit()

        mysql.connection.commit()
        flash('¡Reserva registrada!')      
        return render_template('homeusua.html')

@app.route('/consultacarro', methods = ['GET', 'POST'])
def consultacarro():

    if request.method == 'POST':


        Marca = request.form['marca']
        Modelo = request.form['Modelo']
        Ubicacion = request.form['Ubicacion']
        Correo = request.form['Correo']
        Tipo_trabajo = request.form['Tipo_trabajo']
        if (Modelo == '' or Marca == '' or Ubicacion == '' or Correo == '' or Tipo_trabajo == ''):
            flash('Campos vacios')
            return render_template('consulta-carro.html')
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO consultacarro (Marca, Modelo, Ubicacion, Correo, Tipo_trabajo) VALUES (%s, %s, %s, %s, %s)', (Marca, Modelo, Ubicacion, Correo, Tipo_trabajo))
        
        # Aviso al correo
        message = 'Tienes una consulta para una casa, revise los datos del cliente en el sitio web'
        subject = 'CONSULTA PARA CARRO'
        message = 'Subject: {}\n\n{}'.format(subject, message)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('linacerrajeria@gmail.com', 'Asdf1234zxcv')
        server.sendmail('linacerrajeria@gmail.com', 'linacerrajeria@gmail.com', message)
        server.quit()
        
        mysql.connection.commit()
        flash('¡Consulta registrada!')      
        return render_template('homeusua.html')

@app.route('/consultacasa', methods = ['GET', 'POST'])
def consultacasa():

    if request.method == 'POST':

        Domicilio = request.form['Domicilio']
        Numero = request.form['Numero']
        Correo = request.form['Correo']
        Referencia = request.form['Referencia']
        Tipo_trabajo = request.form['Tipo_trabajo']
        if (Domicilio == '' or Numero == '' or Correo == '' or Referencia == '' or Tipo_trabajo == ''):
            flash('Campos vacios')
            return render_template('consulta-casa.html')
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO consultacasa (Domicilio, Numero, Correo, Referencias, Tipo_trabajo) VALUES (%s, %s, %s, %s, %s)', (Domicilio, Numero, Correo, Referencia, Tipo_trabajo))
        
        # Aviso al correo
        message = 'Tienes una consulta para una casa, revise los datos del cliente en el sitio web'
        subject = 'CONSULTA PARA CASA'
        message = 'Subject: {}\n\n{}'.format(subject, message)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('linacerrajeria@gmail.com', 'Asdf1234zxcv')
        server.sendmail('linacerrajeria@gmail.com', 'linacerrajeria@gmail.com', message)
        server.quit()
        
        mysql.connection.commit()
        flash('¡Consulta registrada!') 
        print('hola')     
        return render_template('homeusua.html')

# ----------------- -------------------- ---------------------- ----------------------

    #Borrar datos de MYSQL

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM reservacarro WHERE Id = {0}' .format(id))
    mysql.connection.commit()
    flash('Contacto Eliminado')
    return redirect(url_for('admincar'))

@app.route('/delete1/<string:id>')
def delete_contact1(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM reservacasa WHERE Id = {0}' .format(id))
    mysql.connection.commit()
    flash('Contacto Eliminado')
    return redirect(url_for('admincas'))

@app.route('/delete2/<string:id>')
def delete_contact2(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM consultacarro WHERE Id = {0}' .format(id))
    mysql.connection.commit()
    flash('Contacto Eliminado')
    return redirect(url_for('adminconscar'))

@app.route('/delete3/<string:id>')
def delete_contact3(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM consultacasa WHERE Id = {0}' .format(id))
    mysql.connection.commit()
    flash('Contacto Eliminado')
    return redirect(url_for('adminconscas'))

@app.route('/delete4/<string:id>')
def delete_contact4(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM usuario WHERE Id = {0}' .format(id))
    mysql.connection.commit()
    flash('Contacto Eliminado')
    return redirect(url_for('usuarios'))

# ----------------- -------------------- ---------------------- ----------------------

    #Denegar accesos




# ----------------- -------------------- ---------------------- ----------------------


if __name__ == "__main__":
    app.run(debug=True)