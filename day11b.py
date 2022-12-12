import math

with open('day11.txt') as f:
    lines = f.read()


class Monkey:
    inspected = 0

    def __init__(self, name, items, operation, test, true_monkey, false_monkey):
        self.name = name
        self.items = items
        self.operation = operation.split(" ")
        self.test = test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.mod = mod

    def add_item(self, item):
        self.items.append(item)

    def print(self):
        return f'[{self.name}] items: {self.items}, operation: {self.operation}, test: {self.test}, true: ' \
               f'{self.true_monkey} and false: {self.false_monkey} [{self.inspected}]'

    def get_worry_level(self, item):
        self.inspected += 1

        if self.operation[0] == "old" and self.operation[2] == "old":
            wl = item * item
            # print(f"\t\tWorry level is multiplied by itself to {wl}")
        elif self.operation[0] == "old" and self.operation[1] == "*":
            multiplier = int(self.operation[2])
            wl = multiplier * item
            # print(f"\t\tWorry level is multiplied by {multiplier} to {wl}")

        else:
            increase = int(self.operation[2])
            wl = increase + item
            # print(f"\t\tWorry level is increased by {increase} to {wl}")

        # print(f'\t\tMonkey gets bored with item. Worry level is divided by 3 to {math.floor(wl / 3)}.')
        # yeah, this is hardcoded.
        return wl % 9699690

    def remove_items(self):
        self.items = []


monkeys = []
for line in lines.split("Monkey ")[1:]:
    raw_monkey = line.strip().split("\n")
    name, items, operation, test, true_monkey, false_monkey = 0, [], '', 0, 0, 0

    for part in raw_monkey:
        if "Starting items" in part:
            items_ids = part.split(": ")[1].split(", ")
            for i in items_ids:
                # pk and worry level
                items.append(int(i))
        elif "Operation" in part:
            operation = part.split(": ")[1].split("new = ")[1]
        elif "Test" in part:
            test = int(part.split(" by ")[1])
        elif "true" in part:
            true_monkey = int(part.split(" monkey ")[1])
        elif "false" in part:
            false_monkey = int(part.split(" monkey ")[1])
        else:
            name = int(part.rstrip(":"))

    # add the monkey
    m = Monkey(name, items, operation, test, true_monkey, false_monkey)

    monkeys.append(m)

for _ in range(10000):
    for m in monkeys:
        # print(m.print())
        for item in m.items:
            # print(f'\tMonkey inspects an item with a worry level of {item}')
            wl = m.get_worry_level(item)
            if (wl % m.test) == 0:
                # print(f"\t\tCurrent worry level is divisible by {m.test}.")
                # print(f'\t\tItem with worry level {wl} is thrown to monkey {m.true_monkey}.')
                for tm in monkeys:
                    if tm.name == m.true_monkey:
                        tm.add_item(wl)
                        break

            else:
                # print(f"\t\tCurrent worry level is not divisible by {m.test}.")
                # print(f'\t\tItem with worry level {wl} is thrown to monkey {m.false_monkey}.')
                for fm in monkeys:
                    if fm.name == m.false_monkey:
                        fm.add_item(wl)
                        break

            m.remove_items()
monkeys.sort(key=lambda x: x.inspected, reverse=True)
part2 = monkeys[0].inspected * monkeys[1].inspected

print(part2)



