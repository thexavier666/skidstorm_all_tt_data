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
    ss_data_dir         = "json_data/"

    ss_wr_dir           = "world_record_data/"

    json_out_file       = ss_data_dir + "file_%s_%s.json"

    # static file directory
    static_dir = "static_data/"

    # Files which contain the map and car name
    map_id_file = static_dir + "map_name.csv"
    car_id_file = static_dir + "car_name.csv"

    map_csv = list(csv.reader(open(map_id_file, 'r')))
    car_csv = list(csv.reader(open(car_id_file, 'r')))

    # for each map
    for i in map_csv:
        print i[1]

        per_car_tmp = []

        # for each car
        for j in car_csv:

            # fetching json source file
            json_file_name = json_out_file % (i[0], j[0])

            fp = open(json_file_name, 'r')

            json_dic = json.load(fp)

            print "\t", j[1]

            # fetching only TT highscore, ie, total map time
            for k in json_dic["scores"]:
                top_one = k["clanName"], k["username"],  k["highscore"]
                print "\t\t", 
                print top_one[0],
                print " | ",
                print top_one[1], 
                print " | ",
                print top_one[2]

                per_car_tmp.append(top_one)
                break

        #write_2dlist_to_csv(per_car_tmp, ss_wr_dir + "wr_%s" % i[0])
            

def main():
    get_skid_data()

if __name__ == "__main__":
    main()
