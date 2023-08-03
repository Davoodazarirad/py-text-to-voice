from gtts import gTTS

print("*" * 50)
print("*" * 50)


matn = input("Matne Morede Nazare ra Vared Namaeed: ")

seda = gTTS(matn)

save = input("name file ba pasvand .mp3 baraye zakhire seda: ")
seda.save(save)


print("*" * 50)
print("*" * 50)