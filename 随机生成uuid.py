import uuid


def getUUID():
    return "".join(str(uuid.uuid4()).split("-")).upper()


if __name__ == '__main__':
    for i in range(0, 10):
        print(getUUID())
