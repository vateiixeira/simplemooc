import random
import hashlib
import string

#CRIA UMA HASH PARA SER USADA NO RESET DA SENHA

# def random_key(size=5):
#     chars = string.ascii_uppercase + string.digits
#     return ''.join(random.choice(chars) for x in range(size))
#
#
# def generate_hash_key(salt, random_str_size=5):
#     random_str = random_key(random_str_size)
#     text = random_str + salt
#     return hashlib.sha224(text.endcode('utf-8')).hexdigest()

def generate_hash_key():
    hash = random.getrandbits(128)
    return hash