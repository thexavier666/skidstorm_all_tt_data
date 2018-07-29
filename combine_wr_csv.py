import subprocess as sp
import csv

from misc_functions import do_transpose
from misc_functions import write_2dlist_to_csv

def create_wr_file_names(map_csv):
    wr_file_name = []

    file_name_prefix = "wr_"
    file_extension = ".csv"

    wr_data_dir = "world_record_data/"

    for row in map_csv:
        wr_file_name.append(wr_data_dir + file_name_prefix + row[0] + file_extension)

    return wr_file_name

def main():
    # map and car data location
    static_dir = "static_data/"

    # world record directory
    wr_dir = "world_record_data"

    # Files which contain the map and car name
    map_id_file = static_dir + "map_name.csv"
    #car_id_file = static_dir + "car_name.csv"

    map_csv = list(csv.reader(open(map_id_file, 'r')))

    wr_file_name = create_wr_file_names(map_csv)

    fp_list = []

    for row in wr_file_name:
        fp_list.append(list(csv.reader(open(row,'r'))))

    #print fp_list[0]

    num_of_maps = len(wr_file_name)

    # note : currently this is static
    num_of_cars = 18

    all_time_list = []

    for j in xrange(num_of_cars):

        tmp_car_list = []

        for i in xrange(num_of_maps):

            tmp_car_list.extend(fp_list[i][j])

        all_time_list.append(tmp_car_list)

    write_2dlist_to_csv(all_time_list, "skidstorm_all_car_wr.csv")

if __name__ == "__main__":
    main()
