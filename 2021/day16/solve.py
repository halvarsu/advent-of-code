import functools
import numpy as np


def from_binary(val):
    return sum(int(v) * 2 ** i for i, v in enumerate(str(val)[::-1]))


def to_binary(val):
    s = val
    out = ""
    for i in range(4):
        out = str(s % 2) + out
        s = s // 2
    return out


def get_literal_packet_value(packet, i=6):
    end_of_packet = False
    packet_value = ""
    while not end_of_packet:
        packet_value += packet[i + 1 : i + 5]
        end_of_packet = packet[i] == "0"
        i += 5
    final_bits = packet[i:]
    packet_value = from_binary(packet_value)
    return packet_value, final_bits


def packet_to_binary(hex_packet):
    packet = ""
    for hex_val in hex_packet:
        int_val = int(hex_val.lower(), base=16)
        bin_val = to_binary(int_val)
        packet += bin_val
    return packet


def prod(x):
    return functools.reduce(lambda a, b: a * b, x)


def gt(x):
    return int(x[0] > x[1])


def lt(x):
    return int(x[0] < x[1])


def eq(x):
    return int(x[0] == x[1])


OPERATORS = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: gt,
    6: lt,
    7: eq,
}


def read_packet(packet):
    assert not all(s == "0" for s in packet), f"{packet=}, {packet_values=}"
    versions = [from_binary(packet[:3])]

    type_id = from_binary(packet[3:6])
    if type_id == 4:
        packet_value, remaining = get_literal_packet_value(packet)
    else:
        length_type_id = packet[6]
        sub_values = []
        if length_type_id == "0":
            length = from_binary(packet[7 : 7 + 15])
            remaining = packet[22:]
            target_length = len(remaining) - length
            # print("SUBPACKET 0, length", length, remaining)
            while len(remaining) > target_length:
                new_versions, sub_value, remaining = read_packet(remaining)
                sub_values.append(sub_value)
                versions += new_versions
        elif length_type_id == "1":
            num_subpackets = from_binary(packet[7 : 7 + 11])
            # print("SUBPACKET 1, num", num_subpackets)
            remaining = packet[18:]
            for i in range(num_subpackets):
                new_versions, sub_value, remaining = read_packet(remaining)
                versions += new_versions
                sub_values.append(sub_value)
        else:
            raise ValueError()
        packet_value = OPERATORS[type_id](sub_values)

    return versions, packet_value, remaining


def get_data():
    filename = "input"
    with open(filename) as infile:
        data = [line.strip() for line in infile.readlines()]
    return data


def main():
    data = get_data()
    for hex_packet in data:
        print(f"{hex_packet=}")
        packet = packet_to_binary(hex_packet)
        # print(f"{packet=}")
        versions, packet_value, rem = read_packet(packet)
        versions_sum = sum(versions)
        print(f"{versions=}, {versions_sum=}")
        print(f"{packet_value=}")
        print()


if __name__ == "__main__":
    main()
