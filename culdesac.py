
class cul_de_sac:

def __init__(self, num_houses):
self.num_houses = num_houses
self.houses = []

for i in range(num_houses):
self.houses.append(house())

def __str__(self):
output = ""
for i in range(self.num_houses):
output += str(self.houses[i]) + "\n"
return output

def update(self, name1, name2):
for i in range(self.num_houses):
if self.houses[i].name == name1:
self.houses[i].leave()
break
for i in range(self.num_houses):
if self.houses[i].name == name2:
self.houses[i].visit(name1)
break


class house:

def __init__(self):
self.name = None
self.occupants = []

def __str__(self):
output = "House " + str(self.name) + ":\n"
for i in range(len(self.occupants)):
output += " " + self.occupants[i] + "\n"
return output

def leave(self):
self.occupants.pop(0)

def visit(self, name):
self.occupants.append(name)


def main():
num_houses = int(input("Enter a number of houses: "))
cd = cul_de_sac(num_houses)

for i in range(num_houses):
cd.houses[i].name = i
cd.houses[i].occupants = ["Person " + str(i)]

while True:
print(cd)
name1 = input("Enter the name of the first person: ")
name2 = input("Enter the name of the second person: ")
cd.update(name1, name2)
