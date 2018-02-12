'''
GET TOKEN
curl -X POST -d "username=staff1&password=4430515s" http://127.0.0.1:8000/api/auth/token/

TOKEN
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6InN0YWZmMSIsImV4cCI6MTUxODE1MjM5MSwiZW1haWwiOiIifQ.A29OIOczz4_mF6qZI9q9cuJJUaDcF2Lq7G07KMG6Yrk

Topic List (METHOD: GET)
curl -H http://13.125.173.238/topic/list/

Post Create(METHOD: POST)
curl -X POST -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6InN0YWZmMSIsImV4cCI6MTUxODE1MTg4MywiZW1haWwiOiIifQ.yl5JEBOwh-rlhXsEMomM28JZ6SebjXW8NULdkq9C7UY" -H "Content-Type: application/json" -d '{"tema":1,"title":"postcurl2","url":"http://www.postcurl2.com","description":"postcurldescription2","content":"postcurlcontent2"}' http://localhost:8000/post/create/


?user=admin
'''


