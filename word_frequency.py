name = input("Enter file:")
if len(name) < 1 : name = "try.txt"
handle = open(name)
dic=dict()
for line in handle:
    words=line.split()
    for word in words:
        dic[word]=dic.get(word,0)+1
print("Words with their frequencies")
for word,freq in dic.items():
    print(word,freq)