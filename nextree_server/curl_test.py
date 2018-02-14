'''
GET TOKEN
curl -X POST -d "username=staff1&password=4430515s" http://127.0.0.1:8000/api/auth/token/

TOKEN
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imp1bmtzb3VuZCIsImV4cCI6MTUxODYwNTgxMiwiZW1haWwiOiJ3b20yMjc3QG5hdmVyLmNvbSJ9.rMlUNdA3KSPCFnXG8vQBnWRswrRidjeTZOVEZrQNbwc

Topic List (METHOD: GET)
curl http://127.0.0.1:8000/account/list/

curl http://127.0.0.1:8000/account/list/
curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imp1bmtzb3VuZCIsImV4cCI6MTUxODYwNzEyMywiZW1haWwiOiJ3b20yMjc3QG5hdmVyLmNvbSJ9.7GXNlOjXSBxXhMxsw0Z2XN9NyVD-QIag3kr7dhUr7Ss" http://127.0.0.1:8000/account/list/

Post Create(METHOD: POST)
curl -X POST -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6InN0YWZmMSIsImV4cCI6MTUxODE1MTg4MywiZW1haWwiOiIifQ.yl5JEBOwh-rlhXsEMomM28JZ6SebjXW8NULdkq9C7UY" -H "Content-Type: application/json" -d '{"tema":1,"title":"postcurl2","url":"http://www.postcurl2.com","description":"postcurldescription2","content":"postcurlcontent2"}' http://localhost:8000/post/create/


?user=admin
'''


