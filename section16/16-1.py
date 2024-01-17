#ans

def caesar_decrypt(ciphertext, shift):

    string = 'abcdefghijklmnopqrstuvwxyz .,-'

    plaintext = ''
    
    for char in ciphertext:
        
        idx = string.find(char)

        decrypted_idx = (idx - shift) % len(string)
        if decrypted_idx < 0:
            decrypted_idx += len(string) 
        elif decrypted_idx > len(string):
            decrypted_idx -= len(string)

        
        decrypted_char = string[decrypted_idx]
        
        plaintext += decrypted_char
    
    return plaintext


ciphertext = "qdq-gi.q-a ziatmxxitmdqibtqi-ustbi ri.qmoqrcxi.qbubu zir -ibtqi-qp-qaai ripmymsqkir -ibtqi-qy dmxi ri.cnxuoi rruoumxakir -ibtqiqzmobyqzbkii-q.qmxi -imyqzpyqzbi rixmeaki -puzmzoqai -i-qscxmbuzaimzpir -i btq-iymbbq-a;iz -iatmxximzgi.q-a zinqiuzimzgiemgipuao-uyuzmbqpimsmuzabir -ia.za -uzsiacotiimi.qbubu zj"
shift = 12
decrypted_text = caesar_decrypt(ciphertext, shift)
print("解読されたテキスト:", decrypted_text)

