import base64
encrypted = "P0YFHAciCxIHSE5+QVEOFiQPFVNDTmMCGQUIJA8GAQpJZFtWTgEyGgQRAgsgRlpJQyQIBxsdGjdG VlNEZgcPFx0LIAgUBQFmQkFTDg0sCBMfASwLDwBITn5BURwKLQECHwoKY01WThYgDAMdGx1jQUxJ QzIPBxFIQmRGEAYLZk5bVEgZLQ9XThk="
my_eyes = str.encode("DavidAnaton")
decoded = base64.b64decode(encrypted)
decrypted = "".join([chr((my_eyes[i%len(my_eyes)] ^ decoded[i])) for i in range(0,len(decoded))])
print(decrypted)