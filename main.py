people = {"eva": ["female", "white", "blonde", "blue", "oval"],
          "larisa": ["female", "white", "brunette", "brown", "oval"],
          "matej": ["male", "white", "black", "blue", "oval"],
          "miha": ["male", "white", "brunette", "green", "square"]
          }

hair = {"black": "CCAGCAATCGC"}, {"brown": "GCCAGTGCCG"}, {"blonde": "TTAGCTATCGC"}

with open("dna.txt", "r") as dna:
   dna = dna.read()
   print(dna)


for key in hair:
   if hair[key] in dna:
    print(key)