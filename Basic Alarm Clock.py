import time
alarm_time = input("Enter alarm time")
while True:
    current_time = time.strftime("%H:%M:%S")
    print("Current time:", current_time)
    if current_time == alarm_time:
        print("Wake up! Alarm ringing")
        break
    time.sleep(1)
    