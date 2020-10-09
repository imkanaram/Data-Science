# class Duck:
#     sound = 'Quaaaaaaaaak!'
#     Walking = 'Walking like a duck.'
#     def quack(self):
#         print(self.sound)

#     def walk(self):
#         print(self.Walking)

# def main():
#     donald = Duck()
#     donald.quack()
#     donald.walk()

# if __name__ == "__main__":
#     main()

#------------------------------------------------------
class Animal:
    def __init__(self, type, name, sound):
        self._type = type
        self._name = name
        self._sound = sound

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): reuires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))

def main():
    a0 = Animal('kitten', 'fluffy', 'rwar')
    a1 = Animal('duck','ram', 'quack')

    print_animal(a0)
    print_animal(a1)    
    print_animal(Animal('hello', 'sdfghj', 'xcvbnm'))

if __name__ == "__main__":
    main()    
