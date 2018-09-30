# Knight-The-Crawler
Custom web crawler with GUI and Hyperthreading

<img src="Knight%20the%20webcrawler/icon/logo.png" align= "middle">

Knight-The-Crawler is a web crawler which crawl a given link and extract all the enternal and external links that a website contains.


It generate two file Queue.txt and crawled.txt 
Queue.txt contains all the links that are in a queue waiting for their turn.
Crawled.txt conatins all th elinks that are crawled by the Knight.
 
Crawler contain following files all coded in python

# common.py
This file handles the Read/Write operation to files and also creation of the files/folders.

# domain.py
This file handles the domain and sub domain extraction from url.

# knight.py
This file contains the class Knight and all the related function.

# main.py
This file handles threading and initialization of the the crawler

# MainApp.py
This is the main file of the crawler run this file to start Knight.
Gui of the Knight use PYQT.

# seeker.py
This file add links to the txt files 



You will required Python3 with Pyqt5 module to run the Knight else it will give error



Preview of the GUI is here:

<img src="Knight%20the%20webcrawler/icon/preview.jpg" align= "middle" height="800" width="600">
