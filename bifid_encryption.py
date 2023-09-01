import random
symbols = ['.','?','!',',','/']
table = [['B','G','W','K','Z'],
         ['Q','P','N','D','S'],
         ['I','O','A','X','E'],
         ['F','C','L','U','M'],
         ['T','H','Y','V','R']]
plaintext = input("Enter the word to be encrypted : ").upper()
plainlist = []
rowlist = []
columnlist = []
sublist = []
for letter in plaintext:
    plainlist.append(letter)
for letter in plainlist:
    if letter == 'J':
        rowlist.append(2)
        columnlist.append(0)
    elif letter in symbols:
        rowlist.append(random.choice(range(5)))
        columnlist.append(random.choice(range(5)))
    else:
        for row in range(5):
            for column in range(5):
                if (letter == table[row][column]):
                    rowlist.append(row)
                    columnlist.append(column)
row_size = len(rowlist)
col_size = len(columnlist)
i = 0
while (i <= row_size):
    for subrow in range(4):
        if subrow+i < row_size:
            sublist.append(rowlist[subrow+i])
        else:
            continue
    for subcol in range(4):
        if subcol+i < row_size:
            sublist.append(columnlist[subcol+i])
        else:
            continue
    i = i + 4
sub_size = len(sublist)
index = 0
final = []
while (index < sub_size):
    final.append(table[sublist[index]][sublist[index+1]])
    index = index + 2
final_size = len(final)
print("Encrypted word is : ",end="")
j = 0
output = []
while (j <= final_size):
    for final_row in range(4):
        if final_row+j < final_size:
           output.append(final[final_row+j]) 
        else:
            continue
    output.append(" ")
    j = j + 4
for final_letter in output:
    print(final_letter,end="")
