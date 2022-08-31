from .point import Point

class Line:
    def __init__(self, a=1, b=1, c=0):
        assert not (a == 0 and b == 0)
        self.a = a
        self.b = b
        self.c = c
        
    def __repr__(self):
        return f"Line[{self.a}x+{self.b}y+{self.c}=0]"
    
    def contains(self, point=Point):
        return self.a*point.x + self.b*point.y + self.c == 0