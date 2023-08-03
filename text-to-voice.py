from gtts import gTTS

matn = input("Matne Morede Nazare Khod ra Vared Namaeed: ")

seda = gTTS(matn)

# if seda:.save == x.mp3:
#     seda

save = input("name morede nazar baraye zakhire seda ra elam namaeed: ")
seda.save(save)