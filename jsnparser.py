# Parsing Engine for Anago Output
# Asharudin 'aviezab' 2018 Aug 20-21

# import library needed
import json
from ast import literal_eval

# variable declaration, also this function will be used
per=[]
nor=[]
fac=[]
org=[]
gpe=[]
loc=[]
prd=[]
evt=[]
woa=[]
law=[]
lan=[]
dat=[]
tim=[]
prc=[]
mon=[]
qty=[]
ordi=[]
crd=[]
reg=[]

# for cleaning memory
def varkosong():
	global per
	global nor
	global fac
	global org
	global gpe
	global loc
	global prd
	global evt
	global woa
	global law
	global lan
	global dat
	global tim
	global prc
	global mon
	global qty
	global ordi
	global crd
	global reg

	per=[]
	nor=[]
	fac=[]
	org=[]
	gpe=[]
	loc=[]
	prd=[]
	evt=[]
	woa=[]
	law=[]
	lan=[]
	dat=[]
	tim=[]
	prc=[]
	mon=[]
	qty=[]
	ordi=[]
	crd=[]
	reg=[]

# example text from anago output
teks = " \"{'text': 'Budi', 'type': 'PER', 'score': 1.0, 'beginOffset': 0, 'endOffset': 1}, {'text': 'Haris', 'type': 'PER', 'score': 1.0, 'beginOffset': 2, 'endOffset': 3}, {'text': 'Bandung', 'type': 'GPE', 'score': 1.0, 'beginOffset': 5, 'endOffset': 6}, {'text': '1000', 'type': 'DAT', 'score': 1.0, 'beginOffset': 8, 'endOffset': 9}, {'text': 'ringgit', 'type': 'MON', 'score': 1.0, 'beginOffset': 9, 'endOffset': 10}\" "

def jsonkansaja(tulisan):
	global per
	global nor
	global fac
	global org
	global gpe
	global loc
	global prd
	global evt
	global woa
	global law
	global lan
	global dat
	global tim
	global prc
	global mon
	global qty
	global ordi
	global crd
	global reg
	#Load json to remove " in anago output
	tulisan = json.loads( tulisan )
	# convert text to tuple
	tp = literal_eval(tulisan)
	# count items in tuple
	i = len(tp)

	print (tp)


	varkosong()
	for x in range(0, i):
		if ( tp[x]['type'] == 'PER') :		
			varx = tp[x]['text']
			per.append(varx)
		if ( tp[x]['type'] == 'NOR') :		
			varx = tp[x]['text']
			nor.append(varx)
		if ( tp[x]['type'] == 'FAC') :		
			varx = tp[x]['text']
			fac.append(varx)
		if ( tp[x]['type'] == 'ORG') :		
			varx = tp[x]['text']
			org.append(varx)
		if ( tp[x]['type'] == 'GPE') :		
			varx = tp[x]['text']
			gpe.append(varx)
		if ( tp[x]['type'] == 'LOC') :		
			varx = tp[x]['text']
			loc.append(varx)
		if ( tp[x]['type'] == 'PRD') :		
			varx = tp[x]['text']
			prd.append(varx)
		if ( tp[x]['type'] == 'EVT') :		
			varx = tp[x]['text']
			evt.append(varx)
		if ( tp[x]['type'] == 'WOA') :		
			varx = tp[x]['text']
			woa.append(varx)
		if ( tp[x]['type'] == 'LAW') :		
			varx = tp[x]['text']
			law.append(varx)
		if ( tp[x]['type'] == 'LAN') :		
			varx = tp[x]['text']
			lan.append(varx)
		if ( tp[x]['type'] == 'DAT') :		
			varx = tp[x]['text']
			dat.append(varx)
		if ( tp[x]['type'] == 'TIM') :		
			varx = tp[x]['text']
			tim.append(varx)
		if ( tp[x]['type'] == 'PRC') :		
			varx = tp[x]['text']
			prc.append(varx)
		if ( tp[x]['type'] == 'MON') :		
			varx = tp[x]['text']
			mon.append(varx)
		if ( tp[x]['type'] == 'QTY') :		
			varx = tp[x]['text']
			qty.append(varx)
		if ( tp[x]['type'] == 'ORD') :		
			varx = tp[x]['text']
			ordi.append(varx)
		if ( tp[x]['type'] == 'crd') :		
			varx = tp[x]['text']
			crd.append(varx)
		if ( tp[x]['type'] == 'REG') :		
			varx = tp[x]['text']
			reg.append(varx)

	per = '{"Person": ' + json.dumps(per) + '}'
	nor = '{"PoliticalOrg": ' + json.dumps(nor) + '}'
	fac = '{"Facility": ' + json.dumps(fac) + '}'
	org = '{"Company": ' + json.dumps(org) + '}'
	gpe = '{"GeopoliticalEnt": ' + json.dumps(gpe) + '}'
	loc = '{"Location": ' + json.dumps(loc) + '}'
	prd = '{"Product": ' + json.dumps(prd) + '}'
	evt = '{"Event": ' + json.dumps(evt) + '}'
	woa = '{"WoArt": ' + json.dumps(woa) + '}'
	law = '{"Law": ' + json.dumps(law) + '}'
	lan = '{"Language": ' + json.dumps(lan) + '}'
	dat = '{"Date": ' + json.dumps(dat) + '}'
	tim = '{"Time": ' + json.dumps(tim) + '}'
	prc = '{"Percentage": ' + json.dumps(prc) + '}'
	mon = '{"Money": ' + json.dumps(mon) + '}'
	qty = '{"Quantity": ' + json.dumps(qty) + '}'
	ordi = '{"Ordinal": ' + json.dumps(ordi) + '}'
	crd = '{"Cardinal": ' + json.dumps(crd) + '}'
	reg = '{"Religion": ' + json.dumps(reg) + '}'		

	per = json.loads( per )
	nor = json.loads( nor )
	fac = json.loads( fac )
	org = json.loads( org )
	gpe = json.loads( gpe )
	loc = json.loads( loc )
	prd = json.loads( prd )
	evt = json.loads( evt )
	woa = json.loads( woa )
	law = json.loads( law )
	lan = json.loads( lan )
	dat = json.loads( dat )
	tim = json.loads( tim )
	prc = json.loads( prc )
	mon = json.loads( mon )
	qty = json.loads( qty )
	ordi = json.loads( ordi )
	crd = json.loads( crd )
	reg = json.loads( reg )
	
	
	res = {}
	res.update ( per )
	res.update ( nor )
	res.update ( fac )
	res.update ( org )
	res.update ( gpe )
	res.update ( loc )
	res.update ( prd )
	res.update ( evt )
	res.update ( woa )
	res.update ( law )
	res.update ( lan )
	res.update ( dat )
	res.update ( tim )
	res.update ( prc )
	res.update ( mon )
	res.update ( qty )
	res.update ( ordi )
	res.update ( crd )
	res.update ( reg )
	
	# Throw away escape encodings
	esce = "\\"
	esce2= chr(0)
	hases=str.maketrans(esce,esce2)
	esce = "\'"
	esce2= chr(34)
	hases2=str.maketrans(esce,esce2)
	res= str( res )

	res= res.translate(hases)
	res= res.translate(hases2)
	print ( res )
	return res
	# Clean memory
	res=''
	esce=None
	esce2=None
	varkosong()
	
jsonkansaja(teks)
