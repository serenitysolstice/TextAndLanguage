import json

with open("words.txt", "r") as file:
	words = file.read().split('\n')
	
for word in words:
	print(word)
	decision = input("Is this word easily understood? Y/N")
	if decision == "N" or decision == "n":
		words.remove(word)
	else:
		continue

with open("final_words.txt", "w") as f:
	file.write(words)