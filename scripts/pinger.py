import serial
import time

def send_and_get_response(send_cmd, get_response, cmd = "None"):
    if send_cmd == 1:
        command = cmd
        #print(f"Sending command : {command}")
        ser.write(command.encode())

    if get_response == 1:
        time.sleep(0.5)
        response = ser.read(ser.in_waiting)
        resp = response.decode('utf-8')
        #print(f"Response: {resp}")
        return resp
    else:
        return 1

num_iter = 0
max_iter = 30


print("starting")
time.sleep(3)

#Align the modems to ideally face each other
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
if ser.is_open:
    print("Serial port is open")

#Clear the timer
resp1 = send_and_get_response(1,1,"$XTC")

time.sleep(0.25)

while num_iter < max_iter:

    ping_resp = send_and_get_response(1,1,"$P002")
    time.sleep(0.5)

    doit_resp = send_and_get_response(1,1,"$B09Doitbitch ")
    time.sleep(3)
    
    time_bc_resp = send_and_get_response(0,1)
    sent_time_len = int(time_bc_resp[5:7])
    print(sent_time_len)
    sent_time = int(time_bc_resp[7:7+sent_time_len])

    index = time_bc_resp.find("T")
    recieved_time = int(time_bc_resp[index+1:])
    #print("----------------------------------------")
    print(f"difference = {sent_time - recieved_time}")
    #print("----------------------------------------")

ser.close()
