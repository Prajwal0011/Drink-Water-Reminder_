import time
from plyer import notification

while True:
    print("Please drink some water!")
    notification.notify(title = "Please drink some water!",message = "Its time to get hydrated!",)
    time.sleep(10)
