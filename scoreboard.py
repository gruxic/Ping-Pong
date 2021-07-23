from turtle import Turtle
FONT=("Courier",20, "normal")
SCOREFONT=("Courier",25, "normal")
ALIGNMENT="center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.rscore=0
        self.lscore=0
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f" {self.lscore}      {self.rscore}",align="center",font=SCOREFONT)
    def increase_score_l(self):
        self.lscore+=1
        self.clear()
        self.update_score()
    def increase_score_r(self):
        self.rscore+=1
        self.clear()
        self.update_score()

    def game_over_checker(self):
        if(self.lscore==5):
            self.goto(0,0)
            self.write(f"   GAME OVER.\nPLAYER ONE WINS",align=ALIGNMENT,font=FONT)
            return False
        if(self.rscore==5):
            self.goto(0,0)
            self.write(f"   GAME OVER.\n PLAYER TWO WINS",align=ALIGNMENT,font=FONT)
            return False
        return True