#Acceptance criteria

#ask the user to choose which website they want to store
def Createmonitor():
    name = input("What would you like to name your new monitor \n")
    url = input("What is the linkanitakuy of the new monitor \n")
    record = [name, url]
    return record
#get the variables name and website

#name = 'anitaku'
#url = 'https://anitaku.to/home.html'
#record = [name, url]

print(Createmonitor())
#check if the website is ok and for any redirects so i wont need to constantly upload url
#use webscaper to grab the entire html of the page to store locally
#once the page receives new content
#code needs to subtract the new content from the old to get the differnece
#the difference should contain the names of any new content as well as the episode number and date released

#later implementation

#to automate instead of doing one for the development I should just be able to manage and create new requests able to adjust the checking frequency and website
#hopefully have this work universally between webpages

#hopes
#for actual use the option of having this as an android app working in the background
