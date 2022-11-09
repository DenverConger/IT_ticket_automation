# Overview

So There I was working in Classroom Technology, I was just assigned a project in which I needed to install over 120 cameras around campus for I.T to better troubleshoot broken classrooms remotely. I was having to Find the times each room was open and also find the best order to go to those rooms. You cannot just go from one room to another because of differeing classtimes.
And than I asked myself the question every Programmer has asked once before. "There has to be a better way"

It started with BYUI's EMS website. This is their scheduling software that everyone has access to. We often use it in I.T to see when the rooms are or are not open. I decided to inspect the html that the page was made of and came to the ralization that I could web scrape the page! I could extract the times each rooms were open and maybe build an algorithm that could tell me the best times and order to go to classrooms. 

I ran into another probllem though. How would I find the best order? Am i doomed to individually place markers over google maps and label each one on the location of the room so I could later build a vector space of it? no. I decided to spend twice as long as that web scraping that data too! It wasnt nearly as simple though. I found out you couldnt simpoly scrape the data of the BYUI interactive map because it was a javascript app. So I diud some digging and discovered that the School provides a free ArcGIS pro account and the employee who built the interactive map and regularly updates it posts the information on the BYUI arcgis page! Score! Well not quite... It did not have any of the physical locations and was merely ovwerlayed onto the map. each room at least. Luckily with a bit of algorithmic compolexity provided by ARCGis you could directly add a long and lat component to your dataset with an approximation. ArcGIS really is a powerful tool!

I have provided my code for webscraping the EMS page which was not very easy and I needed to emu;late a chrome browser to get the proper data.

I would have combined these two datasets into a master dataset with both an updatable open class times and location but I am not certain yet how I want to implement that since part of this Data Frame would need the capability of being regularly updated.

I also will be building an algorithm that can compute the best time and order to go to multiple rooms on its own. Taking into account which floor it is on, whether it is a class break or not and the best way to get to all of them in one fell swoop if possible!

[Software Demo Video](http://youtube.link.goes.here)

# Development Environment

ArcGIS

Python:
    selenium
    Regex (for the win!)
R

# Useful Websites


* [BYUI EMS](https://ems.byui.edu/emswebclient/Login.aspx)
* [BYUI interactive map](https://maps.byui.edu/interactive-map/)

# Future Work

* Find a proper way to consistently update the data to represent the current week of class times and other scheduling tasks
* Present and polish my algorithm for computing the best path and order for room tickets (its a secret for now until I can give it a proper presentation)