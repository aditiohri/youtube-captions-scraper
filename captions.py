filename = 'videolist.csv'			# filname with video ids
colname = 'videoId'					# column storing video ids
delimiter = '\t'                    # delimiter, e.g. ',' for CSV or '\t' for TAB

import csv

# read csv to get video id
# call get transcript with video id
# call log_actions to prepare log file

def get_transcript(video_id):
    return video_id

# prepare log file

# log function
def log_actions(id, msg):
    logwrite = open('captions.log','w',newline='\n')
    logwriter = csv.DictWriter(logwrite, fieldnames=['id','msg'])
    logwriter.writeheader()
    logwriter.writerow({'id':id,'msg':msg})

# read CSV file
def read_csv():
    csvread = open(filename, newline='\n')
    csvreader = csv.DictReader(csvread, delimiter=delimiter, quoting=csv.QUOTE_NONE)
    rowcount = len(open(filename).readlines())

    for row in csvreader:
        msg = get_transcript(row[colname])
        log_actions(row[colname],msg)
        rowcount -= 1
        print(str(rowcount) + " :  " + row[colname] + " : " + msg)

def init():
    return read_csv()

init()