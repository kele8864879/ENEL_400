import serial
import time

ser = serial.Serial("/dev/ttyUSB0", 9600)


def main():
    while True:
        data = ser.inWaiting()
        if data != 0:
            recv = ser.read(data)
            print(recv)
            time.sleep(0.1)
        else:
            print("no data")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if ser is not None:
            ser.close()