from flask import Flask, jsonify
from flask import request
from random import randint
app = Flask(__name__)


# @app.route('/random')
# def random_number():
#     first_num = int(request.args.get('first_num'))
#     second_num = int(request.args.get('second_num'))
#     pupil_name = request.args.get('pupil_name')
#     print(f'{pupil_name} HA HECHO LA REQUEST')
#     return str(randint(first_num, second_num))
# Enviado desde POSTMAN {"numeros": [100,67,65,67,89,90,67,67,90] }

@app.route('/order', methods=['POST'])
def order():
    data = request.json
    numeros = data.get('numeros')
    numeros = list(set(numeros))
    numeros.sort()

    return jsonify(numeros)

app.run(host='0.0.0.0', port=80, debug=True)