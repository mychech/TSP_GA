import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math
import random

random.seed(42)
matplotlib.rcParams['font.family'] = 'Microsoft YaHei'


# get start points
def get_origin(start_point, point_idx_dict, select_point):
    st_idx = point_idx_dict[start_point]
    select_point_idx = [point_idx_dict[select_point[i]] for i in range(len(select_point)) if i != st_idx]
    return st_idx, select_point_idx


# total distance for signle one
def get_total_distance(x, origin):
    dis = 0
    dis += Distance[x[origin]][x[0]]
    for i in range(len(x) - 1):
        dis += Distance[x[i]][x[i + 1]]
    dis += Distance[x[-1]][x[origin]]
    return dis


# init population
def generate_population(totalNum_population, select_point_idx):
    population = []
    for i in range(totalNum_population):
        # 随机生成个体
        x = select_point_idx.copy()
        random.shuffle(x)  # 随机排序
        population.append(x)
    return population


# Roulette algorithm
def selection(population, origin):
    graded = [[get_total_distance(x, origin), x] for x in population]
    # Calculate fitness
    fit_value = []
    for i in range(len(graded)):
        fit_value.append(1 / graded[i][0] ** 15)
    total_fit = sum(fit_value)

    # Calculate the proportion of each fitness to the total fitness
    newfit_value = [single_fit / total_fit for single_fit in fit_value]

    # Calculate cumulative probability
    t = 0
    for i in range(len(newfit_value)):
        t += newfit_value[i]
        newfit_value[i] = t

    # roulette wheel selection
    ms = [random.random() for _ in range(len(population))]
    ms.sort()
    i = 0
    j = 0
    parents = []
    while i < len(population):
        # Choice - cumulative probability is greater than random probability
        if (ms[i] < newfit_value[j]):
            if population[j] not in parents:
                parents.append(population[j])
            i = i + 1
        # No - cumulative probability is less than random probability
        else:
            j = j + 1

    return parents


# Crossover
def crossover(totalNum_population, parents):
    # The number of offspring is generated to ensure that the population number remains unchanged
    child_count = totalNum_population - len(parents)
    children = []

    while len(children) < child_count:
        # select parent
        mother, father = random.sample(parents, 2)
        popu_size = len(mother)

        # select cross point
        left = random.randint(0, len(mother) - 2)
        right = random.randint(left + 1, len(mother) - 1)

        gene1 = mother[left:right]
        gene2 = father[left:right]

        # reverse
        c1_tmp = mother[right:] + mother[:right]
        c2_tmp = father[right:] + father[:right]
        child1 = c1_tmp.copy()
        child2 = c2_tmp.copy()

        # del duplicate gene
        for o in gene2: c1_tmp.remove(o)

        for o in gene1: c2_tmp.remove(o)

        child1[left:right] = gene2
        child2[left:right] = gene1

        child1[right:] = c1_tmp[0:popu_size - right]
        child1[:left] = c1_tmp[popu_size - right:]

        child2[right:] = c2_tmp[0:popu_size - right]
        child2[:left] = c2_tmp[popu_size - right:]

        children.append(child1)
        children.append(child2)

    return children


# mutation
def mutation(children, mutation_rate=0.1):
    for i in range(len(children)):
        if random.random() < mutation_rate:
            child = children[i]
            u = random.randint(0, len(child) - 2)
            v = random.randint(u + 1, len(child) - 1)
            child_x = child[u + 1:v]
            child_x.reverse()
            children[i] = child[0:u + 1] + child_x + child[v:]


# distance of population with origin start point
def get_result(population, origin):
    graded = [[get_total_distance(x, origin), x] for x in population]
    graded = sorted(graded)
    return graded


def draw(origin, result_path, distance):
    # scatter
    plt.scatter(point_coordinate[:, 0], point_coordinate[:, 1])

    for i in range(len(point_name)):
        plt.text(point_coordinate[i, 0], point_coordinate[i, 1], point_name[i], fontsize="8")

    X = []
    Y = []
    X.append(point_coordinate[origin, 0])
    Y.append(point_coordinate[origin, 1])
    i = 0
    for idx in result_path:
        X.append(point_coordinate[idx, 0])
        Y.append(point_coordinate[idx, 1])
        plt.plot(X, Y, '-')
        plt.text((X[0] + X[1]) / 2, (Y[0] + Y[1]) / 2, i, fontsize='small')

        plt.title("distance = " + str(distance))
        del (X[0])
        del (Y[0])
        i += 1
    X.append(point_coordinate[origin, 0])
    Y.append(point_coordinate[origin, 1])
    plt.text((X[0] + X[1]) / 2, (Y[0] + Y[1]) / 2, i, fontdict={"size": 12})  # 给这个线段表上序号
    plt.plot(X, Y, '-')
    # 起点特别标注
    plt.scatter(point_coordinate[origin, 0], point_coordinate[origin, 1], s=150)


def readDate(filename):
    # 载入数据
    point_name = []
    point_coordinate = []
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if i != 0:
                line = line.split('\n')[0]
                line = line.split(',')
                point_name.append(line[0])
                point_coordinate.append([float(line[1]), float(line[2])])
    point_coordinate = np.array(point_coordinate)

    return point_name, point_coordinate


def getDistanceMatrix(point_count):
    Distance = np.zeros([point_count, point_count])
    for i, pt1 in enumerate(point_coordinate):
        for j, pt2 in enumerate(point_coordinate):
            Distance[i][j] = np.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
    return Distance

if __name__ == '__main__':

    point_name, point_coordinate = readDate('city.csv')

    # distance matrix
    point_count = len(point_name)
    Distance = getDistanceMatrix(point_count)

    # NUmber of population
    totalNum_population = 500
    # Number of evolutions
    itter_time = 400
    # mutation rate
    mutation_rate = 0.9

    # point2idx idx2point
    point_idx_dict = {name: i for i, name in enumerate(point_name)}
    idx_point_dict = {i: name for i, name in enumerate(point_name)}

    # num of output
    output = 1
    select_point = [i for i in point_name]

    # start point and select point index
    origin, select_point_idx = get_origin('长春市', point_idx_dict, select_point)

    # init population
    population = generate_population(totalNum_population, select_point_idx)
    DistanceAndPath = get_result(population, origin)

    # 开始迭代
    register = []
    i = 0
    while i < itter_time:
        # select population to reproduction
        parents = selection(population, origin)
        # Cross reproduction
        children = crossover(totalNum_population, parents)
        # mutation
        mutation(children, mutation_rate)
        # refresh population
        population = parents + children

        # refresh best solutions
        DistanceAndPath = get_result(population, origin)
        register.append(DistanceAndPath[0][0])

        if i == 0 or (i + 1) % 50 == 0:
            for j in range(output):
                result_path = DistanceAndPath[j][1]
                distance = DistanceAndPath[j][0]
                plt.figure(figsize=(14, 6))
                plt.subplot(1, 2, 1)
                draw(origin, result_path, distance)

                plt.subplot(1, 2, 2)
                plt.plot(list(range(len(register))), register)
                plt.title("最优结果变化趋势")
                plt.show()
        i += 1

    result_path_name = []
    result_path_name.append(idx_point_dict[origin])
    for item in DistanceAndPath[0][1]:
        result_path_name.append(idx_point_dict[item])
