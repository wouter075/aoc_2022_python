with open('day21.txt') as f:
    lines = [line.rstrip() for line in f]

monkeys = []


class Monkey:
    value = 0
    operator = ""
    monkey1 = ""
    monkey2 = ""

    def __init__(self, name="", job=""):
        self.name = name
        self.job = job

        if job.isdigit():
            self.value = int(job)
        else:
            self.monkey1, self.operator, self.monkey2 = job.split(" ")

    def print(self):
        return f'Monkey name: {self.name}, job: {self.job}: {self.monkey1} {self.operator} {self.monkey2}'


def monkey_by_name(name):
    for m in monkeys:
        if m.name == name:
            return m


for line in lines:
    monkey_name, monkey_job = line.split(": ")
    monkeys.append(Monkey(monkey_name, monkey_job))


start = monkey_by_name("root")
mmm = 0

queue = [start.monkey1, start.monkey2]

while True:
    # get first item:
    m1 = monkey_by_name(queue[0])
    queue.pop(0)
    if m1.value == 0:
        queue.append(m1.monkey1)
        queue.append(m1.monkey2)

    if len(queue) == 2 and monkey_by_name(queue[0]).value != 0 and monkey_by_name(queue[1]).value != 0:
        break


print(queue)




