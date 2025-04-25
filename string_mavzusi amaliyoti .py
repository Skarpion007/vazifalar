kocha = "Bog'bon"

mahalla = "Sog'bon"

tuman = "Bodomzor" 

viloyat = "Samarqand"

print(f"{kocha} kochasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")


kocha = input("kochangiz nomini kiriting\n>>")

mahalla = input("mahallangiz nomini kiriting\n>>")

tuman = input("tumaningiz nomini kiriting\n>>") 

viloyat =input("viloyatiniz nomini kiriting\n>>")

yangi_manzil = f"{kocha.title()} kochasi, {mahalla.lower()} mahallasi, {tuman.upper()} tumani, {viloyat.capitalize()} viloyati"

print(f"Sizning manzilingiz: {kocha} kochasi, {mahalla} mahallasi {tuman} tumani {viloyat} vilayati")

print(f"siznining yangi manzilingiz: {yangi_manzil}")