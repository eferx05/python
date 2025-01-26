faktoriyel=1

sayı=int(input("lütfen faktoriyelini istediğniz sayıyı yazın..."))

for x in range(sayı,0,-1):
    faktoriyel=faktoriyel*x

print(sayı,"sayısının faktöriyeli",faktoriyel)
