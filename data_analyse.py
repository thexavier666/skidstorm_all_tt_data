import csv
import urllib
import os
import json
import numpy
from pprint import pprint

def get_avg(some_list):
    return sum(some_list)*1.0/len(some_list)*1.0

def get_skid_data():
    # The directory which will store all time trail data
    ss_data_dir         = "./json_data"
    ss_stat_dir         = "./json_stat"
    json_out_file       = ss_data_dir + "/" + "file_%s_%s.json"
    full_csv_file_name  = ss_stat_dir + "/" + "stat_%s.csv"
    cut_off_val         = 30
    round_off_val       = 4

    # Files which contain the map and car name
    map_id_file = "map_name.csv"
    car_id_file = "car_name.csv"

    map_csv = list(csv.reader(open(map_id_file, 'r')))
    car_csv = list(csv.reader(open(car_id_file, 'r')))

    # checking if directory exists or not
    if os.path.exists(ss_stat_dir) == 0:
        os.makedirs(ss_stat_dir)

    # for each map
    for i in map_csv:
        print i[0]

        f_list = []

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

        # write to csv file

        csv_fp = open(full_csv_file_name % i[0], 'wb')
        wr = csv.writer(csv_fp)
        wr.writerows(f_list)

def main():
    get_skid_data()

if __name__ == "__main__":
    main()