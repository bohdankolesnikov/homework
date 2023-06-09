# 12.26

# file: *name*, *country*, *amount*


# {product: ([countries...], amount)}
products = {};

with open("file.txt", "r") as f:
    for line in f:
        line = line[:-1];
        lst = line.split(",");
        for i in range(len(lst)):
            lst[i] = lst[i].lstrip(" ").rstrip(" ");
        if lst[0] in products.keys():
            products[lst[0]] = (products[lst[0]][0] + [lst[1]], products[lst[0]][1] + int(lst[2]));
        else:
            products[lst[0]] = ([lst[1]], int(lst[2]));

prod = input("Enter product name: ");

if not (prod in products.keys()):
    raise KeyError("No product in list");

print("Contries of export: ", end="");
for elem in products[prod][0]:
    print(elem, end=", ");
print("\b\b  ")
print(f"Export amount: {products[prod][1]}");
