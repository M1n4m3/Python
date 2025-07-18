class Bird:
    def fly(self):
        print("Bird can fly")

class Plane:
    def fly(self):
        print("Plane can fly")

def test_fly(obj):
    obj.fly()

test_fly(Bird())   # Bird can fly
test_fly(Plane())  # Plane can fly


