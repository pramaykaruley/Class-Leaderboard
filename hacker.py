import json
from urllib.request import urlopen

from pprint import pprint as pp

def getdata(username):
	html = urlopen("https://www.hackerrank.com/{}?hr_r=1".format(username)).read().decode('utf-8')

	html2 = html
	scriptopen = '<script type="application/json" id="initialData">'
	startindex = html.index(scriptopen)

	html = html[startindex + len(scriptopen):]
	endindex = html.index('</script>')
	html = html[:endindex]

	data = json.loads(html)
	
	data = data['community']
	data = data['viewProfile']
	data = data['scores']
	#pp(data.keys())
	algorithms = data['algorithms']
	algorithms = algorithms['contest']
	#print(algorithms)



	return algorithms


# d = getdata('pramaykaruley')

#print(medals)
usernames = ['pramaykaruley','parthlathiya','abhilash29']

strng = ""
for i in usernames:
	d = getdata(i)
	comp = d['competitions']
	medals = d['medals']
	
	strng = strng + """<tr>
				<td>"""+i+"""</td>
				
				<td>"""+str(d['score'])+""" </td>
				<td>"""+str(d['rank'])+""" </td>
				<td>"""+str(d['percentile'])+""" </td>
				<td>"""+str(comp)+"""</td>
				<td>"""+str(medals['gold'])+""" </td>
				<td>"""+str(medals['silver'])+""" </td>
				<td>"""+str(medals['bronze'])+""" </td>
				<tr>"""
#print(strng)

string = """<!DOCTYPE html>
<!-- Template by quackit.com -->
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<title>Class Leaderboard</title>
		<style type="text/css">
		
			body {
				margin:0;
				padding:0;
				font-family: Sans-Serif;
				line-height: 1.5em;
			}
			
			#header {
				background: #ccc;
				height: 100px;
			}
			
			#header h1 {
				margin: 0;
				padding-top: 40px;
			}
			
			main {
				padding-bottom: 10010px;
				margin-bottom: -10000px;
				float: left;
				width: 100%;
			}
			
			#nav {
				padding-bottom: 10010px;
				margin-bottom: -10000px;
				float: left;
				width: 230px;
				margin-left: -100%;
				background: #eee;
			}
			
			#footer {
				clear: left;
				width: 100%;
				background: #ccc;
				text-align: center;
				padding: 4px 0;
			}
	
			#wrapper {
				overflow: hidden;
			}
						
			#content {
				margin-left: 230px; /* Same as 'nav' width */
			}
			
			.innertube {
				margin: 15px; /* Padding for content */
				margin-top: 0;
			}
		
			p {
				color: #555;
			}

			table {
			    border-collapse: collapse;
			    width: 100%;
			}

			th, td {
			    text-align: left;
			    padding: 8px;
			}

			tr:nth-child(even){background-color: #f2f2f2}

			th {
			    background-color: #4CAF50;
			    color: white;
			}
			nav ul {
				list-style-type: none;
				margin: 0;
				padding: 0;
			}
			
			nav ul a {
				color: darkgreen;
				text-decoration: none;
			}
		
		</style>
		
		
	
	</head>
	
	<body>		

		<header id="header">
			<div class="innertube">
				<center><h1><font color = 'Green'>Class Leaderboard for HackerRank</font></h1></center>
			</div>
		</header>
		
		<div id="wrapper">
		
			<main>
				<div>
				<table border = '1'>					
				
				<tr>
				<th rowsapn ='2'>Name</th>
				
				<th rowsapn ='2'>Score</th>
				<th rowsapn ='2'>Rank</th>
				<th rowsapn ='2'>Percentile</th>
				<th rowsapn ='2'>Competitions</th>
				
				<th> <img src = 'gold_big.png' width = '30'></th>
				<th> <img src = 'silver_big.png' width = '30'></th>
				<th> <img src = 'bronze_big.png' width = '30'></th>
				
				<tr>"""+(strng)+"""
				
				</table>


			</div>
			</main>
			
					
		</div>
		
		<footer id="footer">
			<div class="innertube">
				<p>&copy;Pramay Karule, Mtech1, CSE</p>
			</div>
		</footer>
	
	</body>
</html>"""

print(string)
