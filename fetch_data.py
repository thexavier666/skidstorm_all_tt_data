import csv
import urllib
import os

def get_skid_data():

    # IP of the skidstorm server which hosts all match details
    ss_ip = "52.37.195.154"

    # The URL via which we can access the time trail data
    ss_json_url = "http://%s/highscores/list/%s/ALL-%s/1-100"

    # The directory which will store all time trail data
    ss_data_dir = "./json_data"

    # Files which contain the map and car name
    map_id_file = "map_name.csv"
    car_id_file = "car_name.csv"

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
            json_file_name = "file_%s_%s.json" % (i[0], j[0])

            urllib.urlretrieve(full_url, str(ss_data_dir + '/' + json_file_name))

            print "File created : ", json_file_name


def main():

    get_skid_data()

if __name__ == "__main__":
    main()
