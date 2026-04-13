class fan:
    def __init__(self,name,price,brand,power,colour):
        self.name=name
        self.price=price
        self.brand=brand
        self.power=power
        self.colour=colour
s1=fan("pon","fan",7000,"16w","brown")
s2=fan("usha","fan",9000,"15w","white")

print(s1.name)
print(s1.brand)
print(s1.price)
print(s1.power)
print(s1.colour)
print(s2.name)
print(s2.brand)
print(s2.price)
print(s2.colour)
print(s2.power)