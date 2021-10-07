name = ("Mohammad", "Ali", "Reza")
family = ("Taghizadeh", "Mohammadi", "Rahimi",  "Felani", "Behamani")

fullname_tuple = zip(name, family, strict=True) # strict(yek dandeh) => ValueError: zip() argument 2 is longer than argument 1
print(list(fullname_tuple))

# C:\Users\Zanis\AppData\Local\Programs\Python\Python37
# name = ["Mohammad", "Ali", "Reza"]
# family = ["Taghizadeh", "Mohammadi", "Rahimi",  "Felani"]

# fullname_tuple = zip(name, family)
# print(list(fullname_tuple))