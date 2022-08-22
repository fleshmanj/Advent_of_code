import random
import pandas as pd


class GeneticPool:

    def __int__(self, population_size, start, generations):
        self.generations = generations
        self.population_size = population_size
        self.best_child = None
        self.mutation_rate = .03
        pass

    def access_score(self, child, matrix: pd.DataFrame):
        start = 0
        dist = 0
        for i, place in enumerate(child):
            dist += int(matrix.iloc[place][child[start]])
            start = i

        return dist

    def make_child(self):
        values = [0, 1, 2, 3, 4, 5, 6, 7]

        parent1 = random.sample(values, 4)

        parent1_values = []
        for i in parent1:
            parent1_values.append(self.best_child[i])

        missing = []
        for value in values:
            if value not in parent1_values:
                missing.append(value)

        parent2 = random.sample(missing, 4)

        child = []

        for i in range(8):
            if i in parent1:
                trait = self.best_child[i]
                child.append(trait)
            else:
                trait = parent2.pop()
                child.append(trait)
        return child

    def make_gnome(self):
        child = random.sample(range(0, 8), 8)
        self.best_child = child
        return child

    def mutate(self, child):
        a, b = random.sample(range(0, 8), 2)
        child[a], child[b] = child[b], child[a]
        return child

    def run_iterations(self, matrix):
        self.make_gnome()
        current_score = None
        for _ in range(self.generations):
            population = [self.make_child() for _ in range(self.population_size)]
            for i, child in enumerate(population):
                if (len(population) - i) / len(population) < self.mutation_rate:
                    child = self.mutate(child)
                if current_score is None:
                    current_score = self.access_score(child, matrix)
                if self.access_score(child, matrix) > current_score:
                    current_score = self.access_score(child, matrix)
                    self.best_child = child
            print(current_score, self.best_child)
        return current_score

