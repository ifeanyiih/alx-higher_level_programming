#!/usr/bin/python3
def roman_to_int(roman):
    base = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sums = 0
    if type(roman) is not str or roman is None:
        return 0
    for i in range(len(roman)):
        if i != len(roman) - 1:
            sign = roman[i]
            if sign == 'I' and roman[i + 1] in 'VXLCDM':
                sums -= base[sign]
            elif sign == 'V' and roman[i + 1] in 'XLCDM':
                sums -= base[sign]
            elif sign == 'X' and roman[i + 1] in 'LCDM':
                sums -= base[sign]
            elif sign == 'L' and roman[i + 1] in 'CDM':
                sums -= base[sign]
            elif sign == 'C' and roman[i + 1] in 'DM':
                sums -= base[sign]
            else:
                sums += base[sign]
        else:
            sums += base[roman[i]]
    return sums
