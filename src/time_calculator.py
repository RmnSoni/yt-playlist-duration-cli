from isodate import parse_duration
def calculate_times(video_durations_iso):
    total_seconds = 0
    number_of_videos= len(video_durations_iso)
        
    for iso_duration in video_durations_iso:
        total_seconds+=parse_duration(iso_duration).total_seconds()

    return(total_seconds,number_of_videos)
