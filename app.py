from flask import Flask, render_template, jsonify, Response
import serial

app = Flask(__name__)
ser = serial.Serial('COM4', 9600)  # Reemplaza 'COM3' con el puerto serial correspondiente

def generate_data():
    while True:
        data = ser.readline().decode().strip()
        yield f"data: {data}\n\n"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream')
def stream():
    return Response(generate_data(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run()
