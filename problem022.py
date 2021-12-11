with open("p022_names.txt") as file:
    content = file.read()

names = content.split(",")
names = [name[1:-1] for name in names]
sorted_names = sorted(names)
print(sorted_names)
translator = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,
    'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,
    'r':18,'s':19,'t':20,'u':21,'v':22, 'w':23,'x':24,'y':25,'z':26
    }
score = 0
for i,name in enumerate(sorted_names):
    name_score = 0
    name = name.lower()
    for char in name:
        name_score += int(translator[char])
    score += name_score*(i+1)
print(score)