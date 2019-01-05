import string
import random


def random_short_code_generator(size=6, chars = string.ascii_lowercase+string.digits):
	return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=6):
	new_code = random_short_code_generator(size=size)
	# print(new_code)
	# print(instance)
	# print(instance.__class__)
	# print(instance.__class__.__name__)
	Kclass = instance.__class__ # this is kind of importing the class without importing the class
	print(Kclass.objects.filter(shortcode=new_code).exists())
	new_code_exists = Kclass.objects.filter(shortcode=new_code).exists()
	if new_code_exists:
		return create_shortcode(instance, size=size)
	return new_code