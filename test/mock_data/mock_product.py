from apps.products.models import Product, Material, Color


class MockProduct:

    def build_material_JSON(self):
        materials = ["cotton", "linen", "hemp", "polyester", "nylon", "wool", "silk"]

        return [{"material_name": material} for material in materials]

    def build_color_JSON(self):
        colors = ["red", "blue", "green", "orange", "yellow"]
        hex_list = ["FF0000", "0000FF", "00FF00", "FFA500", "FFFF00"]
        return [{"color_name": color, "hex": hex_value} for color, hex_value in zip(colors, hex_list)]

    def create_material(self):
        for material in self.build_material_JSON():
            Material.objects.create(**material)

    def create_color(self):
        for color in self.build_color_JSON():
            Color.objects.create(**color)

    def insert_all(self):
        self.create_material()
        self.create_color()
