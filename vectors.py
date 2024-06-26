from math import sqrt

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def Add(vector1, vector2):
    if type(vector1) is Vector2D and type(vector2) is Vector2D:
        return Vector2D(vector1.x + vector2.x, vector1.y + vector2.y)
    elif type(vector1) is Vector3D and type(vector2) is Vector3D:
        return Vector3D(vector1.x + vector2.x, vector1.y + vector2.y, vector1.z + vector2.z)
    else:
        print("Invalid inputs in vector addition!")
    
def Subtract(vector1, vector2):
    if type(vector1) is Vector2D and type(vector2) is Vector2D:
        return Vector2D(vector1.x - vector2.x, vector1.y - vector2.y)
    elif type(vector1) is Vector3D and type(vector2) is Vector3D:
        return Vector3D(vector1.x - vector2.x, vector1.y - vector2.y, vector1.z - vector2.z)
    else:
        print("Invalid inputs in vector subtraction!")

def Multiply(vector, k):
    if type(vector) is Vector2D:
        return Vector2D(vector.x * k, vector.y * k)
    elif type(vector) is Vector3D:
        return Vector3D(vector.x * k, vector.y * k, vector.z * k)
    else:
        print("Invalid inputs in vector multiplication!")

def Dot(vector1, vector2):
    if type(vector1) is Vector2D and type(vector2) is Vector2D:
        return vector1.x * vector2.x + vector1.y * vector2.y
    elif type(vector1) is Vector3D and type(vector2) is Vector3D:
        return vector1.x * vector2.x + vector1.y * vector2.y + vector1.z * vector2.z
    else:
        print("Invalid inputs in vector dot product!")

def Normalize(vector):
    return Multiply(vector, 1/Magnitude(vector))

def Magnitude(vector):
    if type(vector) is Vector2D:
        return sqrt(vector.x**2 + vector.y**2)
    elif type(vector) is Vector3D:
        return sqrt(vector.x**2 + vector.y**2 + vector.z**2)