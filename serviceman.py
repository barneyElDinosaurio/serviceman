import requests

#USER VARIABLES
#oUser = 
clientId = 'ahBzfnBydWViYWRhdGVwbGF5cl0LEgRVc2VyIiQ3Yzg5NTdkOS02NTQzLTQxZTYtYTcwYS1mMjY0ODg1ZTFiMWMMCxIFVG9rZW4iJDgyZjdiZTAyLWMwZDYtNGUxNC04NjQxLWNlNGQwM2JkZmVlZgw'
idUser = '7c8957d9-6543-41e6-a70a-f264885e1b1c' 
keyClient = 'NKuMGj3giNnq4jy9Dr8p593uNolu5dW9'
idWebUser = 'ahBzfnBydWViYWRhdGVwbGF5ci4LEgRVc2VyIiQ3Yzg5NTdkOS02NTQzLTQxZTYtYTcwYS1mMjY0ODg1ZTFiMWMM'
token = '807ad19edf202bbb76b076402b140ac9'
tokenClient = '807ad19edf202bbb76b076402b140ac9'
tokenRefresh = '470cd0ed9ec455d28bf4b290a8de74f2'
idToken = 'ahBzfnBydWViYWRhdGVwbGF5cl0LEgRVc2VyIiQ3Yzg5NTdkOS02NTQzLTQxZTYtYTcwYS1mMjY0ODg1ZTFiMWMMCxIFVG9rZW4iJDgyZjdiZTAyLWMwZDYtNGUxNC04NjQxLWNlNGQwM2JkZmVlZgw'
#idUserCandidate = 
#block = 
#IMGS
#idImage = 
#linkToNewPicture = 	
#photoId = 
#privateImage = 
#file = 

#QUESTION VARIABLES
#idQuestion = 
#safeWebAnswerOptionId = 

SERVER ='https://pruebadateplay.appspot.com'

#1.USER LOGIN AND CREATION(POST)
#r = requests.post(SERVER+'/_ah/api/userEndpoint/v1/storeUser/')

#2.USER UPDATE(PUT)??wt is objectUser?
#r = requests.put(SERVER+'/_ah/api/userEndpoint/v1/answers/'+oUser+'/'+tokenClient+'/'+idToken)

#3.USER UPDATE(GET)good but so slow
#r = requests.get(SERVER+'/_ah/api/userEndpoint/v1/user/'+idWebUser+'/'+tokenClient+'/'+idToken)

#4.USER DELETE(DELETE)not tested
#r = requests.delete(SERVER+'/_ah/api/userEndpoint/v1/user/'+idWebUser+'/'+tokenClient+'/'+idToken)

#5.USER TOKEN SOFRESH(POST)good, but dont use so much because u need change ur variable tokenClient
#r = requests.post(SERVER+'/_ah/api/userEndpoint/v1/refreshToken/'+tokenRefresh+'/'+idToken+'/'+keyClient)

#6.NOTIFICATIONS UPDATE(PUT)error, this service havnt unique clientId and token by user?
#r = requests.put(SERVER+'/_ah/api/userEndpoint/v1/user/updateNotificationSettings?appSounds=false&appVibrations=false&clientId=ahFzfnBydWViYXNkYXRlcGxheXJdCxIEVXNlciIkMzFjZmQyMmQtOTg2OC00NjU2LTkxMzktZjUyMzQzYzYzYmU0DAsSBVRva2VuIiQ3OTJlODA0NS00ZjMxLTRkYWYtYjY3Yy1iMzQ5Mzc3YzRiYjIM&idWebUser=ahFzfnBydWViYXNkYXRlcGxheXIuCxIEVXNlciIkMzFjZmQyMmQtOTg2OC00NjU2LTkxMzktZjUyMzQzYzYzYmU0DA&matchNotifications=false&messageNotifications=false&token=90b1bcae833afe544d84aa42b297a929')

#7.PREFERENCE UPDATE(PUT)error, maybe the uniques clientId and token need to be changed to my tester server @pruebadateplay@
#r = requests.put(SERVER+'/_ah/api/userEndpoint/v1/user/updateSearchPreferences?genderPreference=B&clientId=ahFzfnBydWViYXNkYXRlcGxheXJdCxIEVXNlciIkMjdiNzFiOTctNjVkNy00NDY2LTlhN2MtODQzYmMzNzIxNzc2DAsSBVRva2VuIiQ5N2M4MWUzMy04YjlkLTQ1YzYtODMzMy04NDhmNDcxZjgxMzMM&idWebUser=ahFzfnBydWViYXNkYXRlcGxheXIuCxIEVXNlciIkMjdiNzFiOTctNjVkNy00NDY2LTlhN2MtODQzYmMzNzIxNzc2DA&maximumAge=25&minimumAge=18&radioPreference=100&token=330c9bdc63a960c96d8d3ba967db7609')

