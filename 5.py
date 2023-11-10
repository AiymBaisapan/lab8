num = ['one', 'two', 'three', 'four', 'five', 'six']
with open('abc.txt', "w") as myfile:
        for c in num:
                myfile.write("%s\n" % c)

content = open('abc.txt')
print(content.read())