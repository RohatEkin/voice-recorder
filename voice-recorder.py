import sounddevice as sd
import wavio as wv

print("Varsayılan giriş cihazı bilgileri:")
print(sd.query_devices(sd.default.device[0], kind='input'))
cevap = input("cihazı değiştirmek ister misiniz(Y/N)")
def cihaz():
    match cevap:
        case "Y":
            devices = sd.query_devices()
            input_devices = {i: d['name'] for i, d in enumerate(devices) if d['max_input_channels'] > 0}
            print("Mevcut giriş cihazları:")
            for i, name in input_devices.items():
                print(f"{i}: {name}")
            device_id = int(input("Kullanmak istediğiniz mikrofonun ID’sini girin: "))
            sd.default.device = (device_id, None)
            print(f" Varsayılan mikrofon: {devices[device_id]['name']}")


        case "N":
            return "Aynı cihazla devam ediyoruz"
cihaz()
dosya = input("dosya hangi isimle kaydedilsin")
saniye = int(input("kaç saniyelik kayıt yapmak istiyosunuz: "))

print("kayıt başladı")
fs = 44100
duration = saniye

myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
sd.wait()
wv.write(dosya+".wav", myrecording, fs, sampwidth=2)
print("kayıt tamamlandı")






