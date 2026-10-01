'''9.	Merge two dictionaries'''
dict1 = input("Enter first dictionary (key:value pairs separated by commas): ")
dict2 = input("Enter second dictionary (key:value pairs separated by commas): ")

dict1 = dict(item.split(":") for item in dict1.split(","))
dict2 = dict(item.split(":") for item in dict2.split(","))

merged_dict = {**dict1, **dict2}
print("Merged dictionary:", merged_dict)