class MijnClass:
    def method(self):
        return f'instance method called', self

    @classmethod
    def class_method(cls):
        return f'class_method_called', cls

    @staticmethod
    def static_method():
        return f'static method called'

print('  #instance call  ')
x = MijnClass()
x.method()
print(40 * '*')
print(x.class_method())
print(40 * '*')
print(x.static_method())
print(40 * '*')
print()

print('  #class call  ')
print(MijnClass.class_method())
print(40 * '*')
print(MijnClass.static_method())
print(40 * '*')

#print(Mijnclass.method()) gaat fout want er deze aanroep werkt alleen op een instance.

