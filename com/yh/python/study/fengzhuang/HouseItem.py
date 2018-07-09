class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s]占地%.2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return ("户型%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
                % (self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self, item):
        print("要添加%s" % item)
        if self.area > item.area:
            self.item_list.append(item)
            self.free_area = self.area - item.area
        else:
            print("家具的面积太大了，无法添加")


bed = HouseItem("以梦思", 4.5)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)
myHome = House("三室一厅", 105)
myHome.add_item(bed)

print(myHome)

print(bed)
print(chest)
print(table)
