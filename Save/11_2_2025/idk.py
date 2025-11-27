s = "### idk lol ###"
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.strip('#'))
print(s.lstrip('#'))
print(s.rstrip('#'))
print(s.replace("###", "").strip())
print(s.find("idk"))
print(s.find("sick my duck"))
print(s.index("lol"))
#print(s.index("sick my duck")) #ValueError
print("-".join(s.split()))