import argparse, urllib, time, json
import xml.dom.minidom as xDom

print 'test'

class Bus():
    apiurl = "http://countdown.api.tfl.gov.uk/interfaces/ura/instant_V1?stoppointname="

    def eta(self, args):
            
        api = urllib.urlopen(self.apiurl + args)
        print "\n"

        sysTime = api.readline()
        print sysTime
        sysTime = json.loads(sysTime)
        sysTime = sysTime[2]
        print sysTime 
        lines = api.readlines()
        for line in lines:
                line = json.loads(line)
                #print line
                bus = line[2]
                busTime = line[3]
                eta = busTime - sysTime
                eta = eta / 1000
                eta = eta / 60
                    
                if eta == 0:
                    eta = "Due"
                        
                bus = str(bus)
                eta = str(eta)
                display = bus + eta.rjust(len(eta) - len(bus) + 8)
                print display
                    


    def busTimes():
            api = urllib.urlopen("http://countdown.api.tfl.gov.uk/interfaces/ura/instant_V1?stoppointname=barking road").read()
            
            for line in api:
                    print bus

    def lineStatus():
            api = urllib.urlopen("http://cloud.tfl.gov.uk/TrackerNet/LineStatus").read()
            xData = xDom.parseString(api)
            arrayOfLineStatus = xData.getElementsByTagName("ArrayOfLineStatus")[0]
            lineStatus = arrayOfLineStatus.getElementsByTagName("LineStatus")
            gs = 0
            pc = 0
            cs = 0
            for lineInfo in lineStatus:
                    lines = lineInfo.getElementsByTagName("Line")[0].attributes["Name"].value
                    service = lineInfo.getElementsByTagName("Status")[0].attributes["Description"].value
                    if service == "Good Service":
                            gs += 1
                    if service == "Part Closure":
                            pc += 1
                    if service == "Planned Closure":
                            cs += 1
                    print lines + service.rjust(len(service) - len(lines) + 6*4)
            print "\nThere are %d Good Services, %d Part Closures and %d Planned Closures" % (gs,pc,cs)


    def getLineCodes():
            f = open("linecodes.txt")
            codes = {}
            for lcodes in f:
                codes[lcodes[4:-1]] = lcodes[0:3]

                print codes

bus = Bus()

bus.eta("Suffolk Road")
                

