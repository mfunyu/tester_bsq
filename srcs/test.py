import sys


class Map():

    def __init__(self):
        self.emp = '.'
        self.obs = 'o'
        self.full = 'x'

        av = sys.argv
        ac = len(av)
        try:
            s = av[1].split('x')
            self.x = int(s[0])
            self.y = int(s[1])
        except:
            exit(0)
        try:
            if ac > 3:
                self.emp = av[3][0]
                self.obs = av[3][1]
                self.full = av[3][2]
        except:
            print("Error: test.py")
            exit(-1)
        self.map = []
        self.read_map()

    def read_map(self):
        with open ("tmp") as f:
            for line in f:
                self.map.append(list(line.strip()))

    def check_map(self):
        self.find_full_size()
        for y in range(self.y):
            cnt = 0
            for x in range(self.x):
                now = self.map[y][x]
                if now == self.obs:
                    cnt = 0
                    continue
                cnt = cnt + 1
                if cnt > self.sq_max:
                    ret = self.bigger_sq_found(cnt, y, x)
                    if ret:
                        print ("Error: wrong answer")
                        exit(1)
                    x = x - cnt + 2
                    cnt = 0

    def bigger_sq_found(self, cnt, y, x):
        x = x - cnt + 1
        # print(cnt, y, x)
        if y + cnt >= self.y:
            return False
        j = 0
        while j < cnt:
            i = 0
            while i < cnt:
                if self.map[y+i][x+j] == self.obs:
                    return False
                i = i + 1
            j = j + 1
        return True


    def find_full_size(self):
        y, x = self.find_full_lefttop()
        sq_size = 0
        while x < self.x:
            if self.map[y][x] != self.full:
                break
            sq_size = sq_size + 1
            x = x + 1
        self.sq_max = sq_size
        # print (self.sq_max)

    def find_full_lefttop(self):
        for y in range(self.y):
            for x in range(self.x):
                now = self.map[y][x]
                if now == self.full:
                    return y, x
        return self.y, self.x


def main():
    map = Map()
    map.check_map()
    return (0)

if __name__ == "__main__":
    main()
