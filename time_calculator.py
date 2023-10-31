from isodate import parse_duration
def calculate_times(video_durations_iso):
    total_seconds = 0
    number_of_videos= len(video_durations_iso)
    print("Total number of videos: ",number_of_videos)
        
    for iso_duration in video_durations_iso:
        total_seconds+=parse_duration(iso_duration).total_seconds()
    display_times(total_seconds)


def stringify_time(seconds):
    seconds=int(seconds)
    minutes,seconds = divmod(seconds,60)
    hours, minutes = divmod(minutes,60)
    
    output_string=""
    output_string+= str(hours) +" hours\t" if hours else "\t"
    output_string+= str(minutes) + " minutes\t" if minutes else "\t"  
    output_string+= str(seconds) + " seconds"  if seconds else ""       
    
    return output_string

def display_times(time_in_seconds):
    speed_factors=[1, 1.25, 1.5, 1.75,2]
    for speed in speed_factors:
        print( f'At {speed:.2f}x speed: {stringify_time(time_in_seconds/speed)}' )
