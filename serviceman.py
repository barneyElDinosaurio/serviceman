import requests

#USER VARIABLES
emailAddress = 'marioalzatelopez@gmail.com'
gender = 'M'
birthday = '2016-09-24'
role = '1'
providerIdFacebook = 'mariolitop'
finalurl = 'marito.dateplay.com'
name = 'amarelio alzate'
lastName = 'amarelio'
firebaseId = 'fireMar'
#oUser = 
clientId = 'ahBzfnBydWViYWRhdGVwbGF5cl0LEgRVc2VyIiQyY2FmMWRhOS03NDY2LTRhNjMtYThmOS04YjlkN2VjZTk1NTIMCxIFVG9rZW4iJDFhMDA5ZTUzLTQ2NWEtNDA0MS1iZTBiLTYzZWQxOGIzZGIxZQw'
idUser = '2caf1da9-7466-4a63-a8f9-8b9d7ece9552' 
keyClient = 'NKuMGj3giNnq4jy9Dr8p593uNolu5dW9'
idWebUser = 'ahBzfnBydWViYWRhdGVwbGF5ci4LEgRVc2VyIiQyY2FmMWRhOS03NDY2LTRhNjMtYThmOS04YjlkN2VjZTk1NTIM'
token = 'c7ca1cc603d9ddeb135fdb08921ab45c'
tokenClient = 'c7ca1cc603d9ddeb135fdb08921ab45c'
tokenRefresh = '658b9e7c00af475d76652f526c1cff03'
idToken = 'ahBzfnBydWViYWRhdGVwbGF5cl0LEgRVc2VyIiQyY2FmMWRhOS03NDY2LTRhNjMtYThmOS04YjlkN2VjZTk1NTIMCxIFVG9rZW4iJDFhMDA5ZTUzLTQ2NWEtNDA0MS1iZTBiLTYzZWQxOGIzZGIxZQw'
#idUserCandidate = 
#block = 
#IMGS
idImage = '71949d59-f6ae-4c68-bc49-6c9a37ed9cde'
linkToNewPicture = 'http://supermariomaker.nintendo.com/assets/img/hero-mario.png'	
#photoId = 
#privateImage = 
#file = 

#QUESTION VARIABLES
#idQuestion = 
#safeWebAnswerOptionId = 

SERVER ='https://pruebadateplay.appspot.com'

#1.USER LOGIN AND CREATION(POST)
#r = requests.post(SERVER+'/_ah/api/userEndpoint/v1/storeUser/'+keyClient+'/'+emailAddress+'/'+gender+'/'+birthday+'/'+role+'/'+providerIdFacebook+'/'+finalurl+'/'+name+'/'+lastName+'/'+firebaseId'/'+latitude'/'+longitude'/'+university'/'+finalurl)

#2.(DEPRECATED)USER UPDATE(PUT)
#r = requests.put(SERVER+'/_ah/api/userEndpoint/v1/answers/'+oUser+'/'+tokenClient+'/'+idToken)

#3.USER GET(GET)good
#r = requests.get(SERVER+'/_ah/api/userEndpoint/v1/user/'+idWebUser+'/'+tokenClient+'/'+idToken)

#4.USER DELETE(DELETE)not tested
#r = requests.delete(SERVER+'/_ah/api/userEndpoint/v1/user/'+idWebUser+'/'+tokenClient+'/'+idToken)

#5.USER TOKEN SOFRESH(POST)good,but dont use so much because u need change ur variable tokenClient
#r = requests.post(SERVER+'/_ah/api/userEndpoint/v1/refreshToken/'+tokenRefresh+'/'+idToken+'/'+keyClient)

#6.NOTIFICATIONS UPDATE(PUT)good
#r = requests.put(SERVER+'/_ah/api/userEndpoint/v1/user/updateNotificationSettings?appSounds=false&appVibrations=false&clientId='+clientId+'&idWebUser='+idWebUser+'&matchNotifications=false&messageNotifications=false&token='+token)

