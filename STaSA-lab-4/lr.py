import numpy as np
import random as rd
import pandas as pd


class Population:
    def __init__(self, population=None, max_fit=0, avg_fit=0):
        if population is None:
            population = []
        self.X_array = [x for x, y in population]
        self.Y_array = [y for x, y in population]
        self.Fit_array = [fit_function(x, y) for x, y in population]
        self.Max = max_fit
        self.Avg = avg_fit


def fit_function(x, y):
    return -np.log(1 + x ** 2 + y ** 2) + 3


class GeneticAlgorithm:
    def __init__(self, mut_proba=0.25, mut_delta=0.1):
        self.history = []
        self._population_size = 4
        self._mut_proba = mut_proba
        self._mut_delta = mut_delta

    def __call__(self, function, interval, iterations):
        self._interval = interval
        self._function = function
        self._iterations = iterations
        population = self.source_population()
        for i in range(iterations):
            population = self.mutation(self.crossover(self.selection(population)))
            pop = Population(population=population, max_fit=self.__max_fit(population),
                             avg_fit=self.__average_fit(population))
            df = pd.DataFrame(np.transpose(
                np.array([pop.X_array, pop.Y_array, pop.Fit_array, [pop.Max, '', '', None], [pop.Avg, '', '', None]])),
                              columns=['X', 'Y', 'Fit', 'Max', 'Avg'])
            self.history.append(df)
        return self.history

    def source_population(self):
        population = []
        for i in range(0, self._population_size):
            pair = (rd.uniform(self._interval[0], self._interval[1]), rd.uniform(self._interval[0], self._interval[1]))
            population.append(pair)
        return population

    def selection(self, population=None):
        if population is None:
            population = []
        selected_individuals = []
        roulette = self.__create_roulette_wheel(population)
        for i in range(0, 3):
            index = self.__individual_selection(roulette)
            selected_individuals.append(population[index])
            selected_individuals.sort(key=lambda individ: self._function(individ[0], individ[1]), reverse=True)
        return selected_individuals

    def crossover(self, selected_population=None):
        if selected_population is None:
            selected_population = []
        new_population = []
        first_pair = self.__crossover_parents(selected_population[0], selected_population[1])
        second_pair = self.__crossover_parents(selected_population[0], selected_population[2])
        new_population.extend(first_pair)
        new_population.extend(second_pair)
        return new_population

    def mutation(self, crossover_population=None):
        if crossover_population is None:
            crossover_population = []
        mutation_population = []
        for (x, y) in crossover_population:
            mut_x, mut_y = x, y
            if rd.random() <= self._mut_proba:
                mut_x = self.__mutate_gen(x)
            if rd.random() <= self._mut_proba:
                mut_y = self.__mutate_gen(y)
            mutation_population.append((mut_x, mut_y))
        return mutation_population

    @staticmethod
    def __get_sum(population=None):
        if population is None:
            population = []
        fit_population = [fit_function(x, y) for (x, y) in population]
        return sum(fit_population)

    def __average_fit(self, population=None):
        if population is None:
            population = []
        return self.__get_sum(population) / len(population)

    @staticmethod
    def __max_fit(population=None):
        if population is None:
            population = []
        fit_population = [fit_function(x, y) for (x, y) in population]
        return max(fit_population)

    def __create_roulette_wheel(self, population=None):
        if population is None:
            population = []
        roulette = []
        if not population:
            return roulette
        bound = 0
        for (x, y) in population:
            bound += self._function(x, y) / self.__get_sum(population)
            roulette.append(bound)
        return roulette

    @staticmethod
    def __individual_selection(roulette=None):
        if roulette is None:
            roulette = []
        shot = rd.random()
        index = 0
        for proba in roulette:
            if shot <= proba:
                index = roulette.index(proba)
                break
        return index

    @staticmethod
    def __crossover_parents(first_parent=(), second_parent=()):
        first_child = (first_parent[0], second_parent[1])
        second_child = (second_parent[0], first_parent[1])
        return [first_child, second_child]

    def __mutate_gen(self, gen=0):
        if rd.random() < 0.5:
            if gen - self._mut_delta > self._interval[0]:
                gen -= self._mut_delta
        else:
            if gen + self._mut_delta < self._interval[1]:
                gen += self._mut_delta
        return gen


ga = GeneticAlgorithm()
n = ga(function=fit_function, interval=(-2, 2), iterations=10)

for one in n:
    print(one)
