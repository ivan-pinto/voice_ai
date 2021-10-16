import serial



def send(code):
    """
    :return: True if success, False if fail
    """
    try:
        ser = serial.Serial("COM3", 9600)
        ser.write(code.encode("ascii"))
        result = "Command " + code + " executed."
    except Exception as e:
        print(e)
        result = False
    return result

def choose(query):

    code = "4"

    if 'turn on light' in query:
        code = "1"
    if 'turn off light' in query:
        code = "2"
    if 'room temperature' in query:
        code = "3"
    
    talk = send(code)

    return talk
