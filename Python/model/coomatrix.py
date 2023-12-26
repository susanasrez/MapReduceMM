class COOMatrix:

    def __init__(self, elements):
        self.elements = elements
        self.sort_elements()
    
    def sort_elements(self):
        self.elements.sort(key=lambda element: (element[0], element[1]))

    def add_element(self, row, col, value):
        if value != 0:
            self.elements.append((row, col, value))

    def get_elements(self):
        return self.elements

    def display_matrix(self):
        for element in self.elements:
            print(element)

