# WebCrawler

Function that create a map of the domain.

## Map of my own domain
You can find it here: https://github.com/zgrzebnickij/BlogApp

http://127.0.0.1:5000/
{'title': 'Flask Blog', 'links': {'http://127.0.0.1:5000/', 'http://127.0.0.1:5000/login', 'http://127.0.0.1:5000/register', 'http://127.0.0.1:5000/user/jj', 'http://127.0.0.1:5000/post/1', 'http://127.0.0.1:5000/post/2', 'http://127.0.0.1:5000/home', 'http://127.0.0.1:5000/about'}}
http://127.0.0.1:5000/post/1
{'title': 'Flask Blog - First post', 'links': {'http://127.0.0.1:5000/', 'http://127.0.0.1:5000/login', 'http://127.0.0.1:5000/register', 'http://127.0.0.1:5000/user/jj', 'http://127.0.0.1:5000/home', 'http://127.0.0.1:5000/about'}}
http://127.0.0.1:5000/post/2
{'title': 'Flask Blog - Second post', 'links': {'http://127.0.0.1:5000/', 'http://127.0.0.1:5000/login', 'http://127.0.0.1:5000/register', 'http://127.0.0.1:5000/user/jj', 'http://127.0.0.1:5000/home', 'http://127.0.0.1:5000/about'}}
http://127.0.0.1:5000/user/jj
{'title': 'Flask Blog', 'links': {'http://127.0.0.1:5000/', 'http://127.0.0.1:5000/login', 'http://127.0.0.1:5000/register', 'http://127.0.0.1:5000/user/jj', 'http://127.0.0.1:5000/post/1', 'http://127.0.0.1:5000/post/2', 'http://127.0.0.1:5000/home', 'http://127.0.0.1:5000/about'}}
http://127.0.0.1:5000/register
{'title': 'Flask Blog - register', 'links': {'http://127.0.0.1:5000/', 'http://127.0.0.1:5000/login', 'http://127.0.0.1:5000/register', 'http://127.0.0.1:5000/home', 'http://127.0.0.1:5000/about'}}
http://127.0.0.1:5000/login
{'title': 'Flask Blog - login', 'links': {'http://127.0.0.1:5000/', 'http://127.0.0.1:5000/login', 'http://127.0.0.1:5000/register', 'http://127.0.0.1:5000/reset_password', 'http://127.0.0.1:5000/home', 'http://127.0.0.1:5000/about'}}
http://127.0.0.1:5000/reset_password
{'title': 'Flask Blog - Reset Password', 'links': {'http://127.0.0.1:5000/', 'http://127.0.0.1:5000/login', 'http://127.0.0.1:5000/register',
'http://127.0.0.1:5000/home', 'http://127.0.0.1:5000/about'}}
http://127.0.0.1:5000/about
{'title': 'Flask Blog - About', 'links': {'http://127.0.0.1:5000/', 'http://127.0.0.1:5000/login', 'http://127.0.0.1:5000/register', 'http://127.0.0.1:5000/blank', 'http://127.0.0.1:5000/home', 'http://127.0.0.1:5000/about'}}
http://127.0.0.1:5000/blank
{'title': 'No title or links', 'links': set()}
http://127.0.0.1:5000/home
{'title': 'Flask Blog', 'links': {'http://127.0.0.1:5000/', 'http://127.0.0.1:5000/login', 'http://127.0.0.1:5000/register', 'http://127.0.0.1:5000/user/jj', 'http://127.0.0.1:5000/post/1', 'http://127.0.0.1:5000/post/2', 'http://127.0.0.1:5000/home', 'http://127.0.0.1:5000/about'}}


