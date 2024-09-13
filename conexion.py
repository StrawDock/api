#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 20:29:14 2024

@author: marcoantonionavavalganon
"""
from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # Permitir solicitudes desde cualquier origen

# Configuración de la conexión a la base de datos MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Halo2202",
    database="Prueba"
)

# Ruta de prueba
@app.route('/', methods=['GET'])
def home():
    return "API está funcionando"

# Ruta para obtener datos de la base de datos
@app.route('/getData', methods=['GET'])
def get_data():
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM alumnos"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results)

# Iniciar el servidor
if __name__ == '__main__':
    app.run(port=5001)