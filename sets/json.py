import random

point1 = {'x': random.random(), 'y': random.random()}
point2 = {'x': random.random(), 'y': random.random()}
point3 = {'x': random.random(), 'y': random.random()}

line1 = {'fr': point1, 'to': point2}
line2 = {'fr': point2, 'to': point3}
line3 = {'fr': point3, 'to': point1}

struct = {'id': 1, 'text': 'hello'}

message = {
    'score': random.random(),
    'dots': [point1, point2, point3],
    'lines': [line1, line2, line3],
    'struct': struct,
    'description': 'description'
}