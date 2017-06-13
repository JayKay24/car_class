class Car:
    """
    This class takes in arguments that depict the type, model and name
    of the vehicle and can be used to instantiate various vehicles.
    """
    def __init__(self, name='General', model='GM', car_type=''):
        self.name = name
        self.speed = 0
        self.num_of_doors = 4
        # Only two doors for Porsche and Koenigsegg.
        if self.name in ['Porshe', 'Koenigsegg']:
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4
        self.model = model
        self.saloon = False
        self.car_type = car_type
        # Eight wheels if the type of car is a trailer.
        if self.car_type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4
        
    def is_saloon(self):
        """
        Return the True if the car is a saloon, otherwise
        return False.
        """
        # The car is a saloon if it has 4 wheels.
        if self.num_of_wheels == 4:
            self.saloon = True
        return self.saloon
        
    def drive(self, value):
        """
        Accelerate and increase the car speed using a given value.
        """
        if self.car_type == 'trailer':
            self.speed = (value * 11)
        else:
            self.speed = round(value * 333.333)
        return self