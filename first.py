def special_cipher(text,rn):
    cipher = ""
    for ch in text :
        if ch.islower() :
            cipher += chr((ord(ch) + rn-97)%26 + 97)
        else:
            cipher += chr((ord(ch) + rn-65)%26 + 65)
    spe_cipher = ""
    c = 1
    for i in range(len(cipher)-1):
        if cipher[i]==cipher[i+1] :
            c+=1
        else:
            if c>1 :
                spe_cipher += cipher[i]+str(c)
            else:
                spe_cipher += cipher[i]
            c = 1
    if c>1 :
        spe_cipher += cipher[i]+str(c)
    else:
        spe_cipher += cipher[i]
    return spe_cipher
text = input()
rn = int(input())
print("special cipher text for given text",text,"is")
print(special_cipher(text,rn))