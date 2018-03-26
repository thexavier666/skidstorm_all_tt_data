import csv
import urllib
import os
import json
import numpy
from pprint import pprint
from misc_functions import do_transpose
from misc_functions import write_2dlist_to_csv

def get_avg(some_list):
    return sum(some_list)*1.0/len(some_list)*1.0

def get_skid_data():
    # The directory which will store all time trail data
    ss_data_dir         = "./json_data"
    ss_stat_dir         = "./json_stat"
    ss_aggr_dir         = "./aggregated_data"

    json_out_file       = ss_data_dir + "/" + "file_%s_%s.json"
    full_csv_file_name  = ss_stat_dir + "/" + "stat_%s.csv"
    all_avg_file_name   = ss_aggr_dir + "/" + "all_car_avg.csv"

    cut_off_val         = 15
    round_off_val       = 4

    # Files which contain the map and car name
    map_id_file = "map_name.csv"
    car_id_file = "car_name.csv"

    map_csv = list(csv.reader(open(map_id_file, 'r')))
    car_csv = list(csv.reader(open(car_id_file, 'r')))

    # checking if directory exists or not
    if os.path.exists(ss_aggr_dir) == 0:
        os.makedirs(ss_aggr_dir)

    if os.path.exists(ss_stat_dir) == 0:
        os.makedirs(ss_stat_dir)

    only_avg_list = []

    # for each map
    for i in map_csv:
        print i[0]

        f_list = []
        only_avg = []

        # for each car
        for j in car_csv:

            # fetching json source file
            json_file_name = json_out_file % (i[0], j[0])

            fp = open(json_file_name, 'r')

            json_dic = json.load(fp)

            print "\t", j[0]

            p = []

            # fetching only TT highscore, ie, total map time
            for k in json_dic["scores"]:
                p.append(k["highscore"])

            # taking only top "cut_off_val" times
            p = p[:cut_off_val]

            # calculating average and standard deviation
            highscore_avg = round(get_avg(p),round_off_val)
            highscore_std = round(numpy.std(p,ddof=1),round_off_val)

            print "\t\t", highscore_avg
            print "\t\t", highscore_std

            tmp_l = [i[0],j[0],highscore_avg,highscore_std]

            f_list.append(tmp_l)

            only_avg.append(highscore_avg)

        # write to csv file

        csv_fp = open(full_csv_file_name % i[0], 'wb')
        wr = csv.writer(csv_fp)
        wr.writerows(f_list)

        only_avg_list.append(only_avg)

    only_avg_list = do_transpose(only_avg_list)
    write_2dlist_to_csv(only_avg_list,all_avg_file_name)

def main():
    get_skid_data()

if __name__ == "__main__":
    main()
