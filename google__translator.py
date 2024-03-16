from googletrans import Translator
translater=Translator()
while(1):
    print("*************************")
    destination=input("Enter the conversion language: ")
    inp=input("Enter the input sentence ")
    out=translater.translate(inp,dest=destination)
    print(out)
    print("\n Translation:",out.text)
    