import random as rd

class Transponder:
    def remove_restricted_codes(transponder_codes):
        removed_list = [1000, 2000, 7000, 7500, 7600, 7700]
        for removed in removed_list:
            transponder_codes.remove(removed)

    def geratransponder():
        transponder_codes = []
        for number in range(1,7778):
            if "8" in str(number):
                continue
            elif "9" in str(number):
                continue
            else:
                if len(str(number)) == 4:
                    transponder_codes.append(number)
                else:
                    transponder_codes.append("0"*(4 - len(str(number)))+str(number))
        Transponder.remove_restricted_codes(transponder_codes)

        return transponder_codes[rd.randint(0,len(transponder_codes))]

if __name__ == '__main__':
    print(f"O seu código transponder será {Transponder.geratransponder()}")

