# battery.py
import psutil
from plyer import notification

def check_battery():
    battery = psutil.sensors_battery()
    if battery:
        if battery.percent <= 20 and not battery.power_plugged:
            # Display a system notification if the battery is low and not charging
            notification.notify(
                title="Caffeine 2.0: Battery Low",
                message=f"🪫: {battery.percent}%. It is recommended you either plug the laptop in or turn off caffeine to save power",
                timeout=10
            )
