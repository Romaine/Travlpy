import argparse, time, json
import xml.dom.minidom as xDom
import urllib2 as net

print 'test'

class Bus():
    "Interface for TFL bus response"

    responseurl = "http://countdown.api.tfl.gov.uk/interfaces/ura/instant_V1?"

    def eta(self, args):
            
        req = net.Request(self.responseurl, "stoppointname=" + args)

        print "got past Request"

        response = net.urlopen(req)
        #print response.read()

        

        sysTime = response.readline()
        sysTime = json.loads(sysTime)
        sysTime = sysTime[2]
        lines = response.readlines()

        data = []

        for raw in lines:
            raw = json.loads(raw)
            print raw

        print
        
        
        ## Schema idea

        
        timetable = [{"epoch" : {"route" : 0, "stop" : '',}}]

        ## Schema attempt

        for line in lines:
            line = json.loads(line)
            data.append({ line[3] : {"route" : line[2], "stop" : line[1] }})
            


        for line in lines:



            line = json.loads(line)
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
            #print display

        print data
        #print net.HTTPError.read()

                    


    def busTimes():
            response = net.urlopen("http://countdown.api.tfl.gov.uk/interfaces/ura/instant_V1?stoppointname=barking road").read()
            
            for line in response:
                    print bus

    def lineStatus():
            response = net.urlopen("http://cloud.tfl.gov.uk/TrackerNet/LineStatus").read()
            xData = xDom.parseString(response)
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
                

