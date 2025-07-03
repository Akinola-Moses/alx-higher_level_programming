#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return (0)
    added_scr = 0
    added_wgt = 0

    for scr, wgt in my_list:
        added_scr += scr * wgt
        added_wgt += wgt
        wgt_avg = added_scr / added_wgt
    return (wgt_avg)
