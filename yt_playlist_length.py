# input se string le aao function
import sys
url = sys.argv

test_str=url[1]

sub1 = "list="
sub2 = "&"
 
idx1 = test_str.find(sub1)
if idx1 ==-1 :
    idx1=0

idx2 = test_str[idx1:].find(sub2)
if idx2==-1:
    idx2=len(test_str)
else:
    idx2+=idx1
print(idx1,idx2)

res = test_str[idx1 + len(sub1)  : idx2]
 
print("The extracted string : " + res)

#fetch all the data for this playlist
from yt_doc import apiCall
api_result_durations = apiCall(res)
print(api_result_durations)

# calculate len/numvides/2x,1.5x etc
from time_calculator import calculate_times
calculate_times(api_result_durations)

#display this data

