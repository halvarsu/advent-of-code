from part1 import MONAD

class hashabledict(dict):
    def __hash__(self):
        return hash(tuple(sorted(self.items())))

def dict_to_tup(d):
    return (d['y'], d['z'])

def tup_to_dict(t):
    return {"y":t[0], "z":t[1], "x":0, "w":0}

def main(filename):
    model_no = 99999999999999
    input_tuples = [set()]
    input_tuples[0].add(dict_to_tup({k:0 for k in 'xyzw'}))
    print(input_tuples)
    for bit in range(14):
        print("BIT!!!", len(input_tuples[-1]))
        input_tuples.append(set())
        for input_tup in input_tuples[bit]:
            # print(input_tup)
            input_state = tup_to_dict(input_tup)
            for i in range(1, 10):
                model_no = str(i)
                # # print(input_state)
                with MONAD(str(model_no), filename, verbose=0,
                        skip_lines=0, state=input_state) as monad:
                    try:
                        for op, a, b, state in monad.iterate():
                            pass
                    except IndexError:
                        # print(i, state)
                        input_tuples[-1].add(dict_to_tup(state))
    print([len(inp_s)  for inp_s in input_tuples])
    # print(input_states)


filename='input'
main(filename)
