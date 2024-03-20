###################################################################
# M5StickCにSCD40(Grove-CO2 sensor)を接続
# 二酸化炭素濃度、温度、湿度を取得してBLEでアドバタイズ（ブロードキャスト）
# M5StickCは10秒：アドバタイズ、20秒：Deep Sleep
# ラズパイ側は常時スキャンし、データを取得したら一度バイナリに変換し２バイトずつ整数へ変換してからprintする
###################################################################
from bluepy.btle import DefaultDelegate, Scanner, BTLEException
import sys
import struct



class ScanDelegate(DefaultDelegate):
	def __init__(self): # コンストラクタ
		DefaultDelegate.__init__(self)
		#self.lastseq = None
		#self.lasttime = datetime.fromtimestamp(0)
		
	def handleDiscovery(self, dev, isNewDev, isNewData):
		if isNewDev or isNewData:
			for (adtype, desc, value) in dev.getScanData():
				if desc == 'Manufacturer' and value[0:4] == 'ffff':
					data = value[4:]
					result = bytearray.fromhex(data).decode()
					
					self.co2 = int(result[0:4])
					self.tmp = int(result[4:8])
					self.rh = int(result[8:12])
					#print(f"co2[ppm]:{co2}  tmp[°C]:{tmp/100:.1f}  RH[%]:{rh/100:.1f}")
					#print(f"co2[ppm]:{co2}")
if __name__ == "__main__":
	sdgate = ScanDelegate()
	scanner = Scanner().withDelegate(sdgate)
	while True:
		try:
			scanner.scan(5.0) # スキャンする。デバイスを見つけた後の処理はScanDelegateに任せる
			print(f"co2[ppm]:{sdgate.co2}  tmp[°C]:{sdgate.tmp/100:.1f}  RH[%]:{sdgate.rh/100:.1f}")
			
		except BTLEException:
			ex, ms, tb = sys.exc_info()
			print('BLE exception '+str(type(ms)) + ' at ' + sys._getframe().f_code.co_name)
			sys.exit(0)
		
		except Exception as e:
			print(e)
			print("プログラムを終了します…")
		
		