osebe = {"Eva": ["female", "white", "blonde", "blue", "oval"],
          "Larisa": ["female", "white", "brown", "brown", "oval"],
          "Matej": ["male", "white", "black", "blue", "oval"],
          "Miha": ["male", "white", "brown", "green", "square"]
          }

hair = {"black": "CCAGCAATCGC", "brown": "GCCAGTGCCG", "blonde": "TTAGCTATCGC"}
facial_shape = {"square": "GCCACGG", "round": "ACCACAA", "oval": "AGGCCTCA"}
eye_color = {"blue": "TTGTGGTGGC", "green": "GGGAGGTGGC", "brown": "AAGTAGTGAC"}
gender = {"female": "TGAAGGACCTTC", "male": "TGCAGGAACTTC"}
race = {"white": "AAAACCTCA", "black": "CGACTACAG", "asian": "CGCGGGCCG"}

with open("dna.txt", "r") as dna:
    dna = dna.read()

zlocinec = []


for key in gender:
    if gender[key] in dna:
        zlocinec.append(key)

for key in race:
    if race[key] in dna:
        zlocinec.append(key)

for key in hair:
    if hair[key] in dna:
        zlocinec.append(key)

for key in eye_color:
    if eye_color[key] in dna:
        zlocinec.append(key)

for key in facial_shape:
    if facial_shape[key] in dna:
        zlocinec.append(key)
print(f"Karakteristike zločinca so: {zlocinec}")

for ime in osebe:
    if osebe[ime] == zlocinec:
        zlocinec.append(ime)

print(f"Zločincu je ime {zlocinec[5]}.")


