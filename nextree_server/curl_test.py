'''
GET TOKEN
curl -X POST -d "username=staff1&password=4430515s" http://127.0.0.1:8000/api/auth/token/

TOKEN
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6Indla2ltZWtpQG5hdmVyLmNvbSIsImV4cCI6MTUxODYyNTM5OSwiZW1haWwiOiJ3ZWtpbWVraUBuYXZlci5jb20ifQ.tp7p-q4ccQm6vIEi6VZ4tY7QLYfoVRsLIRbPMl2A0sU

Topic List (METHOD: GET)
curl http://127.0.0.1:8000/account/list/

curl http://127.0.0.1:8000/account/list/
curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6Indla2ltZWtpQG5hdmVyLmNvbSIsImV4cCI6MTUxODYyNTA5NSwiZW1haWwiOiJ3ZWtpbWVraUBuYXZlci5jb20ifQ.AsKJRaIINkXGFtwA04jP8L8GP_n2e-IcNW0djQPpnKM" http://127.0.0.1:8000/account/list/

Post Create(METHOD: POST)
curl -X POST -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6Indla2ltZWtpQG5hdmVyLmNvbSIsImV4cCI6MTUxODYyNTM5OSwiZW1haWwiOiJ3ZWtpbWVraUBuYXZlci5jb20ifQ.tp7p-q4ccQm6vIEi6VZ4tY7QLYfoVRsLIRbPMl2A0sU" -H "Content-Type: application/json" -d '{"tema":1,"title":"postcurl3","url":"http://www.postcurl3.com","description":"postcurldescription3","content":"postcurlcontent3"}' http://127.0.0.1:8000/post/create/


?user=admin
'''


