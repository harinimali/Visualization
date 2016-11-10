import json
from bs4 import BeautifulSoup
senderreceiver=[]
per=[]
files = ['Battery HD.json','GoogleCalendar.json','StudentAgenda.json','A1_notes.json','Equalizer&Bass.json','A2_camera.json','DoNotCrash.json','QuickMemo.json','A1_maps.json','Chrome.json','Navigator.json','IslamicPrayer.json','BatterySaver.json','Waze.json','A2_piceditor.json','CameraforAndroid.json','DiabetesConnect.json','EasyScreenshot.json','InkPad.json','MapDirections.json']
xmlfiles = ['Battery HD.xml','GoogleCalendar.xml','StudentAgenda.xml','A1_notes.xml','Equalizer&Bass.xml','A2_camera.xml','DoNotCrash.xml','QuickMemo.xml','A1_maps.xml','Chrome.xml','Navigator.xml','IslamicPrayer.xml','BatterySaver.xml','Waze.xml','A2_piceditor.xml','CameraforAndroid.xml','DiabetesConnect.xml','EasyScreenshot.xml','InkPad.xml','MapDirections.xml']

for f in range(len(files)):
	for k in range(f+1,4,1):
		app1 = json.loads(open(files[f]).read())
		app2 = json.loads(open(files[k]).read())
		act=[]
		intents=[]
		flag1 = False
	

		for i in range(len(app1["Intents"])):
			intents.append(app1["Intents"][i])
			x=intents[i]
			if(x):
				intents[i]=x.replace("\"","")
				for j in range(len(app2["Actions"])):
					act.append(app2["Actions"][j])
					if(intents[i] == act[j]):
						flag1=True
						senderreceiver.append([app1["sender"][i],app2["ComponentName"][j]])
				

	
for p in range(len(xmlfiles)):
	soup = BeautifulSoup(open(xmlfiles[p]),"xml")
	name = soup.application.apkFile.next_sibling.next_sibling.contents[0]
	for ele in soup.application.find_all('permission'):
		per.append([name,ele.string])
        
data={
'InteractingComponents':senderreceiver,
'Permissions':per
}
json_str = json.dumps(data)
f= open('connections.json',"w")
f.write(json_str) 

f.close()