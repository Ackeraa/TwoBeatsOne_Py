from settings import *

def packSocket(data):
        return (json.dumps(data) + ' END').encode()

def unPackSocket(tcpSocket):
    data = ''
    while True:
        dataPart = tcpSocket.recv(1024).decode()
        if 'END ' in dataPart:
            data += dataPart[:dataPart.index('END')]
            break
        data += dataPart
    return json.loads(data, encoding = 'utf-8')
    

def i2p(pos):
    return [X0 + pos[0] * GRID_WIDTH, Y0 + pos[1] * GRID_HEIGHT]

def p2i(pos):
    return [int((pos[0] - X0 + GRID_WIDTH / 2) / GRID_WIDTH), int((pos[1] - Y0 + GRID_HEIGHT / 2) / GRID_HEIGHT)]

def validPos(pos):
    index = p2i(pos)
    pos_std = i2p(index)
    if pos[0] >= X0 and pos[0] <= WIDTH + X0 and pos[1] >= Y0 and pos[1] <= Y0 + HEIGHT\
            and abs(pos[0] - pos_std[0]) <= PIECE_SIZE and abs(pos[1] - pos_std[1]) <= PIECE_SIZE:
        return index
    else:
        return [-1, -1]


