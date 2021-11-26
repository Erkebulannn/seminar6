fin=open('mailbox.txt')

lines=fin.readlines()
Erke=[]
file=open('output.txt', 'w')

for line in lines:
   if 'Details:'in line:
     print(line[-6:-1])
     if line not in Erke:

             Erke.append(line[-6:-1])
Erke.sort() 

for item in Erke:
    file.write(item)
    file.write('\n')

fin.close()
file.close()
