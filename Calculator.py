print("This calculator can add, subtract, multiply, and divide.")
print("Begin with a #.")


class Calculator:

    def __init__(self, run_tot, op, num, equal, entries):
        self.run_tot = run_tot
        self.op = op
        self.num = num
        self.equal = equal
        self.entries = entries

    def add(self):
        self.run_tot = float(self.run_tot + self.num)
        return self.run_tot

    def sub(self):
        self.run_tot = float(self.run_tot - self.num)
        return self.run_tot

    def mul(self):
        self.run_tot = float(self.run_tot * self.num)
        return self.run_tot

    def div(self):
        self.run_tot = float(self.run_tot / self.num)       # performs division of run_tot and num
        return self.run_tot

    def check_for_equals(self):                             # checks to see if the equal operator was entered
        if self.op == "=":
            print("Total: " + " " .join(str(x) for x in self.entries) + " " + str(round(self.run_tot, 10)))
            self.entries.clear()
            self.equal = True
            return self.equal
        else:
            self.equal = False
            return self.equal

    def run_tot_input(self):
        self.run_tot = input(" ")
        run_tot_input = False
        while run_tot_input is False:
            try:
                self.run_tot = float(self.run_tot)
                run_tot_input = True
                self.entries.append(self.run_tot)
            except ValueError:
                print("Invalid input. Please enter a number.")
                self.run_tot = input(" ")
        return self.run_tot

    def op_input(self):
        self.op = input(" ")
        op_input = False
        while op_input is False:
            if self.op == "+" or self.op == "-" or self.op == "*" or self.op == "/" or self.op == "=":
                op_input = True
                self.entries.append(self.op)
            else:
                print("Please enter one of the following: + - * / =")
                self.op = input(" ")
        return self.op

    def num_input(self):
        self.num = input(" ")
        num_input = False
        while num_input is False:
            try:
                self.num = float(self.num)
                num_input = True
                self.entries.append(self.num)
            except ValueError:
                print("Invalid input. Please enter a number.")
                self.num = input(" ")
        return self.num


entries = []
run_tot = 0
op = " "
num = 0
equal = False
comp = Calculator(run_tot, op, num, equal, entries)
exit = False
while exit is False:
    run_tot = comp.run_tot_input()
    op = comp.op_input()
    equal = comp.check_for_equals()
    if equal is False:
        while equal is False:
            num = comp.num_input()
            if op == "+":
                run_tot = comp.add()
            elif op == "-":
                run_tot = comp.sub()
            elif op == "*":
                run_tot = comp.mul()
            elif op == "/":
                while num == 0:
                    print("Cannot divide by 0. Please enter valid number.")
                    entries.pop()
                    num = comp.num_input()
                else:
                    run_tot = comp.div()
            else:
                print("No computation done.")
            op = comp.op_input()
            equal = comp.check_for_equals()
