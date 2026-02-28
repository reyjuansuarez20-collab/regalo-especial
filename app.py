from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'mi_llave_secreta_super_romantica'

# CONFIGURACIÓN ORIGINAL
NOMBRE_ELLA = "yorlennie" 
FECHA_BESO = "19092025" 

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    nombre = request.form.get('nombre')
    password = request.form.get('password')

    # Ajuste para permitir el acceso directo del botón de Buny
    # Comprobamos si es el acceso directo o si son los datos originales
    es_acceso_directo = (nombre == "Chiquita" and password == "acceso_directo")
    es_datos_reales = (nombre and nombre.lower() == NOMBRE_ELLA.lower() and password == FECHA_BESO)

    if es_acceso_directo or es_datos_reales:
        # Usamos redirect para que la URL cambie a /carta correctamente
        return redirect(url_for('mostrar_carta'))
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