#8.STORE USER ANSWER(POST)not tested because i need the question things
#r = requests.post(SERVER+'https://pruebasdateplay.appspot.com/_ah/api/userEndpoint/v1/storeUserAnswer/ahFzfnBydWViYXNkYXRlcGxheXIuCxIEVXNlciIkMjdiNzFiOTctNjVkNy00NDY2LTlhN2MtODQzYmMzNzIxNzc2DA/330c9bdc63a960c96d8d3ba967db7609/ahFzfnBydWViYXNkYXRlcGxheXJdCxIEVXNlciIkMjdiNzFiOTctNjVkNy00NDY2LTlhN2MtODQzYmMzNzIxNzc2DAsSBVRva2VuIiQ5N2M4MWUzMy04YjlkLTQ1YzYtODMzMy04NDhmNDcxZjgxMzMM/0383915a-38e2-4fa9-827f-5e765f3600b3/ahFzfnBydWViYXNkYXRlcGxheXKVAQsSCFF1ZXN0aW9uIiQwMzgzOTE1YS0zOGUyLTRmYTktODI3Zi01ZTc2NWYzNjAwYjMMCxIDUFZDIiRhMThmZTU4Mi0yOTNmLTRhMTMtYmUwNS04MTBlN2E1Y2VlMjIMCxIMQW5zd2VyT3B0aW9uIiQwMzRjODg4Zi00MjdjLTQ2NjItOGNiNC05ZTczNDNkODgxOTAM'+'/'
#	idWebUser+'/'+token+'/'+idToken+'/'+idQuestion+'/'+safeWebAnswerOptionId)

#9.GET USER THAT ARE COMPATIBLE(POST)good
#r = requests.post(SERVER+'/_ah/api/userCandidateEndpoint/v1/userCandidateCollection/'+idUser+'/'+token+'/'+idToken)

#10.LIKE OR BLOCK A USER(PUT)not tested, wt is idUserCandidate and block?
#r = requests.put(SERVER+'/_ah/api/userCandidateEndpoint/v1/answers/'+idUser+'/'+idUserCandidate+'/'+token+'/'+idToken+'/'+block)

#11.LUPGRADE ACCOUNT(POST)error, i havnt acces :/
#r = requests.post(SERVER+'/_ah/api/userEndpoint/v1/user/upgradeVIP?clientId=ahBzfnBydWViYWRhdGVwbGF5cl0LEgRVc2VyIiRiMzFjMjc2Ny04NzNkLTRkZjktYmViOC0wZDJmNjU5ZWRjMGEMCxIFVG9rZW4iJDZkOWQ1MDZiLTY4YTctNDZkOC1iMzdlLWQ1NmZkZTkxNDdhYww&idWebUser=ahBzfnBydWViYWRhdGVwbGF5ci4LEgRVc2VyIiRiMzFjMjc2Ny04NzNkLTRkZjktYmViOC0wZDJmNjU5ZWRjMGEM&token=d269140a40fff421fbfb72c551e38d41&vipUpgrade=true')

#12.UPDATE BIO AND UNIVERSITY(PUT)error cannot parse parametro
#r = requests.put(SERVER+'/_ah/api/userEndpoint/v1/user/parametro/parametro/parametro?bio=Woman+in+her+early+twenties&university=Sabana/'+token+'/'+clientId+'/'+idWebUser)

#13.CHANGE PICTURES FROM GALLLERY(POST)not tested, i need know how to embed a file multipart wit python
#r = requests.post(SERVER+'https://pruebasdateplay.appspot.com/gcstorage'+token+'/'+clientId+'/'+idWebUser+'/'+photoId+'/'+privateImage+'/'+file)

#14.CHANGE PICTURES(PUT)not tested, i need do th 13 service first 
#r = requests.put(SERVER+'https://pruebadateplay.appspot.com/_ah/api/userEndpoint/v1/answers/'+token+'/'+clientId+'/'+idWebUser+'/'+idImage+'/'+linkToNewPicture)

#15.DELETE USER(DELETE)not tested, i love my user
#r = requests.delete(SERVER+'https://pruebadateplay.appspot.com/_ah/api/userEndpoint/v1/user/parametros'+idWebUser+'/'+token+'/'+clientId)

print(r.text)