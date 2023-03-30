# 12.13

with open("file.txt", "r") as f:
    buff = "";
    while (len(buff) < 2):
        buff = buff + f.readline().replace(" ", "").replace("\t", "").replace("\n", "");

    ch1 = buff[0];
    ch2 = buff[1];

print(f"First: {ch1}, second: {ch2}");

if (ch1.isdigit() and ch2.isdigit()):
    print("Digits, ", end="");
    if (int(ch1) == 0):
        num = int(ch2);
    else:
        num = int(ch1 + ch2);

    if (num % 2):
        print("odd");
    else:
        print("even");
else:
    print("Non-digits");
