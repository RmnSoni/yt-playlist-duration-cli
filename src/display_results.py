def stringify_time(seconds):
    seconds=int(seconds)
    minutes,seconds = divmod(seconds,60)
    hours, minutes = divmod(minutes,60)
    
    output_string=""
    output_string+= str(hours) +" hours, \t" if hours else "\t"
    output_string+= str(minutes) + " minutes, \t" if minutes else "\t"  
    output_string+= str(seconds) + " seconds"  if seconds else ""       
    
    return output_string

def display_times(time_in_seconds,number_of_videos):
    speed_factors=[1, 1.25, 1.5, 1.75,2]
    print()
    print("Total number of videos:",number_of_videos)
    print("Average Video Duration:", stringify_time(time_in_seconds//number_of_videos))
    print()
    for speed in speed_factors:
        print( f'At {speed}x speed\t: {stringify_time(time_in_seconds/speed)}' )
