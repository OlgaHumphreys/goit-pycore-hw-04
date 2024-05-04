import os


def get_cats_info(path):
    cats_list = []
    if os.path.exists(path): 
        with open(path,'r',encoding="UTF-8") as file:
            for line in file:
                elements = line.split(",")
                cat_dict = {"id": elements[0], "name": elements[1], "age": int(elements[2].replace("\n",""))}
                cats_list.append(cat_dict)
            return cats_list
    else:
        return f"file {path} is not found"    


cats_info = get_cats_info("data_cats.txt")
print(cats_info)


