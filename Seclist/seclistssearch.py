import urllib2

baseLink = "http://seclists.org/fulldisclosure/"

class Entry:
    def __init__(self,title,ID,date,year,month):
        self.title = title
        self.ID = ID
        self.date = date
        self.keywords = []
        self.exclude = False
        self.year = year
        self.month = month

    def prettyPrint(self):
        key = ""
        for keyword in self.keywords:
            key = key + keyword + ", "
        key = key[:len(key)-2:] #Remove comma and space for final entry
        print(self.title + "\t" + self.date + "\t" + baseLink + self.year + "/" + self.month + "/" + self.ID + "\t" + key)

def generateEntries(website,year,month):
    currentId = "-1"

    lines = []
    Entires = []

    for entry in website:
        l = ""
        for char in entry:
            if char in '\n':
                lines.append(l)
                l = ""
            else:
                l = l + char
        lines.append(l)

    for line in lines:
        if "name=" in line and "href=" in line:
            currentIdStart = line.find("\"",0,len(line))
            currentIdEnd = line.find("\"",currentIdStart+1,len(line))
            currentId = line[currentIdStart+1:currentIdEnd:] #We found ID

            titleStart = line.find("\">",0,len(line)) + 2
            titleEnd = line.find("<",titleStart+1,len(line))
            title = line[titleStart:titleEnd:] #We found title

            dateStart = line.find("<em>",0,len(line)) + len("<em>")
            dateStart = line.find("(",dateStart+1,len(line)) + 1
            dateEnd = line.find(")",dateStart+1,len(line))

            date = line[dateStart:dateEnd:]

            Entries.append(Entry(title.replace('\t',' '),currentId,date,year,month))

    return Entries

def filterEntries(entries, filterList, exclusionList):
    firstList = []
    for entry in entries:
        for keyword in exclusionList:
            if(keyword.lower() in entry.title.lower()):
                entry.exclude = True
    
    for entry in entries:
        if entry.exclude is not True:
            firstList.append(entry)

    for entry in firstList:
        for keyword in filterList:
            if keyword.lower() in entry.title.lower():
                entry.keywords.append(keyword)

    finalList = []
    cisco = "cisco"
    for entry in firstList:
        if len(entry.keywords) > 0:
            if cisco.lower() in entry.keywords[0].lower() and len(entry.keywords) > 1:
                finalList.append(entry)
            elif cisco.lower() not in entry.keywords[0].lower():
                finalList.append(entry)

    return finalList

monthList = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
yearList = ["2018","2017","2016","2015","2014","2013","2012","2011","2010"]

filterList = ["Cisco","Dlink","D-link","Asus","Parrot","Zyxel","Huawei","Wind turbine","Xzeres","BMW",
"Smart", "home","IoT","Veichle","Ewon","ZTE","Callisto","Realtek","hikvision","siemens","Samsung",
"prolink","axis","seagate","western digital","zhone","scada","totolink","sterlight","linksys","Dell",
"netgear","canon","geovision","vivotek","cam","router","Samsumg","drone","tp link","printer","Sierra","ELNET","Power Meter","Siklu","MoveIt","Ubiquiti"]

exclusionList = ["Re:","ADSL","homepage","vpn",".exe","camp","firefox","internet explorer","audiotran","scam","Insect Pro","NetRipper"]

Entries = []



for year in yearList:
    for month in monthList:
        if year is "2018" and month is "Mar":
            break
        r = urllib2.urlopen(baseLink+year+"/"+month)

        response = ""
        webs = []
        while 1:
            data = r.read()
            if not data:
                break
            webs.append(data)

        website = response
        Entries = generateEntries(webs,year,month)

Entries = filterEntries(Entries,filterList,exclusionList)


for entry in Entries:
    entry.prettyPrint()



