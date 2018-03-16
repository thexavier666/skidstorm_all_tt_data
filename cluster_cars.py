from sklearn.cluster import KMeans

import csv

import numpy as np
import pandas as pd

def main():
	ss_aggr_dir         = "./aggrgated_data"
	all_avg_file_name   = ss_aggr_dir + "/" + "all_car_avg.csv"

	map_id_file = "map_name.csv"
	car_id_file = "car_name.csv"

	map_csv = list(csv.reader(open(map_id_file, 'r')))
	car_csv = list(csv.reader(open(car_id_file, 'r')))

	for i in car_csv:
		print i[0][0:4],'\t',

	print

	avg_csv_fp = open(all_avg_file_name,'rb')
	avg_rd = csv.reader(avg_csv_fp)

	for row in avg_rd:
		int_row = map(float, row)
		df = pd.DataFrame({	'x': int_row})

		kmeans = KMeans(n_clusters=5)
		kmeans.fit(df)

		labels = kmeans.predict(df)
		centroids = kmeans.cluster_centers_

		for j in labels:
			print j, '\t',

		print
if __name__ == '__main__':
	main()
