import board_driver_servo as BD
import time

while True:
    print('ID:',BD.ID())
    while True:
        BD.Led(0)
        BD.Led(1)
        BD.Led(2)
        BD.Led(3)

