import csv
import urllib
import os
import subprocess as sp

def get_skid_data():

    # IP of the skidstorm server which hosts all match details
    ss_ip = "api.skidstorm.cmcm.com"

    # The URL via which we can access the time trail data. The parameters are
    # URL
    # map name
    # car name
    ss_json_url = "http://%s/highscores/list/%s/ALL-%s/1-100"

    # The directory which will store all time trail data
    ss_data_dir = "json_data/"

    # map and car data location
    static_dir = "static_data/"

    # output file name
    output_json_name = "file_%s_%s.json"

    # Files which contain the map and car name
    map_id_file = static_dir + "map_name.csv"
    car_id_file = static_dir + "car_name.csv"

    # cleaning previously collected json files
    sp.call("rm -rf %s*.json", shell = True)

    # opening csv files
    map_csv = list(csv.reader(open(map_id_file, 'r')))
    car_csv = list(csv.reader(open(car_id_file, 'r')))

    # checking if directory exists or not
    if os.path.exists(ss_data_dir) == 0:
        os.makedirs(ss_data_dir)

    # for each map
    for i in map_csv:
        # for each car
        for j in car_csv:

            full_url = ss_json_url % (ss_ip,i[0],j[0])
            json_file_name = output_json_name % (i[0], j[0])

            urllib.urlretrieve(full_url, str(ss_data_dir + json_file_name))

            print "File created : ", json_file_name


def main():

    get_skid_data()

if __name__ == "__main__":
    main()
