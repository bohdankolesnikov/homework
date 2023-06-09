try:
    with open("content.txt", "r") as f:
        # each line = name of file
        f_names = [];
        for line in f:
            f_names.append(line[:-1]);
        nums = [];
        for elem in f_names:
            try:
                with open(elem, "r") as fl:
                    for line in fl:
                        try:
                            nums = nums + list(map(float, line.split()));
                        except ValueError:
                            print(f"file \"{elem}\" contains non-numeric characters, file skipped");

            except PermissionError:
                print(f"no permissions to read \"{elem}\", file skipped");
            except FileNotFoundError:
                print(f"file \"{elem}\" is not found, file skipped");
            except IOError:
                print(f"can't read from \"{elem}\", file skipped");

        print(f"Result: {sum(nums)}");


except PermissionError:
    print("no permissions to read \"content.txt\"");
except FileNotFoundError:
    print("file \"content.txt\" is not found");
except IOError:
    print("can't read from \"content.txt\"");

