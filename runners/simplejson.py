import simplejson as json
from sets.json import message


def parse(data):
    return json.loads(data)


def serialize(msg):
    return json.dumps(msg)


def run():
    data = serialize(message)
    msg = parse(data)

    # lets do another circle
    data = serialize(msg)
    parse(data)

