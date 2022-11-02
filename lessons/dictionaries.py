"""Demonstrations of dictionary capabolotoes."""


# Declaring the type of a dictionary
schools: dict[str, int]

# Intitialize to an empty dictionary. Can do all in one step, but is done in two here
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19_400
schools["Duke"] = 6_6711
schools["NCSU"] = 26_150

# Print a dictionary literal representation
print(schools)

# access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")  # Used double quotes and then a single quote when needed

# Remove a key-value pair from a dictionary
# by its key
schools.pop("Duke")

# Test for the existance of a key
if "Duke" in schools:
    print("Found the key 'Duke' in schools")
else:
    print("No key 'Duke' found in schools")

# Update / Reassign a key-value pair
schools["UNC"] = 20_000
schools["NCSU"] += 200

print (schools)

# Demonstration of dictionary literals

# Empty dictionary literal
schools = {}  # Same as dict()
print(schools)

# Alternatively, initialize key-value pairs
schools = {
    "UNC": 19_400, 
    "Dukie": 6_717, 
    "NCSU": 26_150
    }
print(schools)

# What happens when a key does not exist?
# print(schools["UNCC"])

# Example looping over the keys of a dict
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")