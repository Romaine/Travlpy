import argparse, urllib, time, json
import xml.dom.minidom as xDom

def printer2(args):
        #road = raw_input("Choose a bus stop: ")
        api = urllib.urlopen("http://countdown.api.tfl.gov.uk/interfaces/ura/instant_V1?stoppointname=" + args,road)
        print "\n"

        sysTime = api.readline()
        sysTime = json.loads(sysTime)
        sysTime = sysTime[2]
        
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

parser = argparse.ArgumentParser(description='An argparse test script')

parser.add_argument("-n", "--name", dest="action", action='store_const', const=printer2, help='Print bus timetable for given bus')

args = parser.parse_args()

args.action(args)

def printer():
        i = 3
        road = raw_input("Choose a bus stop: ")
        api = urllib.urlopen("http://countdown.api.tfl.gov.uk/interfaces/ura/instant_V1?stoppointname=" + road)
        print "\n"

        sysTime = api.readline()
        sysTime = json.loads(sysTime)
        sysTime = sysTime[2]
        
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
                display = str(bus) + str(eta).rjust(len(eta) - len(bus) + 8)
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


def lineTimes():
        bakerloo = {'Jubilee': 'J', 'Bakerloo': 'B', 'Central': 'C', 'District': 'D', 'Metropolitan': 'M', 'Waterloo & Cit': 'W', 'Piccadilly': 'P', 'Victoria': 'V', 'Northern': 'N', 'Hammersmith & Circle': 'H'}
        central = {'Marylebone': 'MYB', 'Stonebridge Park': 'SPK', 'Charing Cross': 'CHX', "Queen's Park": 'QPK', 'Warwick Avenue': 'WAR', 'Willesden Junction': 'WJN', 'Waterloo': 'WLO', 'Kilburn Park': 'KPK', 'Oxford Circus': 'OXC', 'Kenton': 'KNT', 'Paddington': 'PAD', 'North Wembley': 'NWM', 'Kensal Green': 'KGN', 'Harlesden': 'HSD', 'Baker Street': 'BST', 'Edgware Road': 'ERB', 'Piccadilly Circus': 'PIC', 'Maida Vale': 'MDV', 'Elephant and Castle': 'ELE', 'Wembley Central': 'WEM', 'Embankment': 'EMB', "Regent's Park": 'RPK', 'South Kenton': 'SKT', 'Harrow and Wealdstone': 'HAW', 'Lambeth North': 'LAM'}
        district = {'Redbridge': 'RED', 'Bond Street': 'BDS', 'South Ruislip': 'SRP', 'Leyton': 'LEY', 'Leytonstone': 'LYS', 'Ealing Broadway': 'EBY', 'Holland Park': 'HPK', 'Holborn': 'HOL', 'St Paul\x92s': 'STP', 'Newbury Park': 'NEP', 'Roding Valley': 'ROD', 'Lancaster Gate': 'LAN', 'Chancery Lane': 'CYL', 'Oxford Circus': 'OXC', 'Fairlop': 'FLP', 'Gants Hill': 'GHL', 'Buckhurst Hill': 'BHL', 'Queensway': 'QWY', 'Loughton': 'LTN', 'Theydon Bois': 'THB', 'Snaresbrook': 'SNB', 'Tottenham Court RoaWAN Wanstead': 'TCR', 'Stratford': 'SFD', 'East Acton': 'EAC', 'South Woodford': 'SWF', 'Mile End': 'MLE', 'Bank': 'BNK', 'Notting Hill Gate': 'NHG', 'North Acton': 'NAC', 'Bethnal Green': 'BNG', 'West Ruislip': 'WRP', 'Shepherd\x92s Bush': 'SBC', 'Hanger Lane': 'HLN', 'West Acton': 'WAC', 'Chigwell': 'CHG', 'Ruislip Gardens': 'RUG', 'Barkingside': 'BDE', 'Debden': 'DEB', 'Liverpool Street': 'LST', 'Northolt': 'NHT', 'Woodfor': 'WFD', 'Grange Hill': 'GRH', 'Greenford': 'GFD', 'Epping': 'EPP', 'Marble Arch': 'MAR', 'White City': 'WCT', 'Perivale': 'PER', 'Hainault': 'HAI'}
        hammersmithAndCircle = {'Upminster Bridge': 'UPB', 'Stepney Green': 'STG', 'Southfields': 'SFS', 'Wimbledon Par': 'WMP', 'Embankment': 'EMB', 'Wimbledon': 'WDN', 'High Street Kensington': 'HST', 'Elm Park': 'EPK', 'East Ham': 'EHM', 'Edgware Road (H & C)': 'ERD', 'Ealing Broadway': 'EBY', 'Plaistow': 'PLW', 'Turnham Green': 'TGR', 'South Kensington': 'SKN', 'Victoria': 'VIC', 'Bromley-by-Bow': 'BBB', 'Barons Court': 'BCT', 'Chiswick Park': 'CHP', 'Mansion House': 'MAN', 'Aldgate East': 'ALE', 'Putney Bridge': 'PUT', 'East Putney': 'EPY', 'Temple': 'TEM', 'Fulham Broadway': 'FBY', "St. James's Park": 'SJP', 'West Kensington': 'WKN', 'West Brompton': 'WBT', 'Upney': 'UPY', 'Gunnersbury': 'GUN', 'Mile End': 'MLE', 'Blackfriars': 'BLF', 'Westminster': 'WMS', 'Upminster': 'UPM', 'Sloane Square': 'SSQ', 'West Ham': 'WHM', 'Whitechapel': 'WCL', 'Becontree': 'BEC', 'Kensington (Olympia)': 'OLY', 'Upton Park': 'UPK', 'Bow Road': 'BWR', 'Monument': 'MON', 'Dagenham East': 'DGE', 'Hammersmith(District and Piccadilly)': 'HMD', 'Ealing Common': 'ECM', 'Gloucester Road': 'GRD', 'Cannon Street': 'CST', 'Olympia': 'OLY', 'Richmond': 'RMD', 'Acton Town': 'ACT', 'Barking': 'BKG', 'Ravenscourt Park': 'RCP', 'Stamford Brook': 'STB', 'Dagenham Heathway': 'DGH', 'Parsons Green': 'PGR', 'Tower Hill': 'THL', 'Earl\x92s Court': 'ECT', 'Kew Gardens': 'KEW'}
        jubilee = {'Stepney Green': 'STG', 'Embankment': 'EMB', 'Farringdon': 'FAR', 'Moorgate': 'MGT', 'Edgware Road (H & C)': 'ERD', 'Westminster': 'WMS', 'Plaistow': 'PLW', 'Euston Square': 'ESQ', 'South Kensington': 'SKN', 'Victoria': 'VIC', 'Great Portland Street': 'GPS', 'Whitechape': 'WCL', 'Aldgate': 'ALD', 'Mansion House': 'MAN', 'Aldgate East': 'ALE', 'Bromley-by-Bow': 'BBB', 'Paddington': 'PAD', 'East Ham': 'EHM', "St. James's Park": 'SJP', 'High Street Kensington': 'HST', 'Mile End': 'MLE', 'Hammersmith': 'HMS', 'Blackfriars': 'BLF', 'Baker Street': 'BST', 'Sloane Square': 'SSQ', 'West Ham': 'WHM', "King's Cross St Pancras": 'KXX', 'Temple': 'TEM', 'Bow Road': 'BWR', 'Monument': 'MON', 'Gloucester Road': 'GRD', 'Cannon Street': 'CST', 'Liverpool Street': 'LST', 'Barking': 'BKG', 'Tower Hill': 'THL', 'Upton Park': 'UPK', 'Barbican': 'BAR'}
        metroPolitan = {'Southwark': 'SWK', 'Canada Water': 'CWR', 'North Greenwich': 'NGW', 'Westminster': 'WMS', 'Bermondsey': 'BER', 'Green Park': 'GPK', 'West Hampstead': 'WHD', 'Queensbury': 'QBY', 'Willesden Green': 'WLG', 'Bond Street': 'BDS', 'Canary Wharf': 'CWF', 'Stanmore': 'STA', 'Kilburn': 'KIL', 'Neasden': 'NEA', 'Finchley Road': 'FRD', 'Baker Street': 'BST', 'Waterloo': 'WLO', 'West Ham': 'WHM', 'London Bridge': 'LON', 'Canning Town': 'CNT', 'Canons Park': 'CPK', 'Dollis Hill': 'DHL', 'Swiss Cottage': 'SWC', 'St John\x92s Wood': 'SJW', 'Stratford': 'SFD', 'Kingsbury': 'KBY', 'Wembley Park': 'WPK'}
        northern = {'Farringdon': 'FAR', 'Ickenham': 'ICK', 'Moorgate': 'MGT', 'Croxley': 'CRX', 'Euston Square': 'ESQ', 'Northwood': 'NWD', 'Great Portland Street': 'GPS', 'Aldgate': 'ALD', 'Pinner': 'PIN', 'Northwick Park': 'NWP', 'North Harrow': 'NHR', 'Ruislip': 'RUI', 'Chalfont and Latimer': 'CLF', "King's Cross St Pancras": 'KXX', 'Rayners Lane': 'RLN', 'Finchley Road': 'FRD', 'Chorleywood': 'CWD', 'Colliers Wood': 'CLW', 'Baker Street': 'BST', 'Northwood Hills': 'NWH', 'Eastcote': 'ETE', 'Moor Park': 'MPK', 'West Harro': 'WHR', 'Barbican': 'BAR', 'Hillingdon': 'HDN', 'Amersham': 'AME', 'Liverpool Street': 'LST', 'Rickmansworth': 'RKY', 'Watford': 'WAT', 'Ruislip Manor': 'RUM', 'Uxbridge': 'UXB', 'Harrow on the Hill': 'HOH', 'Wembley Park': 'WPK'}
        piccadilly = {'Woodside Par': 'WSP', 'Hendon Central': 'HND', 'Colliers Wood': 'CLW', 'Clapham South': 'CPS', 'Kennington': 'KEN', 'Moorgate': 'MGT', 'Warren Street': 'WST', 'Mill Hill East': 'MHE', 'Camden Town': 'CTN', 'Charing Cross': 'CHX', 'Totteridge and Whetstone': 'TOT', 'Tooting Broadway': 'TBY', 'Highgate': 'HIG', 'Burnt Oak': 'BUR', 'Morden': 'MOR', 'Hampstead': 'HMP', 'Clapham North': 'CPN', 'Colindale': 'COL', 'Balham': 'BAL', 'Stockwell': 'STK', 'Old Street': 'OLD', 'Mornington Crescent': 'MCR', 'Edgware': 'EDG', 'Bank': 'BNK', 'Brent Cross': 'BTX', 'Chalk Farm': 'CHF', 'Waterloo': 'WLO', "King's Cross St Pancras": 'KXX', 'Archway': 'ARC', 'South Wimbledon': 'SWM', 'East Finchley': 'EFY', 'Tufnell Park': 'TPK', 'Elephant and Castle': 'ELE', 'West Finchley': 'WFY', 'Embankment': 'EMB', 'High Barnet': 'HBT', 'Clapham Common': 'CPC', 'Tooting Bec': 'TBE', 'Kentish Town': 'KTN', 'Angel': 'ANG', 'Golders Green': 'GGR', 'Finchley Central': 'FYC', 'Leicester Square': 'LSQ', 'Belsize Park': 'BPK', 'London Bridge': 'LON', 'Oval': 'OVL', 'Goodge Street': 'GST', 'Euston': 'EUS', 'Borough': 'BOR', 'Tottenham Court Road': 'TCR'}
        victoria = {'Sudbury Town': 'STN', 'Ickenham': 'ICK', 'Oakwood': 'OAK', 'Bounds Green': 'BGR', 'South Kensington': 'SKN', 'Hammersmith (District and Piccadilly)': 'HMD', 'South Harrow': 'SHR', 'Holborn': 'HOL', 'Heathrow Terminal 5': 'HRV', 'Green Park': 'GPK', 'Hyde Park Corner': 'HPC', 'Hounslow West': 'HNW', 'Wood Gree': 'WGN', 'Barons Court': 'BCT', 'Covent Garden': 'COV', 'Earl\x92s Court': 'ECT', 'North Ealing': 'NEL', 'Turnpike Lane': 'TPL', 'Arnos Grove': 'AGR', 'Finsbury Park': 'FPK', 'Hatton Cross': 'HTX', 'Park Royal': 'PRY', 'Manor House': 'MNR', 'Alperton': 'ALP', 'Hounslow East': 'HNE', "King's Cross St Pancras": 'KXX', 'Rayners Lane': 'RLN', 'Caledonian Road': 'CRD', 'Ruislip': 'RUI', 'Piccadilly Circus': 'PIC', 'Eastcote': 'ETE', 'Cockfosters': 'CFS', 'Hillingdon': 'HDN', 'Sudbury Hill': 'SHL', 'Hounslow Central': 'HNC', 'Southgate': 'SGT', 'Ealing Common': 'ECM', 'Osterley': 'OST', 'Gloucester Road': 'GRD', 'Northfields': 'NFD', 'Acton Town': 'ACT', 'Turnham Green': 'TGR', 'Heathrow Terminals 123': 'HRC', 'Arsenal': 'ARL', 'Leicester Square': 'LSQ', 'Holloway Road': 'HRD', 'Russell Square': 'RSQ', 'Ruislip Manor': 'RUM', 'Uxbridge': 'UXB', 'Knightsbridge': 'KNB', 'South Ealing': 'SEL', 'Boston Manor': 'BOS', 'Heathrow Terminal 4': 'HTF'}
        waterlooAndCity = {'Waterlo': 'WLO', 'Bank': 'BNK'}
        
def getLineCodes():
        f = open("linecodes.txt")
        codes = {}
        for lcodes in f:
                codes[lcodes[4:-1]] = lcodes[0:3]

        print codes
                

        


#parser.add_argument('-p','--parse', dest='ptext', action='store_const',
#                    const=printer,
#                    help='print epochs')

#parser.add_argument('-l','--lines', dest='line', action='store_const',
#                    const=linesStatus,
#                    help='print line statuses')


#parser.parse_args()
#args.pline()#
#print args.accumulate(args.integers)
##if options.verbose:
##
##        print "Mode is set to verbose!"
##
##
##print options.write
##
##print args[0]
##
##print args[1]


