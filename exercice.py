#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_first_part_of_name(name):
	split_name = name.split("-")
	first_name = split_name[0].capitalize()

	return f"Bonjour, {first_name}"

def get_random_sentence(animals, adjectives, fruits):

	# random numbers
	number_animals = random.randrange(len(animals))
	number_adjectives = random.randrange(len(adjectives))
	number_fruits = random.randrange(len(fruits))

	# choices
	animal = animals[number_animals]
	adjective = adjectives[number_adjectives]
	fruit = fruits[number_fruits]

	return "Aujourd'hui, j'ai vu un {} s'emparer d'un panier {} plein de {}".format(animal, adjective, fruit)

def encrypt(text, shift):
	upper_string = text.upper()
	new_string = ""
	for c in upper_string:
		if 65 <= ord(c) <= 90:
			new_order = ord(c) + shift
			if new_order <= 90:
				new_string += chr(new_order)
			elif new_order > 90:
				new_order -= 90
				new_string += chr(new_order + 64)
		else:
			new_string += c

	return new_string

def decrypt(encrypted_text, shift):
	new_string = ""
	for c in encrypted_text:
		# ne décrypter que les caractères alphabétique
		if 65 <= ord(c) <= 90:
			order = ord(c) - shift
			if 65 <= order <= 90:
				new_string += chr(order)
			elif order < 65:
				new_string += chr(order + 26)
		# ne pas décrypter caractères non alphabétique
		else :
			new_string += c

	return new_string


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
