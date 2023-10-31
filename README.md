# YouTube Playlist Length Calculator

This Python project calculates the total duration of a YouTube playlist based on the provided URL. It utilizes the YouTube Data API to fetch information about the playlist and the videos it contains. The project also uses the `dotenv` and `isodate` Python modules for managing environment variables and parsing video durations, respectively.

![](https://imgur.com/a/1GhP74h)

## Dependencies

Firstly you will need a YouTube Data API key. You can read about it [here](https://developers.google.com/youtube/v3/getting-started)

To run this project, you will need to install the following Python packages:

- `dotenv`: For managing environment variables securely.
- `isodate`: For parsing video durations from ISO formats.
- `googgle-api-client`: For using the YouTube Data API. 

You can install these dependencies using pip:
```
pip install python-dotenv isodate
pip install --upgrade google-api-python-client
```
## How to Use It

To use the project, follow these steps:

1. Clone the project repository to your local machine.

2. Install the dependencies.

2. Set up your YouTube Data API key by creating a `.env` file in the project's root directory and adding your API key as follows:

   ```env
   YOUTUBE_API_KEY=your_api_key_here
   ```

3. Run `main.py` to execute the program. Either provide a YouTube playlist URL along in shell or when prompted.
    ```
    python yt_playlist_length.py 'https://www.youtube.com/watch?v=C9S8L_giVz0&list=PL54Fx8wLxTCmrWmZYTlIcumPs8KI-GPlC'
    ```
4. The program will fetch the playlist information and display the total duration in hours, minutes, and seconds.
## How It Works

The project fetches the playlist data using the YouTube Data API and calculates the total duration by summing the durations of all videos in the playlist. Here's a brief overview of how it works:

1. `retrieve_playlist_id.py` is responsible for extracting the playlist ID from the provided YouTube playlist URL.
2. The `yt_api.py` module interacts with the YouTube Data API to retrieve playlist information and video details.
3. `time_calculator.py` calculates the total duration of all videos in the playlist.
4. `display_results.py` displays the calculated playlist length to the user.

