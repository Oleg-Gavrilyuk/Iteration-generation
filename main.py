nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

class FlatIterator:
  def __init__(self, list):
    self.list = list

  def __iter__(self):
    self.cursor = -1
    self.counter = 0
    return self

  def __next__(self):
      self.cursor += 1
      if self.cursor > len(self.list):
        raise StopIteration
      if isinstance(self.list[self.cursor], list):
          if self.counter >= len(self.list[self.cursor]):
              self.counter = 0
              self.cursor += 1
              if self.cursor == len(self.list):
                  raise StopIteration
              item = self.list[self.cursor][self.counter]
              self.cursor -= 1
              self.counter += 1
              return item
          else:
            item = self.list[self.cursor][self.counter]
            self.counter += 1
            self.cursor -= 1
            return item


for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)


# второе задание
def flat_generator(main_list):
    for lists in main_list:
        for i in lists:
            yield i

for item in  flat_generator(nested_list):
    print(item)

# 4 задание
nested_list2 = [
    [['a'], 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [[1, [2]], None],
]

def hard_generator(main_list):
    for lists in main_list:
        if isinstance(lists, list):
            for lis in hard_generator(lists):
                yield lis
        else:
            yield lists

for item in hard_generator(nested_list2):
    print(item)
