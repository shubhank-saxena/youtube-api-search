## Youtube API Search
This project aims to make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

## Tech Stack
- Asyncio for fetching videos from YouTube.
- Django for backend server.
- React for frontend server.
- SQLite for database.
- nginx for url managements and static serving.

## API Description
 - To get all videos: http://localhost:8000/getvideos/?q=&page=1
 - To search with a query along with pagination: http://localhost:8000/getvideos/?q=messi&page=1
 <br><br>
 <b>Note:</b> By default I'm only fetching music videos from www.youtube.com in every 5 minutes. 
   But you can change that by replacing the `'search_query': <your_tag>` in settings.py
   before firing the <b>Docker</b>

## Docker Instructions
```
$ docker-compose build
$ docker-compose up
```
Now navigate to localhost:3000
### How to <i>Configure</i>
 - Settings.py : add your search query for which the job will insert entries in database. Currently it's set to 
 - Append your API_KEY to backend/keys.json file which you obtained from https://console.developers.google.com/apis/api/youtube.googleapis.com/ 
