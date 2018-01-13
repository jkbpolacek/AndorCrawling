import requests, bs4, re
from time import time
from itertools import permutations

"""poslední login: poslední login: 16. prosince 2015 23:17"""

"""Format must be kept in this way."""
logIn = '13.*ledna.*2018.*17:12'

found = False
patternB = re.compile(logIn)
pattern = re.compile('\d\d\..+?\d\d\d\d.*?\d*:\d\d')
for x in range(0,19950,50):
	
	a = time()
	
	if (x % 1000 == 0):
		print("Finished checking ", x)
	with requests.Session() as s:
		res = s.get('http://www.andor.cz/user/index.php?action=viewUsers&from='+str(x)+'&page=400')
		# print the html returned or something more intelligent to see if it's a successful login page.
			
		andor = bs4.BeautifulSoup(res.text, "html.parser")
		tags = andor.findAll("div", class_ = "onePj" )
		
		for tag in tags:
			
			
			match = pattern.search(str(tag))				
			if match:
				if patternB.search(str(match.group(0))):
					print("Found something")
					found = True
					tagsB = tag('a')
					print(tagsB)
					retag = str(tag.get('href', None))
					print(retag)
