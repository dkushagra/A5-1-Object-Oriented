import numpy as np

#we declare three empty numpy arrays which we will be modifying to store the values of the three lfsr's
class a5(object):

    def __init__(self,key):
        self.reg_1 = np.empty
        self.reg_2 = np.empty
        self.reg_3 = np.empty
        self.reg_1 = key[0:19]
        self.reg_2 = key[19:41]
        self.reg_3 = key[41:64]
        print("registers loaded succesfully")

    def get_majority(self,a,b,c):
        if int(a) + int(b) + int(c) > 1:
            return True
        else:
            return False

    def clock_a5(self,clocking):
        c = clocking
        # print(reg_1[7], reg_2[9], reg_3[9])

        while c != 0:
            majority = self.get_majority(self.reg_1[8], self.reg_2[10], self.reg_3[10])
            # print(majority)
            if self.reg_1[8] == majority:
                first_bit = int(self.reg_1[18]) ^ int(self.reg_1[17]) ^ int(self.reg_1[16]) ^ int(self.reg_1[13])
                temp_arr1 = np.empty_like(self.reg_1)
                temp_arr1[0] = first_bit
                # copying all except last bit
                temp_arr1[1:] = self.reg_1[:18]
                #swapping reg_1
                self.reg_1 = temp_arr1

            if self.reg_2[10] == majority:
                first_bit = int(self.reg_2[20]) ^ int(self.reg_2[21])
                temp_arr2 = np.empty_like(self.reg_2)
                temp_arr2[0] = first_bit
                # copying all except last bit
                temp_arr2[1:] = self.reg_2[:21]
                # swapping reg_2
                self.reg_2 = temp_arr2

            if self.reg_3[10] == majority:
                first_bit = int(self.reg_3[20]) ^ int(self.reg_3[21]) ^ int(self.reg_3[22])
                temp_arr3 = np.empty_like(self.reg_3)
                temp_arr3[0] = first_bit
                #copying all except last bit
                temp_arr3[1:] = self.reg_3[:22]
                # swapping reg_3
                self.reg_3 = temp_arr3

            #calculating final output bit
            output = int(self.reg_1[18]) ^ int(self.reg_2[21]) ^ int(self.reg_3[22])
            print(int(output), end= '')

            c -= 1



def user_input():
    usrinput = np.array(list(map(int,(input("Enter the 64 bit key with space between the elements").strip().split()))), dtype=bool)
    # print(usrinput)
    # print(type(usrinput))
    if len(usrinput) == 64:
        return usrinput
    else:
        while len(usrinput) != 64:
            if len(usrinput) == 64:
                return usrinput
            usrinput = np.array(list(map(int,(input("Enter the 64 bit key with space between the elements").strip().split()))), dtype=bool)
        return usrinput


def main():
    key = user_input()
#    replacing user input by test values for now
#    testlist = list(map(int, "0 1 0 1 0 0 1 0 0 0 0 1 1 0 1 0 1 1 0 0 0 1 1 1 0 0 0 1 1 0 0 1 0 0 1 0 1 0 0 1 0 0 0 0 0 0 1 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1 0 1".strip().split()))
#    key = np.array(testlist, dtype=bool)
    # print(key, type(key))
    lfsr = a5(key)
    lfsr.clock_a5(int(input("Please enter the number of times to clock the Stream Generator")))

main()
