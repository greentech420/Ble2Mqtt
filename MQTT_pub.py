import paho.mqtt.client as mqtt
from time import sleep as wait



class MQTTApplication:
	#コンストラクタ
	def __init__(self, host, port, topic):
		print("MQTT Initiaraze")
		self._host = host
		self._port = port
		self._topic = topic
	
		#クライアントオブジェクト生成
		self.client = mqtt.Client()

		#接続時コールバック関数登録
		self.client.on_connect = self.on_connect

		# 接続
		self.client.connect_async(self._host, port=self._port, keepalive=60)

		
		
		# MQTTクライアント起動
		self.client.loop_start()
	
	#with文によってオブジェクト生成するとき実行する(自身のオブジェクトを戻す)
	def __enter__(self):
		return self
	
	#with文を脱出するときに実行する（後処理を実行する）
	def __exit__(self, exception_type, exception_value, traceback):
		self.close()
		
	def on_connect(self, client, userdata, flags, rc):
		if rc==0:
			print("connection successfull!!")
		else:
			print(f"connected fail with code{rc}")		
		
	def send(self, payload):
		print("MQTT Send...")

		# パブリッシュ（発行）
		self.client.publish(self._topic, payload,qos=1)
		
	def close(self):
		print("MQTT Stop...")
		#　MQTTクライアント停止
		self.client.loop_stop()

		# 切断
		self.client.disconnect()

# 定数定義
host = "localhost"
port = 1883
topic = 'pi/sub'



if __name__=="__main__":
	with MQTTApplication(host, port, topic) as app:
		app.send("Hello MQTT from RaspberryPi!!")


