from panda3d.core import Vec3


def center(points):
    c = Vec3(0, 0, 0)
    for p in points:
        c += p
    return c / len(points)


def lerp(a, b, t=0.5):
    return a + (b - a) * t


def dot(a, b):
    return a.x * b.x + a.y * b.y + a.z * b.z


def prod(a, b):
    return Vec3(a.x * b.x, a.y * b.y, a.z * b.z)
