import sys
 
#usage : python accuracy.py <file>
 
f1 = open(sys.argv[1])
 
count = 0
true = 0
false = 0
sentences = 0
for line in f1:
    if line == '\n' or line.split()==[]:
        sentences+=1
        continue
    count = count + 1
    x = line.strip().split()
    if(x[-1]==x[-2]):
        true=true+1
    else:
        false = false+1
 
#print '#true', '#false', '#total_words', '#sentences'
print("#Result -------------------------")
print('Accuracy                 : ', (100.0*true/count))
print('Correctly tagged words   : ', true)
print('Incorrectly tagged words : ', false)
print('Total words              : ', count)
print('Total sentences          : ', sentences)
#print true, false, count, sentences
 

f1.close()
