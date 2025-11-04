# r = Dosyayi okuma modunda aciyor
# w = Dosyayi yazma modunda aciyor
# a = Verilere dokumadan kaldigi yerden yazi eklemesini yapiyor
# rb = Resimleri goruntuleme modunda aciyor
# wb = Resimlerin uzerine yazi yazma modunda aciyor

f = open("test.txt", "r", encoding="utf-8")
yazi_sonucu = f.read()
print(yazi_sonucu)
f.close

t = open("muhit.txt", "w", encoding="utf-8")
yazi = "Evet hayir biz grubu kasarli kofte karpuz fasulye efendim kedi armut"
t.write(yazi)
t.close

t = open("muhit.txt", "r", encoding="utf-8")
b = t.read()
print(b)
t.close

c = open("muhit.txt", "r", encoding="utf-8")
yeni_yazi = "testimiz basarili mi?"
c.write(yeni_yazi)
c.close

t = open("muhit.txt", "r", encoding="utf-8")
b = t.read()
print(b)
t.close






