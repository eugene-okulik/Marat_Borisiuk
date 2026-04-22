class Flowers:

    def __init__(self, name, colour, length, price, avg_lifetime):
        self.name = name
        self.colour = colour
        self.length = length
        self.price = price
        self.avg_lifetime = avg_lifetime


class Roses(Flowers):
    pass


class Irises(Flowers):
    pass


class Peonies(Flowers):
    pass


rose_1 = Roses('rose', 'red', 50, 5, 4)
rose_2 = Roses('rose', 'white', 45, 4.5, 4)
rose_3 = Roses('rose', 'yellow', 40, 4, 4)

iris_1 = Irises('iris', 'blue', 20, 4, 6)
iris_2 = Irises('iris', 'blue', 18, 4, 6)
iris_3 = Irises('iris', 'blue', 15, 4, 6)

peony_1 = Peonies('peony', 'white', 50, 6.5, 12)
peony_2 = Peonies('peony', 'red', 55, 6.5, 12)
peony_3 = Peonies('peony', 'red', 55, 6.5, 12)


class Bouquet():
    def __init__(self, bouquet_name, bouquet_list):
        self.name = bouquet_name
        self.bouquet_list = bouquet_list

    def bouquet_price(self):
        total = 0
        for flower in self.bouquet_list:
            total += flower.price
        return total

    def avg_lifetime_bouquet(self):
        total_lifetime = 0
        for flower in self.bouquet_list:
            total_lifetime += flower.avg_lifetime
        return total_lifetime / len(self.bouquet_list)

    def sort_by_avg_lifetime(self):
        self.bouquet_list.sort(key=lambda flower: flower.avg_lifetime)

    def sort_by_color(self):
        self.bouquet_list.sort(key=lambda flower: flower.colour)

    def sort_by_length(self):
        self.bouquet_list.sort(key=lambda flower: flower.length)

    def sort_by_price(self):
        self.bouquet_list.sort(key=lambda flower: flower.price)

    def search_by_avg_lifetime(self):
        found_flowers = []
        for flower in self.bouquet_list:
            if flower.avg_lifetime == 12:
                found_flowers.append(flower)
        return found_flowers

    def search_by_colour(self):
        found_flowers = []
        for flower in self.bouquet_list:
            if flower.colour == 'red':
                found_flowers.append(flower)
        return found_flowers


bouquet_list_1 = [rose_1, iris_1, peony_1]
bouquet_1 = Bouquet('First Bouquet', bouquet_list_1)
