fowardPlayer1 = "player1_foward.png"
backwardPlayer1 = "player1_backward.png"
leftPlayer1 = "player1_left.png"
rightPlayer1 = "player1_right.png"

def movePlayer1():

    for event in pygame.event.get():

        if event.type==KEYDOWN:

            if event.key==K_Z:
                fowardPlayer1
                position_player1.move(0,10)

            if event.key==K_S:
                backwardPlayer1
                position_player1.move(0,-10)

            if event.key==K_Q:
                leftPlayer1
                position_player1.move(-10,0)

            if event.key==K_D:
                rightPlayer1
                position_player1.move(10,0)

            ##if event.key==K_SPACE:
                ## placeBomb()

fowardPlayer2 = "player2_foward.png"
backwardPlayer2 = "player2_backward.png"
leftPlayer2 = "player2_left.png"
rightPlayer2 = "player2_right.png"


def movePlayer2():

        for event in pygame.event.get():

            if event.type==KEYDOWN:

                if event.key==K_UP:
                    fowardPlayer2
                    position_player2.move(0,10)

                if event.key==K_DOWN:
                    backwardPlayer2
                    position_player2.move(0,-10)

                if event.key==K_LEFT:
                    leftPlayer2
                    position_player2.move(-10,0)

                if event.key==K_RIGHT:
                    rightPlayer2
                    position_player2.move(10,0)

                ##if event.key==K_0:
                    ## placeBomb()
