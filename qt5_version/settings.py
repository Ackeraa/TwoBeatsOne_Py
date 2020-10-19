import os

TITLE = "Two Beats One"
WIDTH = 540
HEIGHT = 540
LINES = 4
X0 = 50
Y0 = 130
GRID_WIDTH = WIDTH / (LINES - 1)
GRID_HEIGHT = HEIGHT / (LINES - 1)
PIECE_SIZE = 35

SIMULATIONS = 3000
DEPTH = 80
CPRAMS = 0.9
SEARCH_DEPTH = 8
INF = 10000000000

DIR = [[1, 0], [0, -1], [-1, 0], [0, 1]]

SERVERNAME = '45.76.169.66'
PORT = 6666

#icon path
ICON_FILEPATH = os.path.join(os.getcwd(), 'img/icon/icon.ico')

#bgi path
BACKGROUND_IMAGEPATHS = {
                            'start_bgi': os.path.join(os.getcwd(), 'img/bg/start_bgi.png'),
                            'game_bgi': os.path.join(os.getcwd(), 'img/bg/game_bgi.jpg'),
                            'board_bgi': os.path.join(os.getcwd(), 'img/bg/board_bgi.png')
                        }
#piece path
PIECEPATH = {
                'white': os.path.join(os.getcwd(), 'img/piece/white.png'),
                'black': os.path.join(os.getcwd(), 'img/piece/black.png'),
                'white1': os.path.join(os.getcwd(), 'img/piece/white1.png'),
                'black1': os.path.join(os.getcwd(), 'img/piece/black1.png'),
            }
#button image path
BUTTON_IMAGEPATHS = {
                        'online': [os.path.join(os.getcwd(), 'img/buttons/online_0.png'),
                                   os.path.join(os.getcwd(), 'img/buttons/online_1.png'),
                                   os.path.join(os.getcwd(), 'img/buttons/online_2.png')],
                        'ai': [os.path.join(os.getcwd(), 'img/buttons/ai_0.png'),
                               os.path.join(os.getcwd(), 'img/buttons/ai_1.png'),
                               os.path.join(os.getcwd(), 'img/buttons/ai_2.png')],
                        'home': [os.path.join(os.getcwd(), 'img/buttons/home_0.png'),
                                 os.path.join(os.getcwd(), 'img/buttons/home_1.png'),
                                 os.path.join(os.getcwd(), 'img/buttons/home_2.png')],
                        'givein': [os.path.join(os.getcwd(), 'img/buttons/givein_0.png'),
                                   os.path.join(os.getcwd(), 'img/buttons/givein_1.png'),
                                   os.path.join(os.getcwd(), 'img/buttons/givein_2.png')],
                        'regret': [os.path.join(os.getcwd(), 'img/buttons/regret_0.png'),
                                   os.path.join(os.getcwd(), 'img/buttons/regret_1.png'),
                                   os.path.join(os.getcwd(), 'img/buttons/regret_2.png')],
                        'startgame': [os.path.join(os.getcwd(), 'img/buttons/startgame_0.png'),
                                      os.path.join(os.getcwd(), 'img/buttons/startgame_1.png'),
                                      os.path.join(os.getcwd(), 'img/buttons/startgame_2.png')],
                        'urge': [os.path.join(os.getcwd(), 'img/buttons/urge_0.png'),
                                 os.path.join(os.getcwd(), 'img/buttons/urge_1.png'),
                                 os.path.join(os.getcwd(), 'img/buttons/urge_2.png')]
                    }

