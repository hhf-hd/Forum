#!/usr/bin/python
#coding=utf-8

import re
import MySQLdb
from bs4 import BeautifulSoup

db = MySQLdb.connect("localhost","root","hhf150076","Forum",charset='utf8')
cursor = db.cursor()

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

#soup = BeautifulSoup(html,"html.parser")
soup = BeautifulSoup(open("Contest2.html"),"html.parser")
tag = soup.find_all("td","t_f")
length = len(tag)
Time =0
for i in range(length):
	Stop = 1
	Time = Time+1
	Stop_Num = 0
	Str = tag[i].get_text('|','br /')
	Str = Str+'|'
	StrLen =len(Str)
	print Str;
	for k in range(StrLen):
		if Str[k]=='|':
			Stop_Num =Stop_Num+1
	for k in range(StrLen):
		if Str[k]=='|':
			#print "Stop is ",Stop
			if(Stop%5==1):
				Ret = k-1
				while(Str[Ret]!='|'):
					Ret = Ret-1
				Name = Str[Ret+4:k]
				#print "name is ",Name
				Stop = Stop+1
				continue
			if(Stop%5==2):
				Ret = k-1
				while(Str[Ret]!='|'):
					Ret = Ret-1
					
				City = Str[Ret+4:k]
				#print "City is ",City
				Stop = Stop+1
				continue
			if(Stop%5==3):
				Ret = k-1
				while(Str[Ret]!='|'):
					Ret = Ret-1
					
				Location = Str[Ret+4:k]
				#print "Location is ",Location
				Stop = Stop+1
				continue
			if(Stop%5==4):
				Ret = k-1
				while(Str[Ret]!='|'):
					Ret = Ret-1
				for Num in range(Ret+1,k):
					if is_number(Str[Num]):
						Score = Str[Num:Num+4]
						#print "Score is ",Score
						break
				if k-Ret>8:
					Memo = Str[Num+4:k]
				else:
					Memo = "Nothing"
				#print "Memo is ",Memo
				Stop = Stop+1
				continue
			if(Stop%5==0):
				Ret = k-1
				while(Str[Ret]!='|'):
					Ret = Ret-1
					
				Tel = Str[Ret+4:k]
				#print "Tel is ",Tel
				Stop = Stop+1
				print Time,Name,City,Location,Score,Tel
				print 
				SQL = """insert into Data values('%d','%s','%s','%s','%s','%s','%s')"""%(Time,Name,City,Location,Score,Tel,Memo)
				try:
					#cursor.execute(SQL)
					db.commit()
				except:
					db.rollback()
				continue
			
	


