import sys

class Map():

    def __init__(self, x, y, emp, obs, full):
        self.emp = emp
        self.obs = obs
        self.full = full

        self.x = int(x)
        self.y = int(y)
        self.map = []

    def read_map(self, cnt):
        with open ("tmp") as f:
            for line in f:
                if line == '\n':
                    if cnt <= 0:
                        break
                    cnt = cnt - 1
                    continue
                if cnt > 0:
                    continue
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
                        # print(y, x)
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
                # print (self.map[y+i][x+j], end="")
                if self.map[y+i][x+j] == self.obs:
                    return False
                i = i + 1
            # print ()
            j = j + 1
        # print(y+i, x+j)
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

    def __str__(self):
        str = ""
        for line in self.map:
            str = str + ' '.join(line) + '\n'
        return str

def main():
    av = sys.argv
    ac = len(av)

    start = 1
    emp = '.'
    obs = 'o'
    full = 'x'
    if av[1][0] < '0' or '9' < av[1][0]:
        emp = av[1][0]
        obs = av[1][1]
        full = av[1][2]
        start = start + 1
    cnt = 0
    for i in range(start, ac):
        s = av[i].split('x')
        try:
            map = Map(s[0], s[1], emp, obs, full)
            map.read_map(cnt)
            # print (map)
            map.check_map()
        except:
            exit(2)
        cnt = cnt + 1
    return (0)

if __name__ == "__main__":
    main()
