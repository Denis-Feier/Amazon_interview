from math import sqrt


class TwoDSpace:
    def __init__(self, space, origin=(0, 0)):
        self.space = space
        self.origin = origin
        self.dis = []
        for point in space:
            self.dis.append(sqrt((origin[0] - point[0])**2 + (origin[1] - point[1])**2))

    def __str__(self):
        return "Origin: " + str(self.origin) + "\nSpace: " + str(self.space)

    def solve_prob(self, n):
        aux_dis = self.dis.copy()
        for i in range(n):
            minim = aux_dis[0]
            index = 0
            for j in range(len(aux_dis)):
                if minim > aux_dis[j] and -1 < aux_dis[j]:
                    minim = aux_dis[j]
                    index = j
            print(minim, self.space[index])
            aux_dis[index] = -1


def main():
    p1 = TwoDSpace([(4, 4), (0, 1), (1, 1), (2, 1), (2, 2), (3, 1)])
    p1.solve_prob(7)
    #print(p1)
    print(p1.dis)

if __name__ == '__main__':
    main()
