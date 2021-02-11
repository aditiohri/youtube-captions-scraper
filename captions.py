filename = 'videolist.csv'			# filname with video ids
colname = 'videoId'					# column storing video ids
delimiter = '\t'                    # delimiter, e.g. ',' for CSV or '\t' for TAB

import csv
import os.path
import json

from youtube_transcript_api import YouTubeTranscriptApi

# get transcript data and write transcript file
def get_transcript(video_id):

    # check if transcript file already exists
    writefilename = 'subtitles/transcript_' + video_id + '.txt'
    if os.path.isfile(writefilename):
        msg = 'transcript file already exists'
        return msg
    
    # retrieve video transcript
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
    except: 
        msg = 'error retrieving transcript'
        return msg

    # create dictionary from transcript 
    data = {}
    data["transcript"] = []
    for element in transcript:
        data["transcript"].append(element)

    # write transcript file
    with open(writefilename, "w") as outfile:
        json.dump(data, outfile)
   
    return 'success'

# create log file
logwrite = open('captions.log','w',newline='\n')
logwriter = csv.DictWriter(logwrite, fieldnames=['id','msg'])
logwriter.writeheader()

# write log file
def log_actions(id, msg):
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