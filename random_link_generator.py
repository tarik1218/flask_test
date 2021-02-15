
#random string üretip döndüren fonksiyon olacak.
import random
import string

def random_link():
    letters_and_digits = string.ascii_lowercase + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(8)))
    return result_str