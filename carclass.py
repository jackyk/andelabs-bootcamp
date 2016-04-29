class Car:
    my_cars=[
        ("racer","audi"),
        ("sport","tesla"),
        ("family","lambogini")]

    def __init__(self,model,veh_name):
        self.model = model
        self.veh_name = veh_name

    def name_car(self):
        return "My car is a {} and its called {}".format(self.model,self.veh_name)
