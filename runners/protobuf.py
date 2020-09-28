from sets.protobuf import Message, message


def parse(data):
    msg = Message()
    msg.ParseFromString(data)

    return msg


def serialize(msg):
    return msg.SerializeToString()


def run():
    data = serialize(message)
    msg = parse(data)

    # let another circle
    data = serialize(msg)
    parse(data)
