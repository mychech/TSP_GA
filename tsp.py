import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math
import random

matplotlib.rcParams['font.family'] = 'Microsoft YaHei'


# get start points
def get_origin(point_idx_dict, select_point):
    select_point_idx = [point_idx_dict[select_point[i]] for i in range(1, len(select_point))]
    return point_idx_dict[select_point[0]], select_point_idx


# total distance for signle one
def get_total_distance(x, origin):
    dis = 0
    dis += Distance[origin][x[0]]
    for i in range(len(x) - 1):
        dis += Distance[x[i]][x[i + 1]]
    dis += Distance[origin][x[-1]]
    return dis


# init population
def generate_population(count, select_point_idx):
    population = []
    for i in range(count):
        # 随机生成个体
        x = select_point_idx.copy()
        random.shuffle(x)  # 随机排序
        population.append(x)
    return population


# 自然选择    轮盘赌算法
def selection(population, origin):
    graded = [[get_total_distance(x, origin), x] for x in population]
    # 计算适应度
    fit_value = []  # 存储每个个体的适应度
    for i in range(len(graded)):
        fit_value.append(1 / graded[i][0] ** 15)
    # 适应度总和
    total_fit = 0
    for i in range(len(fit_value)):
        total_fit += fit_value[i]

    # 计算每个适应度占适应度总和的比例
    newfit_value = []  # 储存每个个体轮盘选择的概率
    for i in range(len(fit_value)):
        newfit_value.append(fit_value[i] / total_fit)

    # 计算累计概率
    t = 0
    for i in range(len(newfit_value)):
        t = t + newfit_value[i]
        newfit_value[i] = t

    # 生成随机数序列用于选择和比较
    ms = []  # 随机数序列
    for i in range(len(population)):
        ms.append(random.random())
    ms.sort()

    # 轮盘赌选择法
    i = 0
    j = 0
    parents = []
    while i < len(population):
        # 选择--累积概率大于随机概率
        if (ms[i] < newfit_value[j]):
            if population[j] not in parents:
                parents.append(population[j])
            i = i + 1
        # 不选择--累积概率小于随机概率
        else:
            j = j + 1

    return parents


# 交叉繁殖
def crossover(parents):
    # 生成子代的个数,以此保证种群稳定
    child_count = count - len(parents)
    # 孩子列表
    children = []
    while len(children) < child_count:
        # 随机选择父母
        mother_idx = random.randint(0, len(parents) - 1)
        father_idx = random.randint(0, len(parents) - 1)
        if mother_idx != father_idx:
            mother = parents[mother_idx]
            father = parents[father_idx]

            # 随机选择交叉点
            left = random.randint(0, len(mother) - 2)
            right = random.randint(left + 1, len(mother) - 1)

            # 交叉片段
            gene1 = mother[left:right]
            gene2 = father[left:right]

            child1_c = mother[right:] + mother[:right]
            child2_c = father[right:] + father[:right]
            child1 = child1_c.copy()
            child2 = child2_c.copy()

            for o in gene2:
                child1_c.remove(o)

            for o in gene1:
                child2_c.remove(o)

            child1[left:right] = gene2
            child2[left:right] = gene1

            child1[right:] = child1_c[0:len(child1) - right]
            child1[:left] = child1_c[len(child1) - right:]

            child2[right:] = child2_c[0:len(child1) - right]
            child2[:left] = child2_c[len(child1) - right:]

            children.append(child1)
            children.append(child2)

    return children


# 变异    基因次序片段交换
def mutation(children):
    for i in range(len(children)):
        if random.random() < mutation_rate:
            child = children[i]
            u = random.randint(0, len(child) - 2)
            v = random.randint(u + 1, len(child) - 1)

            child_x = child[u + 1:v]
            child_x.reverse()
            child = child[0:u + 1] + child_x + child[v:]


# 得到最佳纯输出结果
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


if __name__ == '__main__':

    point_name, point_coordinate = readDate('city.csv')

    # distance matrix
    point_count = len(point_name)
    Distance = np.zeros([point_count, point_count])
    for i, pt1 in enumerate(point_coordinate):
        for j, pt2 in enumerate(point_coordinate):
            Distance[i][j] = np.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

    # 种群数
    count = 800
    # 进化次数
    itter_time = 300
    # 变异率
    mutation_rate = 0.1

    # point2idx idx2point
    point_idx_dict = {name: i for i, name in enumerate(point_name)}
    idx_point_dict = {i: name for i, name in enumerate(point_name)}

    # 获得输出方案个数
    output = 1
    select_point = [i for i in point_name]

    # start point and select point index
    origin, select_point_idx = get_origin(point_idx_dict, select_point)

    # init population
    population = generate_population(count, select_point_idx)
    DistanceAndPath = get_result(population, origin)

    # 开始迭代
    register = []
    i = 0
    while i < itter_time:
        # 选择繁殖个体群
        parents = selection(population, origin)
        # 交叉繁殖
        children = crossover(parents)
        # 变异操作
        mutation(children)
        # 更新种群
        population = parents + children
        # 更新最优解

        DistanceAndPath = get_result(population, origin)
        register.append(DistanceAndPath[0][0])
        i += 1

    result_path_name = []
    result_path_name.append(idx_point_dict[origin])
    for item in DistanceAndPath[0][1]:
        result_path_name.append(idx_point_dict[item])

    for j in range(output):
        result_path = DistanceAndPath[j][1]
        distance = DistanceAndPath[j][0]

        plt.figure(j + 1)
        draw(origin, result_path, distance)

        plt.figure(j + 2)
        plt.plot(list(range(len(register))), register)
        plt.title("最优结果变化趋势")
        plt.show()
