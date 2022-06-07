class Audi:
    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max = max_speed
        self.color = color
    def start_engine(self):
        print(f"{self.title} {self.model} start engine ")
    def stop_engine(self):
        print(f"{self.title} {self.model} stop engine ")
    def info(self):

        print(f"title:{self.title}\n"
          f"model:{self.model}\n"
          f"weight:{self.weight}\n"
          f"hp:{self.hp}\n"
          f"nm:{self.nm}\n"
          f"max speed:{self.max}\n"
          f"color:{self.color}\n")
Car = Audi('Audi', 'R8', 1500, 560, 700, 280, "black")
Car.start_engine()
Car.stop_engine()
Car.info()

































