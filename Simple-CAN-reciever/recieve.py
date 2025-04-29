import can

bus = can.interface.SerialBus('COM5', baudrate=250000, channel='can0', receive_own_messages=True)
while True:
    message = bus.recv()
    print(message)
