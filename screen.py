class Screen:
    def __init__(self, make: str, model: str, serial: str, output_port=""):
        self.make = make
        self.model = model
        self.serial = serial
        self.output_port = output_port

    def __eq__(self, other) -> bool:
        if not isinstance(other, Screen):
            return False
        return self.make == other.make and \
            self.model == other.model and \
            self.serial == other.serial
