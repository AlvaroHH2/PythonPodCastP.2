#Herencia Simple
class X:

    def print_text(self):
        self.var = 10
        print("Esta es la clase Base ")


class Y(X):
    pass
x = X()#Instanciamos
x.print_text()
print(x.var)
print ("\n" + str(x) + "\n") #función str
#función SUper()
class Parent:
  def __init__(self, txt):
    self.message = txt

  def escribirMensaje(self):
    print(self.message)

class Child(Parent):
  def __init__(self, txt):
    super().__init__(txt)

x = Child("Ejemplo super()")
print("La función super() se utiliza para dar acceso a los métodos y propiedades de una clase padre o hermano.")
x.escribirMensaje()



#Herencia Multiple

class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass
