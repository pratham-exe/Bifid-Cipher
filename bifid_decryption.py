import bifid
import bifid_encryption
sublist = []
for letter in bifid_encryption.final:
    for row in range(5):
        for col in range(5):
            if letter == 'J':
                sublist.extend([2,0])
            elif letter == bifid.table[row][col]:
                sublist.extend([row,col])
            else:
                continue
size = len(sublist)
rowlist = []
collist = []
def splitting(i):
    count = 0
    while i > 0:
        if i == 2:
            rowlist.append(sublist[count])
            count += 1
            collist.append(sublist[count])
            i -= 2
        elif i == 4:
            for _ in range(2):
                rowlist.append(sublist[count])
                count += 1
            for _ in range(2):
                collist.append(sublist[count])
                count += 1
            i -= 4
        elif i == 6:
            for _ in range(3):
                rowlist.append(sublist[count])
                count += 1
            for _ in range(3):
                collist.append(sublist[count])
                count += 1
            i -= 6
        else:
            for _ in range(4):
                rowlist.append(sublist[count])
                count += 1
            for _ in range(4):
                collist.append(sublist[count])
                count += 1
            i -= 8
splitting(size)
output = []
output1 = []
rowsize = len(rowlist)
for i in range(rowsize):
    output.append(bifid.table[rowlist[i]][collist[i]])
for i in range(rowsize):
    if rowlist[i] == 2 and collist[i] == 0:
        output1.append('J')
    else:
        output1.append(bifid.table[rowlist[i]][collist[i]])
key_decrypt = input("\nKey please: ")
if key_decrypt == bifid_encryption.key:
    print("Decrypted word is: ", end="")
    for ouput_letter in output:
        print(ouput_letter, end="")
    print(" / ", end="")
    for output1_letter in output1:
        print(output1_letter, end="")
else:
    print("Sorry! Key not matching.")
