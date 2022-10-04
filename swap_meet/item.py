class Item:
    def __init__(self, category='', condition=0, age=None):
        self.category = category
        self.condition = condition
        self.age = age
    def __str__(self):
        return "Hello World!"
    def condition_description(self):
        description_options = ['Poor','Used fair','Used good','Used very good','Used like new', 'New']
        return description_options[self.condition]

    
