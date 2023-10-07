import bifid
plaintext = input("Enter the word to be encrypted : ").upper()
key = input("Enter the key to protect this plaintext word : ")
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
    else:
        for row in range(5):
            for column in range(5):
                if (letter == bifid.table[row][column]):
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
    final.append(bifid.table[sublist[index]][sublist[index+1]])
    index = index + 2
final_size = len(final)
print("Encrypted word is : ",end="")
for final_letter in final:
    print(final_letter,end="")
