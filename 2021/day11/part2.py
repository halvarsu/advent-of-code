from part1 import get_data, simulate

def run():
    vals = get_data("input")
    sync_time = simulate(vals, nstep=1000, visualize=True, find_sync=True)
    print(sync_time)

if __name__ == "__main__":
    run()
