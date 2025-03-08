
vocale = "aeiouAEIOU"

input_string = "Salutare, ce mai faci?"

#var1
def elimina_vocala(ch):
   return ch not in vocale

print("".join(filter(elimina_vocala, input_string)))



#var2
print("".join(filter(lambda char: char not in vocale, input_string)))

#var3 list comprehension

print("".join([ch for ch in input_string if ch not in vocale]))
