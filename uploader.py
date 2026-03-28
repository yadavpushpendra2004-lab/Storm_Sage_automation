import os
import pickle
import datetime
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# ==========================================
# AUTHENTICATION (Wahi purana logic)
# ==========================================
def get_authenticated_service():
    credentials = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', 
                ['https://www.googleapis.com/auth/youtube.upload']
            )
            credentials = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)
    return build('youtube', 'v3', credentials=credentials)

# ==========================================
# SCHEDULING LOGIC
# ==========================================
def schedule_short_folder(folder_path):
    meta_path = os.path.join(folder_path, "metadata.txt")
    video_path = os.path.join(folder_path, "video.mp4")

    # 1. Metadata Read karna
    metadata = {}
    try:
        with open(meta_path, 'r', encoding='utf-8') as f:
            for line in f:
                if ':' in line:
                    key, val = line.split(':', 1)
                    metadata[key.strip()] = val.strip()
    except Exception as e:
        print(f"Error reading metadata in {folder_path}: {e}")
        return

    # 2. Time Logic (ISO format conversion)
    # Metadata: 2026-03-17 10:00 -> YouTube: 2026-03-17T10:00:00Z
    raw_time = metadata.get('SCHEDULE_TIME', '')
    scheduled_iso = raw_time.replace(" ", "T") + ":00Z"

    youtube = get_authenticated_service()

    request_body = {
        'snippet': {
            'title': metadata.get('TITLE', 'New Short')[:100], # Automatic 100 char limit
            'description': metadata.get('DESCRIPTION', ''),
            'tags': ['Shorts', 'StormSage', 'Space'],
            'categoryId': '27'
        },
        'status': {
            'privacyStatus': 'private', # Schedule ke liye private hona must hai
            'publishAt': scheduled_iso,
            'selfDeclaredMadeForKids': False
        }
    }

    media = MediaFileUpload(video_path, chunksize=-1, resumable=True)

    print(f"🚀 Processing: {folder_path}")
    print(f"⏰ Scheduling for: {scheduled_iso}")
    
    try:
        response = youtube.videos().insert(
            part='snippet,status',
            body=request_body,
            media_body=media
        ).execute()
        print(f"✅ SUCCESS! Video ID: {response['id']}")
    except Exception as e:
        print(f"❌ Failed to upload {folder_path}: {e}")

# ==========================================
# MAIN EXECUTION (Scan all folders)
# ==========================================
if __name__ == "__main__":
    queue_dir = "Shorts_Queue"
    
    if not os.path.exists(queue_dir):
        print(f"Folder '{queue_dir}' nahi mila!")
    else:
        folders = [f for f in os.listdir(queue_dir) if os.path.isdir(os.path.join(queue_dir, f))]
        print(f"Found {len(folders)} shorts in queue.")
        
        for folder in folders:
            full_path = os.path.join(queue_dir, folder)
            schedule_short_folder(full_path)