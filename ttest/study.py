# greet = "Hello, World!"
# print(greet + "\nfrom test.py")
# print(type("hello world"))
# a = 5
# b = 10
# c = 2.5
# a = b / c
# print(a)
# print(type(a))

# BMI = 体重 / (身高 * 身高)
# user_weight = input("请输入您的体重(kg): ")
# user_height = input("请输入您的身高(cm): ")
# user_BMI = float(user_weight) / ((float(user_height) / 100) ** 2)
# print("您的BMI指数为: {:.2f}".format(user_BMI))

# height_cm = float(input("请输入您的身高(cm): "))
# height_m = height_cm / 100
# bmi = float(input("请输入您的目标BMI指数: "))

# weight = bmi * (height_m ** 2)

# print("为达到该BMI，您的体重应为: {:.2f} kg".format(weight))

# mood_index = int(input("对象今天的心情指数是："))
# if mood_index >= 60:
#     print("恭喜，今晚应该可以打游戏，去吧皮卡丘！")
# else:
#     print("为了自个小命，还是别打了。")

# shopping_list = []
# shopping_list.append("键盘")
# shopping_list.append("键帽")
# shopping_list.append("键帽")
# shopping_list.append("音响")
# shopping_list.append("电竞椅")
# shopping_list[1] = "硬盘"

# print(shopping_list)
# print(len(shopping_list))
# print(shopping_list[1])

# price = [100, 200, 300, 400, 500]
# max_price = max(price)
# min_price = min(price)
# sorted_price = sorted(price)
# print("最高价格:", max_price)
# print("最低价格:", min_price)
# print("价格从低到高排序:", sorted_price)

# slang_dict = {
#     "LOL": "League of Legends",
#     "GG": "Good Game",
#     "BRB": "Be Right Back",
#     "AFK": "Away From Keyboard",
#     "IMO": "In My Opinion", }
# slang_dict["LMAO"] = "Laughing"
# slang_dict["ROFL"] = "Rolling On the Floor Laughing"
# query = input("请输入要查询的网络用语: ")
# if query in slang_dict:
#     print("您查询的" + query + "含义如下")
#     print(slang_dict[query])
# else:
#     print("您查询的" + query + "不在词典中，请重新输入")

# for i in range():
#     print(i)
#     i += 1
#     if i == 100:
#         break

# contacts = ["老余", "老林", "老陈", "老曾", "老李", "老张"]
# year = "虎"
# name = "老林"
# message = f"""
# 金{year}贺岁，欢乐祥瑞。
# 金{year}敲门，五福临门。
# 给{name}及家人拜年了！
# 新春快乐，{year}年大吉!
# """
# print(message)

# def calculate_BMI(weight, height):
#     BMI = weight / height ** 2
#     if BMI <= 18.5:
#         category = "偏瘦"
#     elif BMI <= 24.9:
#         category = "正常"
#     elif BMI <= 29.9:
#         category = "偏胖"
#     else:
#         category = "肥胖"
#     print(f"您的BMI指数为: {BMI:.2f}，属于{category}范围。")
#     # return BMI, category


# calculate_BMI(70, 1.75)  # 示例调用，体重70kg，身高1.75m

# class CuteCat:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#     def


# cat1 = CuteCat("Lambton", 3, "黑色")
# print(f"猫咪的名字是: {cat1.name}, 年龄是: {cat1.age}岁, 颜色是: {cat1.color}")

# class Student:
#     def __init__(self, name, age, student_id):
#         self.name = name
#         self.age = age
#         self.student_id = student_id
#         self.grades = {"语文": 0, "数学": 0, "英语": 0}

#     def set_grade(self, course, grade):
#         if course in self.grades:
#             self.grades[course] = grade

#     def print_grades(self):
#         print(f"学生{self.name} (学号：{self.student_id}) 的成绩如下")
#         for course in self.grades:
#             print(f"{course}: {self.grades[course]}分")


# chen = Student("陈小明", 20, "2023001")
# zeng = Student("曾小红", 21, "2023002")
# print(chen.name)
# print(zeng.name)
# chen.set_grade("语文", 85)
# chen.set_grade("数学", 88)
# chen.set_grade("英语", 90)
# zeng.set_grade("语文", 95)
# zeng.set_grade("数学", 90)
# zeng.set_grade("英语", 92)
# chen.print_grades()
# zeng.print_grades()

# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

#     def print_info(self):
#         print(f"员工名字：{self.name}, 工号：{self.id}")


# class FullTimeEmployee(Employee):
#     def __init__(self, name, id, mothly_salary):
#         super().__init__(name, id)
#         self.monthly_salary = mothly_salary

#     def calculate_monthly_pay(self):
#         return self.monthly_salary


# class PartTimeEmployee(Employee):
#     def __init__(self, name, id, daily_salary, work_days):
#         super().__init__(name, id)
#         self.daily_salary = daily_salary
#         self.work_days = work_days

#     def calculate_monthly_pay(self):
#         return self.daily_salary * self.work_days


# # 创建全职员工实例
# zhangsan = FullTimeEmployee("张三", "1011", 6000)
# lisi = PartTimeEmployee("李四", "1002", 230, 15)
# # 打印全职员工信息
# zhangsan.print_info()
# # 打印兼职员工信息
# lisi.print_info()
# print(zhangsan.calculate_monthly_pay())
# print(lisi.calculate_monthly_pay())

# with open("D:/CODE/datecontest/ttest/data.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line.strip())


# with open("./poem.txt", "w", encoding="utf-8") as file:
#     file.write("我欲乘风归去，\n又恐琼楼玉宇，\n高处不胜寒。")

# with open("./poem.txt", "a", encoding="utf-8") as file:
#     file.write("\n起舞弄清影,\n")
#     file.write("何似在人间。")


class ShoppingList:
    def __init__(self, shopping_list):
        self.shopping_list = shopping_list

    def get_item_count(self):
        return len(self.shopping_list)

    def get_total_price(self):
        total_price = 0
        for price in self.shopping_list.values():
            total_price += price
        return total_price
