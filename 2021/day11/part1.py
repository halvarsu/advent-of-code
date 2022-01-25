import scipy.signal
import numpy as np
import time
import os

def get_data(filename):
    with open(filename) as infile:
        vals = np.array([[int(v) for v in line.strip()] for line in  infile.readlines()])
    return vals


def print_flash(has_flashed):
    for line in has_flashed:
        for val in line:
            print("x" if val else " ", end="")
        print()


def simulate(vals, nstep=7, visualize=False, find_sync=False):
    stencil = np.ones((3,3))
    stencil[1,1] = 0  # not really necessary
    tot_flash = 0
    for i in range(nstep):
        vals += 1
        has_flashed = np.zeros_like(vals)
        sync = False
        while True:
            flashing = np.logical_and(vals > 9, ~has_flashed)
            if np.all(~flashing):
                break
            has_flashed = np.logical_or(flashing, has_flashed)
            indx, indy = np.where(flashing)
            add = scipy.signal.convolve2d(flashing, stencil)[1:-1, 1:-1]
            vals += add.astype(int) # [add.astype(bool)] += 1
        tot_flash += np.sum(has_flashed)
        vals[vals > 9] = 0
        if find_sync and np.all(has_flashed):
            return i+1
        if visualize:
            print_flash(has_flashed)
            time.sleep(0.01)
            os.system("clear")
    if find_sync:
        raise ValueError(f"Octopuses did not sync after {nstep} steps")
    return vals, tot_flash


def run():
    vals = get_data("input")
    _,tot_flash = simulate(vals, nstep=100, visualize=False)
    print(tot_flash)

if __name__ == "__main__":
    run()
