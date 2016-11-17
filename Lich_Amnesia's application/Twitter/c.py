

class Solution(object):
    """docstring for Solution"""

    def __init__(self):
        # Store the begin time and end time of the interval
        self.begin = 0
        self.end = 0
        # dic is to store the month record in the map.
        # like {'2015-11': {' impressions': 222, ' clicks': 232}}
        # The time-Record map. The record is also a map.
        self.dic = {}
        # Store the time in the interval, and help the output in order
        self.time_list = set([])
        self.readInput()

    # get input of the problem
    def readInput(self):
        interval = raw_input()
        self.begin, self.end = interval.split()
        self.begin = self.begin[:-1]
        line = raw_input()
        line = raw_input()
        while True:
            try:
                self.handle(line)
                line = raw_input()
            except (EOFError):
                break

    # Put the record data in the map.
    def handle(self, line):
        time_, type_, num = line.split(',')
        time_ = time_.rsplit('-', 1)[0]
        num = int(num)
        if time_ >= self.begin and time_ < self.end:
            self.time_list.add(time_)
            if time_ in self.dic:
                if type_ in self.dic[time_]:
                    self.dic[time_][type_] += num
                else:
                    self.dic[time_][type_] = num
            else:
                self.dic[time_] = {}
                self.dic[time_][type_] = num

    # Output the data in order.
    def outPut(self):
        self.time_list = list(self.time_list)
        self.time_list = sorted(self.time_list, reverse=True)
        for idx in self.time_list:
            ans = idx
            self.dic[idx] = sorted(
                self.dic[idx].iteritems(), key=lambda d: d[0])
            for type_ in self.dic[idx]:
                ans += "," + type_[0] + ", " + str(type_[1])
            print(ans)


def main():
    res = Solution()
    res.outPut()

if __name__ == '__main__':
    main()
