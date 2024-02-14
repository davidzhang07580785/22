from datetime import datetime, timedelta

# 获取用户输入的日期
user_input = input("请输入日期（格式：YYYY-MM-DD）：")

# 将用户输入的日期转换为datetime对象
input_date = datetime.strptime(user_input, "%Y-%m-%d")

# 计算279周前的日期
delta = timedelta(weeks=279)
result_date = input_date - delta

# 将结果格式化为指定的日期格式
result_str = result_date.strftime("%Y-%m-%d")

# 输出结果
print("279周前的日期是：", result_str)

#写一个python 程序，让用户输入日期，计算279周前对应的日期