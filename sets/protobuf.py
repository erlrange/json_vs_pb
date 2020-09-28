import random
from proto.message_pb2 import Message, Structure, Line, Point

point1 = Point()
point1.x = random.random()
point1.y = random.random()

point2 = Point()
point2.x = random.random()
point2.y = random.random()

point3 = Point()
point3.x = random.random()
point3.y = random.random()

line1 = Line()
line1.fr.CopyFrom(point1)
line1.to.CopyFrom(point2)

line2 = Line()
line2.fr.CopyFrom(point2)
line2.to.CopyFrom(point3)

line3 = Line()
line3.fr.CopyFrom(point3)
line3.to.CopyFrom(point1)


struct = Structure()
struct.id = 1
struct.text = 'hello'


message = Message()
message.score = random.random()
message.dots.extend([point1, point2, point3])
message.lines.extend([line1, line2, line3])
message.struct.CopyFrom(struct)
message.description = 'description'
