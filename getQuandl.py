#!/usr/bin/env python
import Quandl
import csv
import time
import urllib2

search_count = 0
start_search_time = time.time()
end_search_time = start_search_time
get_count = 0
start_get_time = time.time()
end_get_time = start_get_time
total_count = 0

def is_time(search):
    global start_search_time
    global end_search_time
    global search_count
    global start_get_time
    global end_get_time
    global get_count
    global total_count
    if search:
        if (time.time() - start_search_time >= 60) and search_count == 60:
            start_search_time = time.time()
            search_count = 0
        elif (time.time() - start_search_time < 60) and search_count == 60:
            print "waiting: " + str(60.0 - (time.time() - start_search_time))
            wait_time = 60 - (time.time() - start_search_time)
            if( wait_time < 0):
                time.sleep(-wait_time)
            else:
                time.sleep(wait_time)
            start_search_time = time.time()
            search_count = 0
        else:
            search_count = search_count + 1
    if not search:
        total_count = total_count + 1
        print 'Total count: ' + str(total_count)
        print 'Time: ' + str(time.time() - start_get_time)
        if (time.time() - start_get_time >= 10.0*60.0) and get_count == 1999:
            start_get_time = time.time()
            print "waiting: " + str(time.sleep(5))
            time.sleep(5)
            get_count = 0
        elif (time.time() - start_get_time < 10.0*60.0) and get_count == 1999:
            print "waiting: " + str(10.0*60.0 - (time.time() - start_get_time))
            time.sleep(10*60 - (time.time() - start_get_time))
            start_get_time = time.time()
            get_count = 0
        else:
            get_count = get_count + 1

def csv_write(filename, data):
    with open(filename, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(['Code', 'Name'])
        for row in data:
            row = [c.encode('utf8') if isinstance(c, unicode) else c for c in row]
            writer.writerow(row)
            
def update_dataset_csv(token, source, filename):    
    dataset_info = []
    
    for page in range(1, 6910): #7414
        is_time(True);
        print page
        datasets = None
        while datasets is None:
            try:
                datasets = Quandl.search(query = "*", source = source, page = page, verbose = False, authtoken=token)
            except urllib2.URLError:
                print 'none'
                pass
        for dataset in datasets:
            dataset_info.append( [dataset['code'], dataset['name']] )
    csv_write(filename, dataset_info)

def retrieve_dataset_codes(filename):
    dataset_codes = []
    with open(filename, "rb") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            dataset_codes.append(row)
    return dataset_codes[1:]
    
def get_dataset_information(token, source, dataset_codes):
    for code in dataset_codes:
        is_time(False)
        data = None
        while data is None:
            try:
                data = Quandl.get(code[0], authtoken=token)
            except urllib2.URLError:
                print 'nope'
                pass
            except urllib2.HTTPError:
                print 'nope'
                pass
        if ('/' in code[1]):
            code[1] = code[1].replace('/', '-')
        data.to_csv(source + '/' + code[0][5:] + '_' + code[1] + '.csv')
        print 'FRED/' + code[0][5:] + '_' + code[1]

if __name__ == "__main__":
    #API key
    #token = "7nDGyEXKUdFxwLGeWpmW"
    token = 'yiaV93DYtQRBNzQzRq1G'
    source = 'FRED'
    filename = source + '_datasets.csv'
    
    #update_dataset_csv(token, source, filename);
    #print "update_dataset_csv done"
    data_codes = retrieve_dataset_codes(filename)
    print "data_codes done"
    get_dataset_information(token, source, data_codes)
