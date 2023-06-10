# 18.7

class Material:

    def __init__(self):
        self.mat_type = None;
        self.mat_name = None;
        self.mat_natur = None;

    def make_material(self, mtype, mname, mnaturalness):
        self.mat_type = mtype;
        self.mat_name = mname;
        self.mat_natur = mnaturalness;

    def set(self):
        self.mat_type = input("Enter material type: ");
        self.mat_name = input("Enter material name: ");
        self.mat_natur = input("Enter naturalness: ");

    def show(self):
        print(f"type: {self.mat_type}, name: {self.mat_name}, naturalness: {self.mat_natur}");


class FunctionalAdaptation:

    def __init__(self):
        self.fun_name = None;
        self.fun_ager = None;

    def make_functional_adaptation(self, fname, fager):
        self.fun_name = fname;
        self.fun_ager = fager;

    def set(self):
        self.fun_name = input("Enter functional name: ");
        self.fun_ager = input("Enter functional age recommendation: ");

    def show(self):
        print(f"name: {self.fun_name}, age recommendation: {self.fun_ager}");


class Furniture(Material, FunctionalAdaptation):

    def __init__(self):
        self.type = None;
        self.name = None;
        FunctionalAdaptation.__init__(self);
        Material.__init__(self);

    def make_furniture(self, furtype, furname, funname, funager, mtype, mname, mnaturalness):
        self.type = furtype;
        self.name = furname;
        self.make_functional_adaptation(funname, funager);
        self.make_material(mtype, mname, mnaturalness);

    def set(self):
        self.type = input("Enter furniture type: ");
        self.name = input("Enter furniture name: ");
        FunctionalAdaptation.set(self);
        Material.set(self);

    def show(self):
        print(f"type: {self.type}, name: {self.name}, material type: {self.mat_type}, material name: {self.mat_name}, material naturalness: {self.mat_natur}, functional name: {self.fun_name}, functional age recommendation: {self.fun_ager}");

if (__name__ == "__main__"):

    condition = True;
    frn_lst = [];

    while (condition):
        n = int(input("1. add furniture\n2. show furniture\n3. classify by ...\n0. exit\nEnter number: "));

        if (n == 0):
            condition = False;
            break;

        elif (n == 1):
            temp_fur = Furniture();
            temp_fur.set();
            frn_lst = frn_lst + [temp_fur];

        elif (n == 2):
            print("\t\t\t== == == == == == == == ==n");
            for frn in frn_lst:
                frn.show();
                print("");
            print("\t\t\t== == == == == == == == ==");

        elif (n == 3):
            m = int(input("\tClassify by:\n\t1. material type\n\t2. furniture type\n\t3. functional appointment\n\tEnter number: "));

            if (m == 1):
                mat = input("\tEnter material type: ");
                print("\t\t\t\t == == == == == == ==\n\n\t", end="");
                for furn in frn_lst:
                    if (furn.mat_type == mat):
                        furn.show();
                        print("", end="\n\t");
                print("\t\t\t == == == == == == ==");

            elif (m == 2):
                ftype = input("\tEnter furniture type: ");
                print("\t\t\t\t == == == == == == ==\n\n\t", end="");
                for furn in frn_lst:
                    if (furn.type == ftype):
                        furn.show();
                        print("", end="\n\t");
                print("\t\t\t == == == == == == ==");

            elif (m == 3):
                func = input("\tEnter functional appointment: ");
                print("\t\t\t\t == == == == == == ==\n\n\t", end="");
                for furn in frn_lst:
                    if (furn.fun_name == func):
                        furn.show();
                        print("", end="\n\t");
                print("\t\t\t == == == == == == ==");

            else:
                print("\tWrong number");
        else:
            print("Wrong number");
