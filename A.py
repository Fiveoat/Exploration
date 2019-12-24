cat = {"name" : "cat", "weight" : "fat", "age" : 10}

print(cat)
# cat.clear()
#clears dict contents

cat_2 = cat.copy()
print(cat_2)
#copies dict

print(cat == cat_2)

cats = {}.fromkeys(["cat", "age", "fat", "tacos"], "unknown")
print(cats)
# makes a dict with default values

name = cats.get("name")
print(name)

