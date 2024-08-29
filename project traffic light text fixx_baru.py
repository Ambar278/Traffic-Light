from machine import Pin, I2C
from sh1106 import SH1106_I2C
import time

i2c = I2C(0, sda=Pin(8), scl=Pin(9))
display = SH1106_I2C(128, 64, i2c, Pin(4), 0x3c)

led_red1 = machine.Pin(3, machine.Pin.OUT)
led_red2 = machine.Pin(7, machine.Pin.OUT)
led_red3 = machine.Pin(12, machine.Pin.OUT)
led_red4 = machine.Pin(6, machine.Pin.OUT)

led_green1 = machine.Pin(0, machine.Pin.OUT)
led_green2 = machine.Pin(14, machine.Pin.OUT)
led_green3 = machine.Pin(10, machine.Pin.OUT)
led_green4 = machine.Pin(22, machine.Pin.OUT)

led_yellow1 = machine.Pin(1, machine.Pin.OUT)
led_yellow2 = machine.Pin(18, machine.Pin.OUT)
led_yellow3 = machine.Pin(11, machine.Pin.OUT)
led_yellow4 = machine.Pin(5, machine.Pin.OUT)

def draw_title():
    display.text("Traffic Light", 14, 0, 1)
    display.show()

def draw_static_elements():
    display.vline(63, 9, 22, 1)         # vertikal kiri atas (geser kanan kiri, geser keatas, panjang)
    display.vline(70, 9, 22, 1)         # vertikal kanan atas
    display.vline(70, 37, 25, 1)        # vertikal kanan bawah
    display.vline(63, 37, 25, 1)        # vertikal kiri bawah
    display.hline(19, 30, 45, 1)         # horizontal kiri atas (geser kanan kiri, geser atas bawah, panjang)
    display.hline(19, 37, 45, 1)         # horizontal kiri bawah
    display.hline(70, 37, 43, 1)        # horizontal kanan bawah
    display.hline(70, 30, 43, 1)        # horizontal kanan atas
    display.hline(19, 8, 95, 1)
    display.hline(19, 62, 95 ,1)
    display.vline(19, 8, 55, 1)
    display.vline(113, 8, 55, 1)
    display.show()

def handle_led_red_state13():
    if led_red3.value(1) == led_red1.value(1):
        display.text('M', 53, 40, led_red3.value()) #m3 #(x,y) kanan kiri- atas bawah
        display.text('M', 71, 21, led_red3.value()) #m1
    else:
        display.text('M', 53, 40, led_red3.value()) #m3
        display.text('M', 71, 21, led_red3.value()) #m1
    display.show()
    time.sleep(0.5)

def handle_led_red_alternate_state24():
    if led_red2.value(0) == led_red4.value(0):
        display.text('M', 71, 40, led_red2.value()) #m2
        display.text('M', 53, 21, led_red2.value()) #m4
    else:
        display.text('M', 71, 40, led_red2.value()) #m2
        display.text('M', 53, 21, led_red2.value()) #m3
    display.show()
    time.sleep(0.5)

def handle_led_yellow_state24():
    if led_yellow2.value(1) == led_yellow4.value(1):
        display.text('K', 78, 40, led_yellow2.value()) #k2
        display.text('K', 45, 21, led_yellow2.value()) #k4
    else:
        display.text('K', 78, 40, led_yellow2.value())
        display.text('K', 45, 21, led_yellow2.value())
    display.show()
    time.sleep(0.5)

def handle_led_yellow_alternate_state24():
    if led_yellow2.value(0) == led_yellow4.value(0):
        display.text('K', 78, 40, led_yellow2.value())
        display.text('K', 45, 21, led_yellow2.value())
    else:
        display.text('K', 78, 40, led_yellow2.value())
        display.text('K', 45, 21, led_yellow2.value())
    display.show()
    time.sleep(0.5)
    
def handle_led_green_state24():
    if led_green2.value(1) == led_green4.value(1):
        display.text('H', 83, 40, led_green2.value())
        display.text('H', 40, 21, led_green2.value())
    else:
        display.text('H', 83, 40, led_green2.value())
        display.text('H', 40, 21, led_green2.value())
    display.show()
    time.sleep(1)

def handle_led_green_alternate_state24():
    if led_green2.value(0) == led_green4.value(0):
        display.text('H', 83, 40, led_green2.value())
        display.text('H', 40, 21, led_green2.value())
    else:
        display.text('H', 83, 40, led_green2.value())
        display.text('H', 40, 21, led_green2.value())
    display.show()
    time.sleep(1)

def handle_led_red_alternate_state13():
    if led_red3.value(0) == led_red1.value(0):
        display.text('M', 53, 40, led_red3.value())
        display.text('M', 71, 21, led_red3.value())
    else:
        display.text('M', 53, 40, led_red3.value())
        display.text('M', 71, 21, led_red3.value())
    display.show()
    time.sleep(0.5)

def handle_led_red_state24():
    if led_red2.value(1) == led_red4.value(1):
        display.text('M', 71, 40, led_red2.value())
        display.text('M', 53, 21, led_red2.value())
    else:
        display.text('M', 71, 40, led_red2.value())
        display.text('M', 53, 21, led_red2.value())
    display.show()
    time.sleep(0.5)

def handle_led_yellow_state13():
    if led_yellow3.value(1) == led_yellow1.value(1):
        display.text('K', 53, 43, led_yellow3.value()) #k3
        display.text('K', 71, 14, led_yellow3.value()) #k1
    else:
        display.text('K', 53, 43, led_yellow3.value())
        display.text('K', 71, 14, led_yellow3.value())
    display.show()
    time.sleep(0.5)
    
def handle_led_yellow_alternate_state13():
    if led_yellow3.value(0) == led_yellow1.value(0):
        display.text('K', 53, 43, led_yellow3.value())
        display.text('K', 71, 14, led_yellow3.value())
    else:
        display.text('K', 53, 43, led_yellow3.value())
        display.text('K', 71, 14, led_yellow3.value())
    display.show()
    time.sleep(0.5)

def handle_led_green_state13():
    if led_green3.value(1) == led_green1.value(1):
        display.text('H', 53, 54, led_green3.value()) #h3
        display.text('H', 71, 9, led_green3.value())  #h1
    else:
        display.text('H', 53, 54, led_green3.value())
        display.text('H', 71, 9, led_green3.value())
    display.show()
    time.sleep(1)
    
def handle_led_green_alternate_state13():
    if led_green3.value(0) == led_green1.value(0):
        display.text('H', 53, 54, led_green3.value())
        display.text('H', 71, 9, led_green3.value())
    else:
        display.text('H', 53, 54, led_green3.value())
        display.text('H', 71, 9, led_green3.value())
    display.show()
    time.sleep(1)

while True:
    draw_title()
    draw_static_elements()
    handle_led_red_state13()
    handle_led_red_alternate_state24()
    handle_led_yellow_state24()
    handle_led_yellow_alternate_state24()
    handle_led_green_state24()
    handle_led_green_alternate_state24()
    handle_led_red_alternate_state13()
    handle_led_red_state24()
    handle_led_yellow_state13()
    handle_led_yellow_alternate_state13()
    handle_led_green_state13()
    handle_led_green_alternate_state13()

