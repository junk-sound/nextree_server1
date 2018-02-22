'''
GET TOKEN
curl -X POST -d "email=wekimeki@naver.com&password=4430515s" http://127.0.0.1:8000/account/login/

TOKEN
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6Indla2ltZWtpQG5hdmVyLmNvbSIsImV4cCI6MTUxOTMwMTUyNSwiZW1haWwiOiJ3ZWtpbWVraUBuYXZlci5jb20ifQ.F2RwdfZxpjmw_EwFjI7ipiElFF0zUeiNmKIxLqFA1y4

Category Create

curl -X POST -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6Indla2ltZWtpQG5hdmVyLmNvbSIsImV4cCI6MTUxOTMwMTUyNSwiZW1haWwiOiJ3ZWtpbWVraUBuYXZlci5jb20ifQ.F2RwdfZxpjmw_EwFjI7ipiElFF0zUeiNmKIxLqFA1y4" -H "Content-Type: application/json" -d '{"category_name":"category_curl"}' http://127.0.0.1:8000/category/create/

Topic List (METHOD: GET)
curl http://127.0.0.1:8000/account/list/

curl http://127.0.0.1:8000/account/list/
curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imp1bmtzb3VuZEBuYXZlci5jb20iLCJleHAiOjE1MTkyMDAyOTYsImVtYWlsIjoianVua3NvdW5kQG5hdmVyLmNvbSJ9.Ez3qyffJElVWInbEa-xRBxYjrolNZB-anJpxycB9Vk0" http://127.0.0.1:8000/account/list/

Post Create(METHOD: POST)
curl -X POST -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imp1bmtzb3VuZEBuYXZlci5jb20iLCJleHAiOjE1MTkyMDA5MTMsImVtYWlsIjoianVua3NvdW5kQG5hdmVyLmNvbSJ9.wZuPfEoM6c9226qyzNXJnZBQvDhVva8OpnN6aCZ9B60" -H "Content-Type: application/json" -d '{"title":"post_curl", "tema":"tema1_edit", "url":"http://www.dadf.com","description":"dffffff"}' http://127.0.0.1:8000/post/create/


?user=admin
'''


