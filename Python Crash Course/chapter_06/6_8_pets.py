"""
6_8_pets.py

Make several dictionaries, where the name of each dictionary is the
name of a pet. In each dictionary, include the kind of animal and the owner’s
name. Store these dictionaries in a list called pets. Next, loop through your list
and as you do print everything you know about each pet.
Created: 1-28-19
@author: Brian Jacobe

"""
Max = {
	"pet_name":"Max",
	"type": "Dog",
	"breed":"Bernese Mountain",
	"age":3,
	}
Luna = {
	"pet_name":"Luna",
	"type": "Dog",
	"breed":"Labrador Retreiver",
	"age":2,
}
Coco = {
	"pet_name":"Coco",
	"type": "Bird",
	"breed":"Cockatiel",
	"age":1,
}

pets = [Max, Luna, Coco]

# Create Pet Class to return Pet description without repeating uncessary print calls

print("Jacobe Family Pets:")
for pet in pets:
	if pet["pet_name"] == "Max":
		print("Pet Name: " + pet["pet_name"])
		print("Type: " + pet["type"])
		print("Breed: " + pet["breed"])
		print("Age: " + str(pet["age"]) + "\n")
	elif pet["pet_name"] == "Luna":
		print("Pet Name: " + pet["pet_name"])
		print("Type: " + pet["type"])
		print("Breed: " + pet["breed"])
		print("Age: " + str(pet["age"]) + "\n")
	elif pet["pet_name"] == "Coco":
		print("Pet Name: " + pet["pet_name"])
		print("Type: " + pet["type"])
		print("Breed: " + pet["breed"])
		print("Age: " + str(pet["age"]) + "\n")
