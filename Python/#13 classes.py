
class new:

    def __init__(self):
        pass

    def foots(self, meters):
        self.meters = meters * 3.28084
        return self.meters

    def meters(self, foots):
        self.foots = foots / 3.28084
        return self.foots


if __name__ == '__main__':
    var = new()