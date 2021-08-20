from flask import Flask, render_template, request, jsonify
from ai import Acker

app = Flask(__name__)
ai = None

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/start', methods=['GET', 'POST'])
def start():
   message = request.args.get('message')
   global ai
   # 0: white
   # 1: black
   if message == 'first':
       print(message)
       ai = Acker(0)
   else:
       ai = Acker(1)

   #print(message)
   return message

@app.route('/move', methods=['GET', 'POST'])
def move():
    global ai
    message = request.args.get('message')
    pos = list(map(int, message.split(',')))
    source, dest = ai.move([pos[0], pos[1]], [pos[2], pos[3]])
    return str(source[0]) + ',' + str(source[1]) + ',' + str(dest[0]) + ',' + str(dest[1])

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=5000)
