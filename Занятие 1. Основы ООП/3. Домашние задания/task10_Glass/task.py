class Glass:
    def __init__(self, material):
        self.material = material
    def get_material(self):
         return self.material


if __name__ == "__main__":
    glass_1 = Glass("Стекло")
    print(glass_1.get_material())


