import serial
import time


def send(code):
    """
    :return: Command if success, False if fail or Command 404
    """
    try:
        ser = serial.Serial("COM3", 9600)
        ser.write(code.encode("ascii"))
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
        ser = serial.Serial("COM3", 9600)
        result = ser.readline()
    except Exception as e:
        print(e)
        result = False
    return result

def choose(query):

    code = "404"

    if 'turn on board led' in query:
        code = "33"
    if 'turn on light' in query:
        code = "55"
    if 'more light' in query:
        code = "48"
    if 'less light' in query:
        code = "24"
    
    talk = send(code)

    return talk

# ! - 33
# 7 - 55
if __name__ == "__main__":
    ser = serial.Serial("COM3", 9600)
    while True:
        ser.write('7'.encode("ascii"))
        time.sleep(2)

