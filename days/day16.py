# Solutions do Day16 puzzle at https://adventofcode.com/2021

class Packet:
    def __init__(self, index):
        self.index = index
        self.version = None
        self.type_id = None
        self.value = 0
        self.lenght_type_id = 0
        self.sub_packets = list()
        self.bits = ""

    @property
    def version_sum(self):
        total = int(self.version, 2)
        for sub_packet in self.sub_packets:
            total += sub_packet.version_sum
        return total

    @property
    def sum_value(self):
        type_id = int(self.type_id, 2)
        if type_id == 0:
            return sum(sub_packet.sum_value for sub_packet in self.sub_packets)
        elif type_id == 1:
            temp = 1
            for sub_packet in self.sub_packets:
                temp *= sub_packet.sum_value
            return temp
        elif type_id == 2:
            return min(sub_packet.sum_value for sub_packet in self.sub_packets)
        elif type_id == 3:
            return max(sub_packet.sum_value for sub_packet in self.sub_packets)
        elif type_id == 4:
            return self.value
        elif type_id == 5:
            return 1 if self.sub_packets[0].sum_value < self.sub_packets[1].sum_value else 0
        elif type_id == 6:
            return 1 if self.sub_packets[0].sum_value > self.sub_packets[1].sum_value else 0
        elif type_id == 7:
            return 1 if self.sub_packets[0].sum_value == self.sub_packets[1].sum_value else 0

    def __str__(self):
        string = f"Index: {self.index}, Version: {self.version}, Type_id: {self.type_id}, Lenght_type_id {self.lenght_type_id}, Value: {self.value}"
        for sub_packets in self.sub_packets:
            string += "\n"+sub_packets.__str__()
        return string


class Day16:
    def __init__(self):
        #with open("puzzle_input/input_day16_test.txt") as file:
        with open("puzzle_input/input_day16.txt") as file:
                lines = [x for x in file.read().split("\n") if x != ""]
        file.close()
        packet = self.parse_binary(self.parse_input(lines[0]))
        print("Total value sum:", packet.version_sum)
        print("After operations:", packet.sum_value, "\n1922490999789")

    @staticmethod
    def parse_input(line):
        leading_0 = len(line) * 4
        return str(bin(int(line, 16))[2:]).zfill(leading_0)

    def parse_binary(self, binary):
        index = 0
        while index < len(binary):
            packet = Packet(index)
            packet.version = binary[index:index+3]
            index += 3
            packet.type_id = binary[index:index+3]
            index += 3
            if packet.type_id == "100":
                value = ""
                while True:
                    chunk = binary[index: index + 5]
                    index += 5
                    value += chunk[1:]
                    if chunk[0] == "0":
                        packet.bits = binary[packet.index:index]
                        packet.value = int(value, 2)
                        return packet
            else:
                packet.lenght_type_id = int(binary[index], 2)
                index += 1
                if packet.lenght_type_id == 0:
                    sub_pack_length = int(binary[index:index + 15], 2)
                    index += 15
                    sub_packets = list()
                    new_index = 0
                    while new_index < sub_pack_length:
                        new_binary = binary[index + new_index:]
                        sub_pack = self.parse_binary(new_binary)
                        sub_packets.append(sub_pack)
                        new_index += len(sub_pack.bits)
                    packet.sub_packets = sub_packets
                    index += new_index

                if packet.lenght_type_id == 1:
                    sub_packets_number = int(binary[index:index + 11], 2)
                    index += 11
                    sub_packets = list()
                    while len(sub_packets) < sub_packets_number:
                        new_binary = binary[index:]
                        sub_pack = self.parse_binary(new_binary)
                        sub_packets.append(sub_pack)
                        index += len(sub_pack.bits)
                    packet.sub_packets = sub_packets

            packet.bits = binary[packet.index:index]
            return packet
