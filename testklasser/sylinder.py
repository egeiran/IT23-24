import math

pi = math.pi

class Sylinder:
    def __init__(self, radius=20, høyde=50) -> None:
        self.radius = radius
        self.høyde = høyde

    def volum(self):
        return pi*self.radius**2*self.høyde
    
    def overflateareal(self):
        return 2*pi*self.radius**2 + 2*pi*self.radius*self.høyde

class TestSylinder:
    def __init__(self) -> None:
        self.sylinder1 = Sylinder(1, 1)
        self.sylinder2 = Sylinder(10, 2)

    def testVolum(self):
        assert self.sylinder1 == pi
        assert self.sylinder2.volum() == 200* pi

    def testOverflateareal(self):
        assert self.sylinder1.overflateareal() == 4 * pi
        assert self.sylinder2.overflateareal() == 220 * pi

    def testMetoder(self):
        print("Tester metoder")
        self.testVolum()
        self.testOverflateareal()

test = TestSylinder()
test.testMetoder()