alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
textin = str(input("enter text"))
textin = textin.lower()


def decrypt(t,s):
    encrypted = ""
    for char in t:
        if char == " ":
            encrypted = encrypted+" "
        elif char == ".":
            encrypted = encrypted+"."
        elif char == ",":
            encrypted = encrypted+","
        else:
            i = alphabets.index(char) 
            newi = ((i+(-s)+1)%26)-1
            encrypted = encrypted + alphabets[newi]
    return encrypted

def evalulate(x):
    score = 0
    score += (x.count("e")*12) + (x.count("a")*8.49) + (x.count("r")*7.58) + (x.count("i")*7.54) + (x.count("o")*7.16) + (x.count("t")*6.95)
    score += (x.count(" the ")*50) + (x.count(" be ")*25) + (x.count(" to ")*25) + (x.count(" of ")*10) + (x.count(" and ")*10)
    return score


# table generator
index = 1
table_text = []
table_score = []
table_shift = [] 

while index <= 26:
    table_shift.append(index)
    
    tempd = decrypt(textin, index)
    table_text.append(tempd)
    table_score.append(evalulate(tempd))
    
    index += 1
#print(table_score, table_shift, table_text)


#best score sorter 

besti = [0]
i2 = 0
while i2< len(table_score) -1:
    if table_score[i2] >= table_score[besti[-1]]:
        besti.append(i2)
    i2+=1

print(besti)

#printer
print("score-",table_score[besti[-1]], "relitive score-", table_score[besti[-1]] - table_score[besti[-2]] ,"shift key-", table_shift[besti[-1]] ,"decoded text -", table_text[besti[-1]]  )
