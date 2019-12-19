"""
8_13_user_profile.py

Start with a copy of user_profile.py from page 153. Build
a profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you.

Created: 2-14-19
@author: Brian Jacobe

"""

def build_profile(first, last, **user_info):
	profile = {}
	profile['first'] = first
	profile['last'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

b_user = build_profile('Brian', 'Jacobe', age=27, occupation='Software Engineer', countries_traveled=6)
k_user = build_profile('Khia', 'Bautista', age=26, occupation='Teacher', countries_traveled=12)

print(b_user)
print(k_user)