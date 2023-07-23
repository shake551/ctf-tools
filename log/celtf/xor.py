import base64


encrypted = "VllRAlMDBAEAAlJbVQAABwULAABTX1IAVFldWQsBVg1TBAUA"
plain = b"e852b4f2-37c0-4403-8df1-faea8805d41b"

encrypted_raw = base64.b64decode(encrypted)

dec_chars = []
for i in range(len(plain)):
    dec = encrypted_raw[i] ^ plain[i]
    dec_char = chr(dec)
    dec_chars.append(dec_char)

print("".join(dec_chars))
