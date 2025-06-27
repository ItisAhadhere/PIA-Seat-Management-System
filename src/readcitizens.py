
file = open("data/isidata.txt", "r+")

'''
count = int(file.readline())
for i in range(count):
    line = file.readline()
    print(line.split())
'''

for line in file:
    print(line)
    
file.close()
