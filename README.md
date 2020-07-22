# api-auth


#### Register:
curl -X POST http://127.0.0.1:8000/auth/users/ --data "username=Test&email=testcurl@gmaial.com&password=curl1234&re_password=curl1234"

#### user's detail 
curl -LX GET http://127.0.0.1:8000/auth/users/me/

#### login 
curl -X POST http://127.0.0.1:8000/auth/token/login/ --data "email=hananihoum2016@gmail.com&password=hanane123"

#### user's detail 
curl -LX GET http://127.0.0.1:8000/auth/users/me/ -H "Authorization: Token f6a28dbe42aaebdb0794b6e4dc5deed7cda2997f"

#### logout
curl -X POST http://127.0.0.1:8000/auth/token/logout/ -H "Authorization: Token f6a28dbe42aaebdb0794b6e4dc5deed7cda2997f"

