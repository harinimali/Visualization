import json
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("GoogleCalendar.xml"), "xml")

name = soup.application.apkFile.next_sibling.next_sibling.contents[0]
    

app_permission = []
for children in soup.application.find_all('permission'):
    app_permission.append(children.string)
    
comp_name = []                                                       
for subchild in soup.application.components.find_all('name'):
    comp_name.append(subchild.string)
    
comp_actions = []
for subchild4 in soup.application.components.find_all('actions'):
    comp_actions.append(subchild4.string)
    
intents = []
for child in soup.newIntents.find_all('action'):
    intents.append(child.string)
    
sender = []
for subchild1 in soup.newIntents.find_all('sender'):
    intents.append(subchild1.string)


xml_file = {"ApplicationName":name,
            "ComponentName":comp_name, 
            "Permission":app_permission,
            "Actions":comp_actions,
            "Intents":intents,
            "Sender":sender}
with open("GoogleCalendar.json", "w") as json_file:
    json.dump(xml_file, json_file)
            
            
    
   



