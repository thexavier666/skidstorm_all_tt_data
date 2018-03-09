import csv
import urllib
import os
import json
import numpy
from pprint import pprint

def get_avg(some_list):
    return sum(some_list)*1.0/len(some_list)*1.0

def do_transpose(some_2Dlist):
    y = zip(*some_2Dlist)
    z = []

    for i in y:
        z.append(list(i))

    return z

def get_skid_data():
    # The directory which will store all time trail data
    cut_off_val         = 50
    round_off_val       = 4

    ss_data_dir         = "./json_data"
    ss_stat_dir         = "./json_stat_top%s" % cut_off_val
    json_out_file       = ss_data_dir + "/" + "file_%s_%s.json"
    full_csv_file_name  = ss_stat_dir + "/" + "top%s_stat_%s.csv"


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
                p.append(round(k["highscore"],3))

            # taking only top "cut_off_val" times
            p = p[:cut_off_val]

            tmp_l = [j[0]] + p

            f_list.append(tmp_l)

        # transpoing matrix
        #f_list = do_transpose(f_list)

        # write to csv file
        csv_fp = open(full_csv_file_name % (cut_off_val,i[0]), 'wb')
        wr = csv.writer(csv_fp)
        wr.writerows(f_list)

def main():
    get_skid_data()

if __name__ == "__main__":
    main()
