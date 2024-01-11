import numpy as np


class MONAD:
    def __init__(self, model_no, filename, state=None, skip_lines=0, verbose=0):
        self.skip_lines=skip_lines
        self.model_no = model_no
        self.filename = filename
        if state is None:
            self.state = {k:0 for k in "xyzw"}
        else:
            self.state = state
        self.verbose=verbose
        self.i = 0


    def print(self, s):
        if self.verbose >= 1:
            print(s)

    def get_next_model_val(self):
        val = int(self.model_no[self.i])
        self.print(f"read val: {val}")
        self.i += 1
        assert val > 0
        return val

    def print_state(self):
        for k,v in self.state.items():
            print(f"{k}={v}")

    def iterate(self):
        for instructions in self.file.readlines():
            op, a, b, *cmt = instructions.strip().split()
            a_val_prev = self.state[a]
            if op != 'inp':
                try:
                    b_val = int(b)
                except ValueError:
                    b_val = self.state[b]
            else:
                b_val = 'null'
            self.operate(op, a, b_val)
            yield op, a, b, self.state


    def operate(self, op, a, b):
        getattr(self, op)(a, b)

    def __enter__(self):
        self.file = open(self.filename)
        for i in range(self.skip_lines):self.file.readline()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

    def inp(self, reg, *args):
        val = self.get_next_model_val()
        self.state[reg] = val

    def add(self, reg, val):
        self.state[reg] += val

    def mul(self, reg, val):
        self.state[reg] *= val

    def div(self, reg, val):
        self.state[reg] //= val

    def mod(self, reg, val):
        self.state[reg] %= val

    def eql(self, reg, val):
        self.state[reg] = self.state[reg] == val


def get_next_model_no(model_no):
    return model_no - 1


def main(filename):
    model_no = 99999999999999
    while model_no > 0:
        with MONAD(str(model_no), filename, verbose=0) as monad:
            for op, a, b, state in monad.iterate():
                pass
            # print(monad.state)
            if monad.state['z'] == 0:
                print("FOUND IT!!", model_no)
        # model_no = int(str(model_no)[::-1])
        model_no -= 1
        while "0" in str(model_no):
            model_no -= 1
            print("oops")
        if model_no % 111 == 0:
            print(model_no)
        # model_no = int(str(model_no)[::-1])


if __name__ == "__main__":
    model_no = "99999999999999"
    filename = "input"
    # with MONAD(model_no, filename, verbose=1) as monad:
    #     for op, a, b, state in monad.iterate():
    #         print(op, a, b, "|",  state['z']%26)
    #         print(state)
    main(filename)
