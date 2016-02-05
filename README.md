Command line:  
 
    docker run -v (path_to_your_xml_directory)/xml:/xml aaiache/python-xml ./check.sh xml/annuaire  

You should obviously replace (path_to_your_xml_directory) by the path to the directory that contains the XML and XSD files (which must have the same name and .xml, .xsd extensions respectively).  
docker build -t xml_python .

#Validate an XML file using a machine supporting Docker  
###Objective:  
The project's aim is to create a simple program to validate an XML file against a XSD file.  
So, the objective is to create a docker image customized, from which we can create a container to validate a XML file.  
To do so, we can just use the **xmllint** program which we can install on a debian destribution.  
I chose to do it using a Python API called: **etree** from the toolkit **lxml**.
###Get the image:  
	docker pull aaiache/xml_python 
###Command line:
	docker run -v (path_to_your_xml_directory)/xml:/xml aaiache/xml_python ./check.sh xml/annuaire 
###Image Components
1. The base image is python:latest
2. In order to use **lxml** we shoud install it
3. A python script which allows to validate a XML file against a XSD file.  


###Do you want to try it?
**Download the image from my docker hub repository:**   

    docker pull aaiache/xml_python  
![alt text](https://github.com/AAiache/XML_Python_Docker/blob/master/screen_shots/Screen_Shot1.png)  
**Clone the project's repository from GitHub:**  

    git clone https://github.com/AAiache/XML_Docker.git  
    
**Run:**  

    docker run -v (path_to_your_xml_directory)/xml:/xml aaiache/xml_python ./check.sh xml/annuaire  

![alt text](https://github.com/AAiache/XML_Python_Docker/blob/master/screen_shots/Screen_Shot2.png)

