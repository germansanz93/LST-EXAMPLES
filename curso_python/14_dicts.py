my_dict = {"key1":"value1", "key2":"value2"}
my_dict["key3"] = "value3"
# my_dict["key3"] = "value2"

print(my_dict["key1"])
print(my_dict)
# print(my_dict.pop("key1"))
# print(my_dict)
# print(my_dict.pop("key1", None))

my_dict["key4"] = 1
my_dict[2] = True

print(my_dict)

for val in my_dict.values():
    print(val)

print()

for key in my_dict.keys():
    print(key ,my_dict[key])

print()

for pair in my_dict.items():
    print(pair)

del my_dict["key1"]

for k, v in my_dict.items():
    print(k, v)
