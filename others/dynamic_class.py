class FoodType(object):
    events = []

    def __init__(self, ftype, items):
        self.ftype = ftype
        self.items = items
        FoodType.events.append(self)

    def run(self):
        print("Food Type: % s" %(self.ftype))
        print("Food Menu:", self.items)

    @staticmethod
    def run_events():
        for e in FoodType.events:
            e.run()


def sub_food(ftype):
    class_name = ftype.capitalize()

    def __init__(self, items):
        FoodType.__init__(self, ftype, items)
    # dynamic class creation and defining it as a global attribute
    x= globals()
    globals()[class_name] = type(class_name, (FoodType, ), dict(__init__=__init__))
    x = globals()
    pass

if __name__ == "__main__":
    foodType = ["Vegetarian", "Nonvegetarian"]
    foodItems = "Vegetarian(['Spinach', 'Bitter Guard']); Nonvegetarian(['Meat', 'Fish'])"
    # invoking method for dynamic class creation.
    [sub_food(ftype) for ftype in foodType]
    # executing dynamic classes.
    exec(foodItems)
    FoodType.run_events()