y = input("Janub 'J'\nShimol 'S'\nSharq 'Q'\nG'arb 'G'\nYo'nalishni kirit>> ")
k = input("ongga buril '0'\nchapga buril '1'\n180 gradusga buril '2'\nBurulush burchagi>> ")
m = ''
match y:
    case 'j':m = "Junub"
    case 's':m = "Shimol"
    case 'q':m = "Sharq"
    case "g":m = "G'arb"
print(m,"dan",end=" ")
d = ' '
match int(k):
    case 0:d = "ongga buril"
    case 1:d = "Chapga buril"
    case 2:d = "180 gradusga buril"
print(f"{d} di")

