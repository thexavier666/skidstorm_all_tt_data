import csv
import urllib

def get_skid_data():
    ss_json_url = "http://%s/highscores/list/%s/ALL-%s/1-100"

    ss_ip = "52.36.89.185"

    map_id_file = "map_name.csv"
    car_id_file = "car_name.csv"

    map_csv = list(csv.reader(open(map_id_file, 'r')))
    car_csv = list(csv.reader(open(car_id_file, 'r')))

    for i in map_csv:
        for j in car_csv:
            full_url = ss_json_url % (ss_ip,i[0],j[0])
            json_file_name = "file_%s_%s.json" % (i[0], j[0])

            urllib.urlretrieve(full_url, json_file_name)

            print "File created : ", json_file_name


def main():

    get_skid_data()

if __name__ == "__main__":
    main()
