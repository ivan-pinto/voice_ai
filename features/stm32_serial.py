import serial
import time

ser = serial.Serial("COM3", 9600)

def send(code):
    """
    :return: Command if success, False if fail or Command 404
    """
    try:
        ser.write(code.encode("ascii"))
        time.sleep(2)
        result = "Command " + code + " executed."
    except Exception as e:
        print(e)
        result = False
    return result

def receive():
    """
    :return: True if success, False if fail
    """
    try:
        result = ser.readline()
    except Exception as e:
        print(e)
        result = False
    return result

# ! - 33
# 7 - 55
# 8 - 56
# 9 - 57
def choose(query):

    code = "404"

    if 'turn on lamp two' in query:
        code = "!"
    if 'turn on lamp one' in query:
        code = "7"
    if 'brighter' in query:
        code = "8"
    if 'darker' in query:
        code = "9"
    
    talk = send(code)

    return talk