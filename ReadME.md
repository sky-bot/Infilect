So we have to build 6 APIs, there is little change in urls
**1. Login API:**
For login i am using Djoser(third party) build on top
 of rest auth

http://localhost:8000/api/v1/token/login

This is post API, you need to send
 
username = "akash"    password = "qaws1234"

Refer to screen shots S1.1

You will get a token as a response.

**2.Groups Info API**

Purpose to show all groups info with pagination

http://localhost:8000/api/v1/groups

You need to send the following in headers

Authorization : Token token_you_get_from_login

You can refer to Screenshots: S2.2

Response Structure:

{
    "links": 
    {
        "next": null,
        "previous": null
    },
    "count": 4,
    "result": [
        {}, {}, {}, {}
    ]
}

**3.Group photo API by group_id API**

This api will give all the photos, belongs to that 
particular group. By default I gave page size = 15

http://localhost:8000/api/v1/group/583098@N23

You need to send the following in headers

Authorization : Token token_you_get_from_login

Response Structure:

{
    "links": 
    {
        "next": "http://localhost:8000/api/v1/group/583098@N23/?page=2",
        "previous": null
    },
    "count": 30,
    "result": [
        {}, {}, {}, {} ....
    ]
}

For reference look into S3.1

4.All photo belongs to group_id API

I dont see any difference between 3rd and 4th API, So responce 
is same, just getting group_id is different in 3rd and 4th API

http://localhost:8000/api/v1/photos?group=1225814@N24

You need to send the following in headers

Authorization : Token token_you_get_from_login

{
    "links": 
    {
        "next": "http://localhost:8000/api/v1/group/583098@N23/?page=2",
        "previous": null
    },
    "count": 30,
    "result": [
        {}, {}, {}, {} ....
    ]
}

For reference look into S4.1

**5. Photo Info API**

This api will give Photo info.

http://localhost:8000/api/v1/photos/49548820753/

You need to send the following in headers

Authorization : Token token_you_get_from_login

Sample response
[
    {
        "photo_id": 49548820753,
        "owner_id": "137210102@N02",
        "server": "65535",
        "farm": 66,
        "title": "Torta caprese ricetta originale",
        "is_public": true,
        "owner_name": "La petite Maison Sucrée",
        "date_added": "2020-02-17T20:03:46Z",
        "group_id": "583098@N23"
    }
]

**6. LogOut API**

This is POST API, you need to send.

You need to send the following in headers

Authorization : Token token_you_get_from_login

You wont get any response in this API, apart from 204 No Content Response.
Post this api you wont be able to use Authorization token  

http://localhost:8000/api/v1/token/logout


