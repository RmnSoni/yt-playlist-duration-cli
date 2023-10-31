import sys
from src.display_results import display_times
from src.retrieve_playlist_id import retrieve_pl_id
from src.time_calculator import calculate_times
from src.yt_api import apiCall

def main():
#---parsing input
    url = sys.argv
    if len(url)<2: 
        print("ERROR: No URL Entered")
        return
#---fetch playlistID from URL
    pl_id=retrieve_pl_id(url[1])

#---fetch all the data for this playlist
    api_result_durations = apiCall(pl_id)

#---Parsing api result
    total_duration,number_of_videos = calculate_times(api_result_durations)

#---display the final results
    display_times(total_duration, number_of_videos)
    return

if __name__ == "__main__":
    main()
