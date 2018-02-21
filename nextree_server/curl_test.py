'''
GET TOKEN
curl -X POST -d "username=staff1&password=4430515s" http://127.0.0.1:8000/api/auth/token/

TOKEN
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imp1bmtzb3VuZEBuYXZlci5jb20iLCJleHAiOjE1MTkyMDA5MTMsImVtYWlsIjoianVua3NvdW5kQG5hdmVyLmNvbSJ9.wZuPfEoM6c9226qyzNXJnZBQvDhVva8OpnN6aCZ9B60

Topic List (METHOD: GET)
curl http://127.0.0.1:8000/account/list/

curl http://127.0.0.1:8000/account/list/
curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imp1bmtzb3VuZEBuYXZlci5jb20iLCJleHAiOjE1MTkyMDAyOTYsImVtYWlsIjoianVua3NvdW5kQG5hdmVyLmNvbSJ9.Ez3qyffJElVWInbEa-xRBxYjrolNZB-anJpxycB9Vk0" http://127.0.0.1:8000/account/list/

Post Create(METHOD: POST)
curl -X POST -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imp1bmtzb3VuZEBuYXZlci5jb20iLCJleHAiOjE1MTkyMDA5MTMsImVtYWlsIjoianVua3NvdW5kQG5hdmVyLmNvbSJ9.wZuPfEoM6c9226qyzNXJnZBQvDhVva8OpnN6aCZ9B60" -H "Content-Type: application/json" -d '{"title":"post_curl", "tema":"tema1_edit", "url":"http://www.dadf.com","description":"dffffff"}' http://127.0.0.1:8000/post/create/


?user=admin
'''


