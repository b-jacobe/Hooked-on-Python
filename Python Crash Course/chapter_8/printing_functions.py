
def print_models(unprinted_designs, completed_models):
	"""Simulate printing design & move to completed model when finished"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print("Printing model: " + current_design)
		completed_models.append(current_design)
	return ""


def show_completed_models(completed_models):
	"""Display completed models that were printed"""
	print("\nThe following models have been printed:")
	for models in completed_models:
		print(models)
	return ""
