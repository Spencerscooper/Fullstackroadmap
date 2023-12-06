#Question: Declare a dictionary with keys as "names and ages as values,
#then loop through all the keys and value and print them as "key:{key},
# value, {value}

bio = {"Spencer": 5, "Sahnu":3, "Jeff" : 2, "Freena": 1}

search = bio.items()
for names in search:
    print(names)

