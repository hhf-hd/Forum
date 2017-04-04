#!/usr/bin/python
#coding=utf-8

import re
import MySQLdb
from bs4 import BeautifulSoup

db = MySQLdb.connect("localhost","root","hhf150076","Forum",charset='utf8')
cursor = db.cursor()

html = """
<img class="authicn vm" id="authicon14010167" src="static/image/common/online_moderator2.gif" />
<em id="authorposton14010167">发表于 2017-3-15 11:00</em>
<span class="pipe">|</span>
<a href="http://f.bokett.com/forum.php?mod=viewthread&amp;tid=1449158&amp;page=1&amp;authorid=403043" rel="nofollow">只看该作者</a>
</div>
</div>
</div><div class="pct"><div class="pcb">
<div class="t_fsz">
<table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_14010167">
姓名 叶曦<br />
地区 杭州<br />
县市 杭州<br />
积分 1955<br />
电话 18606525125 <br />
姓名 程海<br />
地区 杭州<br />
县市 杭州<br />
积分 2025<br />
电话 15988163907<br />
</td></tr></table>
</div>
<div id="comment_14010167" class="cm">
</div>

<div id="post_rate_div_14010167"></div>
</div>
</div>
</div><div class="pct"><div class="pcb">
<div class="t_fsz">
<table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_14010169">
姓名：钟鸣拓<br />
地区：杭州<br />
县市：杭电<br />
积分：2050分<br />
电话：13957583033 <br />
姓名：黄鸿飞<br />
地区：杭州<br />
县市：江干<br />
积分：1900分首次参加担保人陈雯妍<br />
电话：15957108625 <br />
</td></tr></table>
</div>
<div id="comment_14010169" class="cm">
</div>

<div id="post_rate_div_14010169"></div>
</div>
</div>

</td></tr>
<tr><td class="plc plm">
"""

#soup = BeautifulSoup(html,"html.parser")
soup = BeautifulSoup(open("Contest1.html"),"html.parser")
tag = soup.find_all("td","t_f")
length = len(tag)
print length
for i in range(length):
	print
	#print tag[i].get_text()
	#print tag[i].name
	ll = len(tag[i].contents)
	if ll<5:
		continue
	print "length is ",ll
	Time = i+1
	print "Time is ",Time
	for j in range(ll-1):
		if j%2==0:	
			if(j/2)%5==0:
				Name = tag[i].contents[j].string
				Name = Name[4:12]
				print "Name is ",Name
			if(j/2)%5==1:
				City = tag[i].contents[j].string
				City = City[4:12]
				#print "City is ",City
			if(j/2)%5==2:
				Location = tag[i].contents[j].string
				Location = Location[4:12]
				#print "Location is ",Location
			if(j/2)%5==3:
				Score = tag[i].contents[j].string
				Memo = Score[9:30]
				Score = Score[4:8]
				print "Score is ",Score
				Score = int(Score)
				#print "Score is ",Score
			if(j/2)%5==4:
				Tel = tag[i].contents[j].string
				Tel = Tel[4:20]
				#print "Tel is ",Tel
		if (j-8)%10==0:

			print Name,City,Location,Score,Tel
			SQL = """insert into Data values('%d','%s','%s','%s','%d','%s','%s')"""%(Time,Name,City,Location,Score,Tel,Memo)
			try:
				cursor.execute(SQL)
				db.commit()
			except:
				db.rollback()
			
	


