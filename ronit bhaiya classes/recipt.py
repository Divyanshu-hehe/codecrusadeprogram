lays=int(input("enter price"))
kurkure=int(input("enter price"))
brush=int(input("enter price"))
total=lays+kurkure+brush
discount=(total)*10/100
originalprice=total-discount
print(f"lays= {lays} kurkure= {kurkure} brush= {brush} total ={total}  discount ={discount} original ={originalprice}" )