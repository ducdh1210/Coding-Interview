from collections import Counter, defaultdict, namedtuple, deque, OrderedDict

# 1. Counter
print("1. Counter Example:")
data = ["apple", "banana", "apple", "orange", "banana", "apple"]
counter = Counter(data)
print(counter)
print()  # New line for separation

# 2. defaultdict
print("2. defaultdict Example:")
data = [("apple", 1), ("banana", 2), ("apple", 3), ("orange", 4), ("banana", 5)]
default_dict = defaultdict(list)
for key, value in data:
    default_dict[key].append(value)
print(default_dict)
print()  # New line for separation

# 3. namedtuple
print("3. namedtuple Example:")
Point = namedtuple("Point", ["x", "y"])
p1 = Point(10, 20)
p2 = Point(30, 40)
print(p1)
print(p2)
print(p1.x, p1.y)
print(p2.x, p2.y)
print()  # New line for separation

# 4. deque
print("4. deque Example:")
d = deque()
d.append("a")
d.append("b")
d.appendleft("c")
d.append("d")
d.appendleft("e")
print(d)
d.pop()
print(d)
d.popleft()
print(d)
print()  # New line for separation

# 5. OrderedDict
print("5. OrderedDict Example:")
ordered_dict = OrderedDict()
ordered_dict["banana"] = 3
ordered_dict["apple"] = 4
ordered_dict["orange"] = 2
ordered_dict["pear"] = 1
print(ordered_dict)
for key, value in ordered_dict.items():
    print(key, value)
