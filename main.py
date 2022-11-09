import tkinter as tk

def encrypt(text):
    tegn = "abcdefjhijklmnopqrstuvwqyzæøåABCDEFGHIJKLMNOPQRSTUVWQYZÆØÅ01234567890 ,.-!=+?"
    crypt_tegn = "NOPQRSTUVWQYZÆØÅ01234567890 ,.-!=+?abcdefjhijklmnopqrstuvwqyzæøåABCDEFGHIJKLM"
    encrypted_text = ""
    for i in text:
        for n, j in enumerate(tegn):
            if i == j:
                encrypted_text += crypt_tegn[n]
    return encrypted_text

def decrypt(text):
    tegn1 ="NOPQRSTUVWQYZÆØÅ01234567890 ,.-!=+?abcdefjhijklmnopqrstuvwqyzæøåABCDEFGHIJKLM"
    crypted_tegn = "abcdefjhijklmnopqrstuvwqyzæøåABCDEFGHIJKLMNOPQRSTUVWQYZÆØÅ01234567890 ,.-!=+?"
    
    decrypted_text = ""
    for i in text:
        for n, j in enumerate(tegn1):
            if i == j:
                decrypted_text += crypted_tegn[n]
    return decrypted_text
def cryptbutton():
    tekst = tekstVindu.get()
    cryptert = encrypt(tekst)
    encryptedVindu.delete(0,"end")
    encryptedVindu.insert(0,cryptert)

def decryptbutton():
    tekst = tekstVindu.get()
    decryptert = decrypt(tekst)
    encryptedVindu.delete(0,"end")
    encryptedVindu.insert(0,decryptert)

root = tk.Tk()

tekstVindu = tk.Entry(root, font = ("Arial", 20))
tekstVindu.grid(row = 0, column = 0, columnspan = 4,)

encryptedVindu =tk.Entry(root, font= ("Arial", 20))
encryptedVindu.grid(row= 1, column= 0, columnspan = 4)

cryptButton = tk.Button(root, text = "encrypt", font = ("Arial, 20"), command = cryptbutton)
cryptButton.grid(row = 2, column = 0, sticky = "we")

decryptButton = tk.Button(root, text = "Decrypt", font = ("Arial, 20"),command = decryptbutton)
decryptButton.grid(row = 2, column = 1, sticky = "we")


root.mainloop()






