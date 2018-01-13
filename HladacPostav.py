import requests, bs4, re
from time import time

"""poslední login: poslední login: 16. prosince 2015 23:17"""

"""Format must be kept in this way."""
logIn = '13.*ledna.*2018.*17:12'

found = False
patternTime = re.compile(logIn)
for x in range(0,280,20):
	
	a = time()
	
	if (x % 100 == 0):
		print("Finished checking ", x)
	with requests.Session() as s:
		res = s.get('https://www.andor.cz/jeskyne/index.php?from='+str(x)+'&page=13')
		# print the html returned or something more intelligent to see if it's a successful login page.
			
		andor = bs4.BeautifulSoup(res.text, "html.parser")
		tags = andor.findAll("span", class_="cHA")
	
		for tag in tags:
		
			
			cave = bs4.BeautifulSoup(s.get(tag.a.get('href')).text, "html.parser")
			cavePostavy = cave.find("div", class_ = "fellovInContent").findAll("span", class_ = "offlinePJ")
			cavePostavyFiltered = list(map(lambda x: x.find("span", class_ = "noDisplay").contents[0], cavePostavy))
		
			foundCharacter = False
			for postava in cavePostavyFiltered:
				parse = re.match(r'.*Postava (.*)je offline, naposledy online byla (.*)', postava)
				
				
				if (re.match(patternTime, parse.group(2))):
					if not foundCharacter:
						foundCharacter = True
						print("")
					
					print (parse.group(1))
				
			if foundCharacter:
				print("V dobrodruzstve: ", end=" ")
				print(tag.a.get('href'))
				
