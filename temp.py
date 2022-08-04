from datetime import datetime

# dict1 = {
#     "name" : "anand",
#     "time" : datetime.now().minute + 1,
# }
#
# dict_time = dict1.get("time")
# list1 = ['hello', 'there']
#
# while len(list1) > 0:
#     if datetime.now().minute == dict_time:
#         list1.clear()
#         print("List cleared")
#     else:
#         print(datetime.now().minute - dict_time)
# print("Outside loop")

# dict1 = {}
#
# list1 = []
# temp = input("Hello there give some input :- ")
# dict1[datetime.now().minute+2] = temp
# list1.append(temp)
#
# while len(list1)>0:
#     # temp = input("Hello there give some input :- ")
#     # dict1[datetime.now().minute + 2] = temp
#     # list1.append(temp)
#     if dict1.get(datetime.now().minute):
#         remove = dict1.get(datetime.now().minute)
#         dict1.pop(datetime.now().minute)
#         list1.remove(remove)
#     else:
#         print("No item found.")
#
# print("List is empty.")

now = datetime.now()
dtString = now.strftime("%H:%M:%S")
print(dtString)