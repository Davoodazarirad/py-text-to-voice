from gtts import gTTS

matn = input("Matne Morede Nazare Khod ra Vared Namaeed: ")

seda = gTTS(matn)

# if seda:.save == x.mp3:
#     seda
seda.save('seda.mp3')