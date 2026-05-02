import time, datetime
alarm = input("time (HH:MM): ")
print("waiting for alarm...")
while True:
    now = datetime.datetime.now().strftime("%H:%M")
    if now == alarm:
        print("WAKE UP! Alarm ringing!")
        for _ in range(5):
            print("a", end="", flush=True)
            time.sleep(1)
        break
    time.sleep(10)