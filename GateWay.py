from MQTT_pub import *
from BLE_SCD40 import *

# 定数定義
host = "localhost"
port = 1883
topic = 'pi/sub'

# ここからプログラムを記述します
with MQTTApplication(host, port, topic) as app:
	sdgate = ScanDelegate()
	scanner = Scanner().withDelegate(sdgate)
	
	while True:
		scanner.scan(5.0)
		payload = f"co2[ppm]:{sdgate.co2}  tmp[°C]:{sdgate.tmp/100:.1f}  RH[%]:{sdgate.rh/100:.1f}"
		app.send(payload)
		
	