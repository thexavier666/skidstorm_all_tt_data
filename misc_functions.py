import unicodecsv as csv

def do_transpose(some_2Dlist):
    y = zip(*some_2Dlist)
    z = []

    for i in y:
        z.append(list(i))

    return z

def convert_2dlist_to_unicode(some_2Dlist):
    tmp_2Dlist = []

    for row in some_2Dlist:
        tmp_row = [s.encode('utf-8') for s in row]
        tmp_2Dlist.append(tmp_row)

    return tmp_2Dlist

def write_2dlist_to_csv(some_2Dlist, some_file_name):
    fp = open(some_file_name, 'wb')
    writer = csv.writer(fp, encoding='utf-8')
    writer.writerows(some_2Dlist)
