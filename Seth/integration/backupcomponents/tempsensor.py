import adafruit_dht


import board

dht = adafruit_dht.DHT22(board.D19)
temperature=dht.temperature
humidity = dht.humidity
print(temperature)
print(humidity)