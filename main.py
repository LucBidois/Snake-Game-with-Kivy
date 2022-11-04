from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock


class Player1(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class Player2(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class SnakeGame(Widget):
    player1 = ObjectProperty(None) #create player 1 object - ref kv file
    player2 = ObjectProperty(None) #create player 1 object - ref kv file


    def set_snake(self, vel=(0, 1)):
        self.player1.center = self.center
        self.player1.velocity = vel
        self.player2.center = self.center
        self.player2.velocity = vel

    def update(self, dt):
        self.player1.move()
        #self.player2.move()


class SnakeApp(App):
    def build(self):
        game = SnakeGame()
        game.set_snake()
        Clock.schedule_interval(game.update, 1.0 / 60)
        return game


if __name__ == '__main__':
    SnakeApp().run()
 