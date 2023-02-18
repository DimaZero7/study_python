class CustomList:
    def __init__(self, obj: list):
        self.obj = obj

    def __iter__(self):
        """Must initialize and return an iterated object"""
        self.index = 0
        return self

    def __next__(self):
        """Instructions describing the procedure for issuing elements"""
        if self.index >= len(self.obj):
            raise StopIteration()
        item = self.obj[self.index]
        self.index += 1
        return item


obj_custom_list = CustomList(obj=['a', 'b', 'c'])

for item in obj_custom_list:
    print(item)
for item in obj_custom_list:
    print(item)


class CustomRange:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __iter__(self):
        """Must initialize and return an iterated object"""
        self.item = self.start
        return self

    def __next__(self):
        """Instructions describing the procedure for issuing elements"""
        if self.item > self.end:
            raise StopIteration()
        return_item = self.item
        self.item += 1
        return return_item


print([x for x in CustomRange(1, 5)])
