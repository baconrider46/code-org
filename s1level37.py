'''s1level37
for (var count2 = 0; count2 < 4; count2++) {
  penColour(colour_random());
  for (var count = 0; count < 3; count++) {
    moveForward(100);
    turnRight(120);
  }
  turnRight(90);
}'''

import turtle

nibbles = turtle.Turtle()
nibbles.pensize(7)
nibbles.pencolor('cyan')



for count2 in range(36):
    nibbles.pencolor('cyan')
    for count in range(3):
        nibbles.forward(100)
        nibbles.right(120)
    nibbles.right(90)
        
