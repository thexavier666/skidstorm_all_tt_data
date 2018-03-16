import csv

def do_transpose(some_2Dlist):
    y = zip(*some_2Dlist)
    z = []

    for i in y:
        z.append(list(i))

    return z

def write_2dlist_to_csv(some_2Dlist, some_file_name):
    fp = open(some_file_name, 'wb')
    writer = csv.writer(fp)
    writer.writerows(some_2Dlist)