#7.PREFERENCE UPDATE(PUT)good
#r = requests.put(SERVER+'/_ah/api/userEndpoint/v1/user/updateSearchPreferences?genderPreference=B&clientId='+clientId+'&idWebUser='+idWebUser+'&maximumAge=25&minimumAge=18&radioPreference=100&token='+token)

#8.STORE USER ANSWER(POST)not tested because i need the idQuestion
#r = requests.post(SERVER+'https://pruebasdateplay.appspot.com/_ah/api/userEndpoint/v1/storeUserAnswer/ahFzfnBydWViYXNkYXRlcGxheXIuCxIEVXNlciIkMjdiNzFiOTctNjVkNy00NDY2LTlhN2MtODQzYmMzNzIxNzc2DA/330c9bdc63a960c96d8d3ba967db7609/ahFzfnBydWViYXNkYXRlcGxheXJdCxIEVXNlciIkMjdiNzFiOTctNjVkNy00NDY2LTlhN2MtODQzYmMzNzIxNzc2DAsSBVRva2VuIiQ5N2M4MWUzMy04YjlkLTQ1YzYtODMzMy04NDhmNDcxZjgxMzMM/0383915a-38e2-4fa9-827f-5e765f3600b3/ahFzfnBydWViYXNkYXRlcGxheXKVAQsSCFF1ZXN0aW9uIiQwMzgzOTE1YS0zOGUyLTRmYTktODI3Zi01ZTc2NWYzNjAwYjMMCxIDUFZDIiRhMThmZTU4Mi0yOTNmLTRhMTMtYmUwNS04MTBlN2E1Y2VlMjIMCxIMQW5zd2VyT3B0aW9uIiQwMzRjODg4Zi00MjdjLTQ2NjItOGNiNC05ZTczNDNkODgxOTAM'+'/'
#	idWebUser+'/'+token+'/'+idToken+'/'+idQuestion+'/'+safeWebAnswerOptionId)

#9.GET USER THAT ARE COMPATIBLE(POST)good
#r = requests.post(SERVER+'/_ah/api/userCandidateEndpoint/v1/userCandidateCollection/'+idUser+'/'+token+'/'+idToken)

#10.LIKE OR BLOCK A USER(PUT)not tested,need idUserCandidate and ?block?
#r = requests.put(SERVER+'/_ah/api/userCandidateEndpoint/v1/answers/'+idUser+'/'+idUserCandidate+'/'+token+'/'+idToken+'/'+false)

#11.UPGRADE ACCOUNT(POST)good
#r = requests.post(SERVER+'/_ah/api/userEndpoint/v1/user/upgradeVIP?clientId='+clientId+'&idWebUser='+idWebUser+'&token='+token+'&vipUpgrade=true')

#12.UPDATE BIO AND UNIVERSITY(PUT)good
#r = requests.put(SERVER+'/_ah/api/userEndpoint/v1/user/'+token+'/'+clientId+'/'+idWebUser+'?bio=Woman+in+her+early+twenties&university=Sabana/')

#13.CHANGE PICTURES FROM GALLLERY(POST)not tested, i need know how to embed a file multipart with python
#r = requests.post(SERVER+'/gcstorage'+token+'/'+clientId+'/'+idWebUser+'/'+photoId+'/'+privateImage+'/'+file)

#14.CHANGE PICTURES(PUT)error, service temporaly unavaible 
r = requests.put(SERVER+'/_ah/api/userEndpoint/v1/answers/'+token+'/'+clientId+'/'+idWebUser+'/'+idImage+'/'+linkToNewPicture)

#15.DELETE USER(DELETE)not tested, i love my user
#r = requests.delete(SERVER+'/_ah/api/userEndpoint/v1/user/parametros'+idWebUser+'/'+token+'/'+clientId)

print(r.text)