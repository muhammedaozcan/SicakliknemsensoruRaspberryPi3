import thingspeak
import time
import Adafruit_DHT

kanal_id = 1435518 
write_key = 'PA914YTTHZ74CVXR' 

pin = 16
sensor = Adafruit_DHT.DHT11

def olcum(channel):
    try:
        nem, sicaklik = Adafruit_DHT.read_retry(sensor, pin)
        if nem is not None and sicaklik is not None:
            print('Sicaklik = {0:0.1f}*C Nem = {1:0.1f}%'.format(sicaklik, nem))
        else:
            print('Sensorden herhangi bir veri gelmedi! kontrol ediniz')
        response = channel.update({'field1': sicaklik, 'field2': nem})
    except:
           print("baglanti basarisiz")

if __name__ == "__main__":
        channel = thingspeak.Channel(id=kanal_id, write_key=write_key)
        while True:
            olcum(channel)
            time.sleep(15)

