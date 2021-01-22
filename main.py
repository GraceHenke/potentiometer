PotentiometerVal = 0

def on_forever():
    global PotentiometerVal
    PotentiometerVal = pins.analog_read_pin(AnalogPin.P2)
    pins.analog_write_pin(AnalogPin.P0, PotentiometerVal)
basic.forever(on_forever)
