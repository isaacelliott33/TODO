
# coding: utf-8

# In[82]:


import csv
with open('output.csv', 'w') as fp1:
    with open("/home/badugi/Desktop/Andrew Schell Work/TODO/TODO_list.csv") as fp:
        for line in fp:
            if line.startswith("- [ ]"):
                line = line.split(" ")
                newline = line[3:]
                TODO = newline[0]
                formattedTODO = TODO[1:]
                if TODO[:5] == '"TODO':
                    sentence = ' '.join(newline[3:])
                    finalline = [formattedTODO, sentence]
                    finalwriter = csv.writer(fp1, delimiter = ',')
                    finalwriter.writerow(finalline) 
                else:
                    sentence = formattedTODO
                    finalline = ["TODO:", ' '.join(newline)]
                    finalwriter = csv.writer(fp1, delimiter = ',')
                    finalwriter.writerow(finalline)             

