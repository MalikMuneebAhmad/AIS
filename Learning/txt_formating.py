thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = '2050'

for x,y in thisdict.items():
    txt = "The {} is {}."
    print(txt.format(x,y))
