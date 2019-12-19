from collections import OrderedDict

#favorite_languages = OrderedDict()

favorite_languages = {}
favorite_languages["Brian"]="Python"
favorite_languages["Sasha"]="Shell"
favorite_languages["Sophia"]="Java"

for name, languages in favorite_languages.items():
	print(name.title() + "'s favorite language is " + languages.title() + ".")