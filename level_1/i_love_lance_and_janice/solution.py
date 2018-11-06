def answer(encrypted):
	decrypted = ""
	for char in encrypted:
		charCode = ord(char)
		if charCode >= 97 and charCode <= 122: # between a and z
			decrypted += chr(219 - charCode) # 122 - charCode + 97
		else:
			decrypted += char
	return decrypted

	# Can also be done with a one liner
	# return "".join([chr(219 - ord(char)) if (ord(char) >= 97 and ord(char) <= 122) else char for char in encrypted])