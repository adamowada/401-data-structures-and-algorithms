class Animal:
    def __init__(self, type_, next_=None):
        self.type = type_
        self.next = next_

class AnimalShelter:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, animal):
        if self.front is None:
            self.front = animal
            self.rear = self.front
        else:
            second = self.rear
            self.rear = animal
            second.next = self.rear

    def dequeue(self, pref=None):
        if pref == None and self.front != None:
            wanted = self.front
            self.front = self.front.next
            wanted.next = None
            return wanted.type
        elif pref == "dog" and self.front != None:
            while self.front.type != "dog":
                self.front = self.front.next
            return self.front.type
        elif pref == "cat" and self.front != None:
            while self.front.type !="cat":
                self.front = self.front.next
            return self.front.type
        else:
            return (f"{pref} is not dog or cat")

brock = Animal("dog")
nuchun = Animal("cat")

house = AnimalShelter()

house.enqueue(brock)
house.enqueue(nuchun)
print(house.dequeue("dog"))
print(house.dequeue("cat"))
