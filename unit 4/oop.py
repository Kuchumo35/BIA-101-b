class Dog:
    def _init_(self, breed, age, color):
        self.breed = breed
        self.age = age
        self.color = color

    def say_age(self):
        words_to_say = "I am " + str(self.age) + " years old"
        print(words_to_say)

    def introduce(self):
        print("Hi")
        print("I am a " +  self.breed + " dog")
        print("I am " + str(self.age) + " dog years old")  
        print("I am "+ self.color + " in color")

    def bark(self):
        print('Woof woof')
    
    def sleep(self):
        print('Zzzzzz')
    
    def eat(self):
        print('i am eating')


dog = Dog('bhutanese', 20, 'black')
petdog = Dog('pug', 10, 'white')
my_friend_dog = Dog('german shephard', 15, 'brown')

dog.say_age()
petdog.say_age()
my_friend_dog.say_age()

dog.introduce()