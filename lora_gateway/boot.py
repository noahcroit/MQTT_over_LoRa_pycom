import machine
import uos
import pycom
from network import WLAN


uart = machine.UART(0, 115200)
uos.dupterm(uart)

pycom.heartbeat(False)

# WIFI initialize
pycom.rgbled(0x7F0000)  # RED LED
wlan = WLAN(mode=WLAN.STA)
"""
wlan_ssid = "ASUS_for_ICT"
wlan_pwd  = "ictadmin"
"""
wlan_ssid = "KDS_A"
wlan_pwd  = "jo123thai"
wlan.connect(wlan_ssid, auth=(WLAN.WPA2, wlan_pwd), timeout=5000)
while not wlan.isconnected():  
    machine.idle()
print("Connected to WiFi\n")
pycom.rgbled(0x007F00)  # GREEN LED
