# by GFG
import re
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
					'C':'-.-.', 'D':'-..', 'E':'.',
					'F':'..-.', 'G':'--.', 'H':'....',
					'I':'..', 'J':'.---', 'K':'-.-',
					'L':'.-..', 'M':'--', 'N':'-.',
					'O':'---', 'P':'.--.', 'Q':'--.-',
					'R':'.-.', 'S':'...', 'T':'-',
					'U':'..-', 'V':'...-', 'W':'.--',
					'X':'-..-', 'Y':'-.--', 'Z':'--..',
					'1':'.----', '2':'..---', '3':'...--',
					'4':'....-', '5':'.....', '6':'-....',
					'7':'--...', '8':'---..', '9':'----.',
					'0':'-----', ', ':'--..--', '.':'.-.-.-',
					'?':'..--..', '/':'-..-.', '-':'-....-',
					'(':'-.--.', ')':'-.--.-'}

def morse_encrypt(message):
	cipher = ''
	for letter in message:
		if letter != ' ':

			cipher += MORSE_CODE_DICT[letter.upper()] + ' '
		else:
			cipher += ' '

	return cipher


def morse_decrypt(message):


	message += ' '

	decipher = ''
	citext = ''
	for letter in message:

		if (letter != ' '):
			i = 0
			citext += letter

		else:
			i += 1

			if i == 2 :

				decipher += ' '
			else:

				decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
				.values()).index(citext)]
				citext = ''

	return decipher


# for camel to snake

def to_camel(txt):
    regex=r"[A-Z]{1}[^\s]{0}[A-za-z\d]+"
    ans= re.fullmatch(regex,txt)
    if (ans):
        res=""
        for i in txt:
            if (i.isupper()):
                res+="_"+i.lower()
            else:
                res+=i
        return res[1:]
    else:
        return "Enter Valid Camelcase"


# for caesar cipher
def encode_caesar(message,key):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) + key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

def decode_caesar(message,key):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) - key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result


# for vugenere cipher
#only work when string is in uppercase
def generateKey(string, key):
	key=key.upper()
	key = list(key)
	if len(string) == len(key):
		return(key)
	else:
		for i in range(len(string) -
					len(key)):
			key.append(key[i % len(key)])
	return("".join(key))
	
def cipherText(string, key):
	cipher_text = []
	for i in range(len(string)):
		x = (ord(string[i]) +
			ord(key[i])) % 26
		x += ord('A')
		cipher_text.append(chr(x))
	return("" . join(cipher_text))

def originalText(cipher_text, key):
	orig_text = []
	for i in range(len(cipher_text)):
		x = (ord(cipher_text[i]) -
			ord(key[i]) + 26) % 26
		x += ord('A')
		orig_text.append(chr(x))
	return("" . join(orig_text))
	

# for emailvalidation
def check_email(txt):
	regex = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
	re_com = re.compile(regex)
	ans= re.fullmatch(re_com,txt)
	# print(ans)
	if ans :
		return True
	else:
		return False

def check_pass(pass1,pass2):
	if (pass1 == pass2):
		regex="[A-Za-z0-9]+[@#%&]+[A-Za-z0-9]{2,10}"
		re_pass = re.compile(regex)
		ans=re.fullmatch(re_pass,pass1)
		if ans:
			return True
		else:
			return False
	else:
		return False









