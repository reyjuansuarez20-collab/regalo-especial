from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'mi_llave_secreta_super_romantica'

# CONFIGURACIÓN: Cambia estos datos por los reales
NOMBRE_ELLA = "yorlennie" # Escribe su nombre exacto
FECHA_BESO = "19092025" # Formato DDMMAAAA

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    nombre = request.form.get('nombre')
    password = request.form.get('password')

    if nombre.lower() == NOMBRE_ELLA.lower() and password == FECHA_BESO:
        # Aquí es donde estaba el error. Cambia el texto por esto:
        return render_template('carta.html') 
    else:
        flash("¡Ups! Buny dice que algo está mal... intenta de nuevo.")
        return redirect(url_for('index'))
    
@app.route('/carta')
def mostrar_carta():
    return render_template('carta.html')

@app.route('/final')
def sorpresa_final():
    return render_template('final.html')

@app.route("/galeria")
def galeria():
    return render_template("galeria.html")

if __name__ == '__main__':
    app.run(debug=True)