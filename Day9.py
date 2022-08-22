# Python3 program to implement traveling salesman
# problem using naive approach.
from sys import maxsize
from itertools import permutations
import pandas as pd
from My_genetic import GeneticPool

pd.options.display.max_columns = 10
pd.options.display.width = 500

input_string = """Faerun to Norrath = 129
Faerun to Tristram = 58
Faerun to AlphaCentauri = 13
Faerun to Arbre = 24
Faerun to Snowdin = 60
Faerun to Tambi = 71
Faerun to Straylight = 67
Norrath to Tristram = 142
Norrath to AlphaCentauri = 15
Norrath to Arbre = 135
Norrath to Snowdin = 75
Norrath to Tambi = 82
Norrath to Straylight = 54
Tristram to AlphaCentauri = 118
Tristram to Arbre = 122
Tristram to Snowdin = 103
Tristram to Tambi = 49
Tristram to Straylight = 97
AlphaCentauri to Arbre = 116
AlphaCentauri to Snowdin = 12
AlphaCentauri to Tambi = 18
AlphaCentauri to Straylight = 91
Arbre to Snowdin = 129
Arbre to Tambi = 53
Arbre to Straylight = 40
Snowdin to Tambi = 15
Snowdin to Straylight = 99
Tambi to Straylight = 70"""


def make_list_of_locations(places_list):
    places = []
    for i in places_list:
        list_of_possible_places = i.split()
        places.append(list_of_possible_places[0])
        places.append(list_of_possible_places[2])
    places = set(places)
    return places


def make_matrix(list_of_data: list, places):
    # df = pd.DataFrame()
    vertices = list(places)
    # df.columns = places
    list_of_series = []
    for vert in vertices:
        series = {}
        for i in list_of_data:
            i = i.split()
            if vert in i:
                if vert == i[0]:
                    series[i[2]] = i[4]
                else:
                    series[i[0]] = i[4]
        series[vert] = 0
        new_series = pd.Series(series, index=places, name=vert)
        list_of_series.append(new_series)
    df = pd.concat(list_of_series, axis=1)
    return df


locations = input_string.split("\n")
# print(make_list_of_locations(locations))
matrix = make_matrix(locations, make_list_of_locations(locations))

matrix = matrix.reindex(sorted(matrix.columns), axis=1)
matrix = matrix.sort_index()
print(matrix)

pool = GeneticPool()
pool.population_size = 1000
pool.generations = 100
pool.mutation_rate = 0.10
test = [7, 3, 2, 0, 6, 5, 4, 1]
score = pool.access_score(test,matrix)
print(score)
print(142+129+71+70+99+129+122)
score = pool.run_iterations(matrix)
print(score, pool.best_child)


