# Visualization
Visualization of components and intents in android applications.

Used tools: COVERT, BeautifiulSoup, d3


Steps followed for the output:
• Create bundle in covert_dist.
• Place 22 apks in the bundle folder.
• Run sh./covert.sh bundle on the command
prompt.
• All the generated xml can be found in the
merged folder.
• Use each xml in the parsingcode.py to
generate corresponding json .
• Now run connections.py to get all the
connections between the components as a
single final json file.
• Use all the 22 JSON from first python
output and the final json which shows interactions in the html d3 visualization code(visualization.html- should only be run on chrome browser) to generate the visualization diagram.
3) Results of Observation:


For Parsing each XML file in parse.py write:
soup = BeautifulSoup(open(“Enter_xml_file_name_here.xml”), “xml") and
with open(“Enter_json_to_be_created_name.json”, "w") as json_file: json.dump(xml_file, json_file)
