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
led_green4 = machine.Pin(26, machine.Pin.OUT)

led_yellow1 = machine.Pin(1, machine.Pin.OUT)
led_yellow2 = machine.Pin(15, machine.Pin.OUT)
led_yellow3 = machine.Pin(11, machine.Pin.OUT)
led_yellow4 = machine.Pin(5, machine.Pin.OUT)

def draw_static_elements():
    display.vline(57, 0, 26, 1)         # vertikal kiri atas (geser kanan kiri, geser keatas, panjang)
    display.vline(73, 0, 26, 1)         # vertikal kanan atas
    display.vline(73, 35, 64, 1)        # vertikal kanan bawah
    display.vline(57, 35, 64, 1)        # vertikal kiri bawah
    display.hline(0, 25, 57, 1)         # horizontal kiri atas (geser kanan kiri, geser atas bawah, panjang)
    display.hline(0, 35, 57, 1)         # horizontal kiri bawah
    display.hline(73, 35, 57, 1)        # horizontal kanan atas
    display.hline(73, 25, 57, 1)
    display.show()

def handle_led_red_state():
    if led_red3.value(1) == led_red1.value(1):
        display.fill_rect(49, 40, 5, 5, led_red3.value())
        display.fill_rect(77, 16, 5, 5, led_red3.value())
    else:
        display.fill_rect(49, 40, 5, 5, led_red3.value())
        display.fill_rect(77, 16, 5, 5, led_red3.value())
    display.show()
    time.sleep(0.5)

def handle_led_red_alternate_state():
    if led_red2.value(0) == led_red4.value(0):
        display.fill_rect(77, 40, 5, 5, led_red2.value())
        display.fill_rect(49, 16, 5, 5, led_red2.value())
    else:
        display.fill_rect(77, 40, 5, 5, led_red2.value())
        display.fill_rect(49, 16, 5, 5, led_red2.value())
    display.show()
    time.sleep(0.5)

def handle_led_yellow_state():
    if led_yellow2.value(1) == led_yellow4.value(1):
        display.fill_rect(85, 40, 5, 5, led_yellow2.value())
        display.fill_rect(41, 16, 5, 5, led_yellow2.value())
    else:
        display.fill_rect(85, 40, 5, 5, led_yellow2.value())
        display.fill_rect(41, 16, 5, 5, led_yellow2.value())
    display.show()
    time.sleep(0.5)

def handle_led_yellow_state1():
    if led_yellow2.value(0) == led_yellow4.value(0):
        display.fill_rect(85, 40, 5, 5, led_yellow2.value())
        display.fill_rect(41, 16, 5, 5, led_yellow2.value())
    else:
        display.fill_rect(85, 40, 5, 5, led_yellow2.value())
        display.fill_rect(41, 16, 5, 5, led_yellow2.value())
    display.show()
    time.sleep(0.5)
    
def handle_led_green_state():
    if led_green2.value(1) == led_green4.value(1):
        display.fill_rect(93, 40, 5, 5, led_green2.value())
        display.fill_rect(33, 16, 5, 5, led_green2.value())
    else:
        display.fill_rect(93, 40, 5, 5, led_green2.value())
        display.fill_rect(33, 16, 5, 5, led_green2.value())
    display.show()
    time.sleep(1)

def handle_led_green_state1():
    if led_green2.value(0) == led_green4.value(0):
        display.fill_rect(93, 40, 5, 5, led_green2.value())
        display.fill_rect(33, 16, 5, 5, led_green2.value())
    else:
        display.fill_rect(93, 40, 5, 5, led_green2.value())
        display.fill_rect(33, 16, 5, 5, led_green2.value())
    display.show()
    time.sleep(1)

def handle_led_red_alternate_state2():
    if led_red3.value(0) == led_red1.value(0):
        display.fill_rect(49, 40, 5, 5, led_red3.value())
        display.fill_rect(77, 16, 5, 5, led_red3.value())
    else:
        display.fill_rect(49, 40, 5, 5, led_red3.value())
        display.fill_rect(77, 16, 5, 5, led_red3.value())
    display.show()
    time.sleep(0.5)

def handle_led_red_alternate_state1():
    if led_red2.value(1) == led_red4.value(1):
        display.fill_rect(77, 40, 5, 5, led_red2.value())
        display.fill_rect(49, 16, 5, 5, led_red2.value())
    else:
        display.fill_rect(77, 40, 5, 5, led_red2.value())
        display.fill_rect(49, 16, 5, 5, led_red2.value())
    display.show()
    time.sleep(0.5)

def handle_led_yellow_alternate_state():
    if led_yellow3.value(1) == led_yellow1.value(1):
        display.fill_rect(49, 48, 5, 5, led_yellow3.value())
        display.fill_rect(77, 8, 5, 5, led_yellow3.value())
    else:
        display.fill_rect(49, 48, 5, 5, led_yellow3.value())
        display.fill_rect(77, 8, 5, 5, led_yellow3.value())
    display.show()
    time.sleep(0.5)
    
def handle_led_yellow_alternate_state2():
    if led_yellow3.value(0) == led_yellow1.value(0):
        display.fill_rect(49, 48, 5, 5, led_yellow3.value())
        display.fill_rect(77, 8, 5, 5, led_yellow3.value())
    else:
        display.fill_rect(49, 48, 5, 5, led_yellow3.value())
        display.fill_rect(77, 8, 5, 5, led_yellow3.value())
    display.show()
    time.sleep(0.5)

def handle_led_green_alternate_state():
    if led_green3.value(1) == led_green1.value(1):
        display.fill_rect(49, 56, 5, 5, led_green3.value())
        display.fill_rect(77, 0, 5, 5, led_green3.value())
    else:
        display.fill_rect(49, 56, 5, 5, led_green3.value())
        display.fill_rect(77, 0, 5, 5, led_green3.value())
    display.show()
    time.sleep(1)
    
def handle_led_green_alternate_state1():
    if led_green3.value(0) == led_green1.value(0):
        display.fill_rect(49, 56, 5, 5, led_green3.value())
        display.fill_rect(77, 0, 5, 5, led_green3.value())
    else:
        display.fill_rect(49, 56, 5, 5, led_green3.value())
        display.fill_rect(77, 0, 5, 5, led_green3.value())
    display.show()
    time.sleep(1)

while True:
    draw_static_elements()
    handle_led_red_state()
    handle_led_red_alternate_state()
    handle_led_yellow_state()
    handle_led_yellow_state1()
    handle_led_green_state()
    handle_led_green_state1()
    handle_led_red_alternate_state2()
    handle_led_red_alternate_state1()
    handle_led_yellow_alternate_state()
    handle_led_yellow_alternate_state2()
    handle_led_green_alternate_state()
    handle_led_green_alternate_state1()
