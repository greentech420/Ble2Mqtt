# このソースに関する説明

BLEとMQTTを利用したゲートウェイアプリを作成した。

# 各機器の役割
* M5StickC : センサタグとして一定間隔でCO２濃度、温度、湿度をBluetooth送信する。

* RassberryPi : センサタグからの情報をPCに送信する。
　BluetoothとMQTTの変換（中継）としての役割を持つ（ゲートウェイ）

* PC : RassberryPiからの情報（CO2濃度、温度、湿度）をコンソール表示する。
