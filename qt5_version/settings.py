import os

TITLE = "Two Beats One"
WIDTH = 750
HEIGHT = 750
MARGIN_LEFT = WIDTH / 10
MARGIN_TOP = HEIGHT / 10
LINES = 4
GRID_WIDTH = (WIDTH - 2 * MARGIN_LEFT) / (LINES - 1)
GRID_HEIGHT = (HEIGHT - 2 * MARGIN_TOP) / (LINES - 1)
PIECE_SIZE = int(GRID_WIDTH // 4)

SERVERNAME = '34.87.108.23'
PORT = 6666

#icon path
ICON_FILEPATH = os.path.join(os.getcwd(), 'img/icon/icon.ico')

#bgi path
BACKGROUND_IMAGEPATHS = {
                            'bg_start': os.path.join(os.getcwd(), 'img/bg/bg_start.png'),
                            'bg_game': os.path.join(os.getcwd(), 'img/bg/bg_game.png')
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

