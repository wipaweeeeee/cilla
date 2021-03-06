import random
import json

all_food = []
all_adj = []
all_adv = []
all_verb = []
all_object = []

def get_word_list(path, set_name, set_array):
	url = 'data/' + path +'.json'
	with open(url) as data_file:
		data = json.load(data_file)
		for item in data[set_name]: 
			set_array.append(item)

def make_sentence(): 
	get_word_list('foods/menuItems', 'menuItems', all_object)
	get_word_list('objects/objects', 'objects', all_object)
	get_word_list('objects/clothing', 'clothes', all_object)
	get_word_list('words/adjs', 'adjs', all_adj)
	get_word_list('words/adverbs', 'adverbs', all_adv)
	get_word_list('humans/moods', 'moods', all_verb)
	get_word_list('words/encouraging_words', 'encouraging_words', all_verb)

	stuff = random.choice(all_object).encode("utf-8")
	adj = random.choice(all_adj).encode("utf-8")
	adv = random.choice(all_adv).encode("utf-8")
	verb = random.choice(all_verb).encode("utf-8")

	sentence = "make " + adj + " " + stuff + " feel " + adv + " " + verb
	return sentence




