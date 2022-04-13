from rtde_receive import RTDEReceiveInterface as RTDEReceive
import time
import sys

ROBOT_IP = "192.168.1.112" # ROBOT IP
LOG_FILENAME = "data.csv"  # CSV file 
FREQUENCY = 50.0  # Frequency in Hertz. You can go up to 500Hz.

def main(args):
    dt = 1 / FREQUENCY
    rtde_r = RTDEReceive(ROBOT_IP, FREQUENCY)
    rtde_r.startFileRecording(LOG_FILENAME)
    print("Data recording started, press [Ctrl-C] to end recording.")
    i = 0
    try:
        while True:
            start = time.time()
            if i % 10 == 0:
                sys.stdout.write("\r")
                sys.stdout.write("{:3d} samples.".format(i))
                sys.stdout.flush()
            end = time.time()
            duration = end - start

            if duration < dt:
                time.sleep(dt - duration)
            i += 1

    except KeyboardInterrupt:
        rtde_r.stopFileRecording()
        print("\nData recording stopped.")

if __name__ == "__main__":
    main(sys.argv[1:])