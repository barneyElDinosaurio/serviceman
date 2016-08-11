import requests

#r = requests.post('http://httpbin.org/post', data = {'keyClient':'value','emailAddress':'value','gender':'value',
#	'birthday':'value','role':'value','providerIdFacebook':'value','finalURL':'value','name':'value','lastName':'value'
#	,'firebaseId':'value'})

#3.USER GET
#payload = {
#	'idWebUser':'ahBzfnBydWViYWRhdGVwbGF5ci4LEgRVc2VyIiQ3Yzg5NTdkOS02NTQzLTQxZTYtYTcwYS1mMjY0ODg1ZTFiMWMM'
#	,'tokenClient':'69556b7cd6d214504a5d177567961e1f'
#	,'idToken':'ahBzfnBydWViYWRhdGVwbGF5cl0LEgRVc2VyIiQ3Yzg5NTdkOS02NTQzLTQxZTYtYTcwYS1mMjY0ODg1ZTFiMWMMCxIFVG9rZW4iJDgyZjdiZTAyLWMwZDYtNGUxNC04NjQxLWNlNGQwM2JkZmVlZgw'}
idWebUser = 'ahBzfnBydWViYWRhdGVwbGF5ci4LEgRVc2VyIiQ3Yzg5NTdkOS02NTQzLTQxZTYtYTcwYS1mMjY0ODg1ZTFiMWMM'
tokenClient = '69556b7cd6d214504a5d177567961e1f'
idToken = 'ahBzfnBydWViYWRhdGVwbGF5cl0LEgRVc2VyIiQ3Yzg5NTdkOS02NTQzLTQxZTYtYTcwYS1mMjY0ODg1ZTFiMWMMCxIFVG9rZW4iJDgyZjdiZTAyLWMwZDYtNGUxNC04NjQxLWNlNGQwM2JkZmVlZgw'
r = requests.get('https://pruebadateplay.appspot.com/_ah/api/userEndpoint/v1/user/'+idWebUser+'/'+tokenClient+'/'+idToken)
#5.USER TOKEN REFRESH
#r = requests.post('https://pruebadateplay.appspot.com/_ah/api/userEndpoint/v1/refreshToken/', data = {
#	'tokenRefresh':'a680c6ef07be191e9449ea204413a2ae'
#	,'idToken':'ahBzfnBydWViYWRhdGVwbGF5cl0LEgRVc2VyIiQ3Yzg5NTdkOS02NTQzLTQxZTYtYTcwYS1mMjY0ODg1ZTFiMWMMCxIFVG9rZW4iJDgyZjdiZTAyLWMwZDYtNGUxNC04NjQxLWNlNGQwM2JkZmVlZgw'
#	,'keyClient':'NKuMGj3giNnq4jy9Dr8p593uNolu5dW9'})

#9.USER TOKEN REFRESH
#r = requests.get('https://pruebasdateplay.appspot.com/_ah/api/userEndpoint/v1/refreshToken/', data = {
#	'tokenRefresh':'a680c6ef07be191e9449ea204413a2ae'
#	,'idToken':'ahBzfnBydWViYWRhdGVwbGF5cl0LEgRVc2VyIiQ3Yzg5NTdkOS02NTQzLTQxZTYtYTcwYS1mMjY0ODg1ZTFiMWMMCxIFVG9rZW4iJDgyZjdiZTAyLWMwZDYtNGUxNC04NjQxLWNlNGQwM2JkZmVlZgw'
#	,'keyClient':'NKuMGj3giNnq4jy9Dr8p593uNolu5dW9'})


#r = requests.post('https://pruebadateplay.appspot.com/_ah/api/userEndpoint/v1/refreshToken/', data = {
#	'tokenRefresh':'a680c6ef07be191e9449ea204413a2ae'
#	,'idToken':'ahBzfnBydWViYWRhdGVwbGF5cl0LEgRVc2VyIiQ3Yzg5NTdkOS02NTQzLTQxZTYtYTcwYS1mMjY0ODg1ZTFiMWMMCxIFVG9rZW4iJDgyZjdiZTAyLWMwZDYtNGUxNC04NjQxLWNlNGQwM2JkZmVlZgw'
#	,'keyClient':'NKuMGj3giNnq4jy9Dr8p593uNolu5dW9'})

print(r.text)