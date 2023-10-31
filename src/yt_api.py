import os
from dotenv import load_dotenv 
import googleapiclient.discovery

load_dotenv()

def apiCall(playlistId):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.getenv("YT_API_KEY")

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)
    
    nextToken=None
    duration_list=[]
    
    while True:
        video_ids_list=[]
        pl_request = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=playlistId,
            maxResults=50,
            pageToken=nextToken
        )
        pl_response = pl_request.execute()
        #TODO : TRY CATCH FOR ERROR CODE
        for item in pl_response["items"]:
            video_ids_list.append(item["contentDetails"]["videoId"])
        videos_req = youtube.videos().list(
            part="contentDetails",
            id=",".join(video_ids_list)
        )

        videos_response=videos_req.execute()
        #TODO : try CATCH implementation
        for item in videos_response["items"]:
            duration_list.append(item['contentDetails']['duration'])
    
        nextToken=pl_response.get("nextPageToken")
        if not nextToken: break

    return(duration_list)
