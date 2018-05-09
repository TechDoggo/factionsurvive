namecount = namecount +"1"
huntingskill = randint(-1,10)
miningskill = randint(-1,10)
geologyskill = randint(-1,10)
combatskill = randint(-1,10)
smithingskill = randint(-1,10)
size = randint(1,3)
haircolor = randint(1,4)
eyecolor = randint(1,3)
if size == 1:
	size = "small"
if size == 2:
	size = "medium"
if size == 3:
	size = "tall"
if haircolor == 1:
	haircolor = "blonde"
if haircolor == 2:
	haircolor = "brown"
if haircolor == 3:
	haircolor = "red"
if haircolor == 4:
	haircolor = "black"
	eyecolor = "blue"
if eyecolor == 2:
	eyecolor = "green"
if eyecolor == 3:
	eyecolor = "brown"
if smithingskill <= 1:
	q = q+"\n"+"##Cannot work in a forge."
if combatskill <= 1:
	q = q+"\n"+"##Is incredibly afraid of attackers."
if geologyskill <= 1:
	q = q+"\n"+"##Is afraid of the underground, and avoids caves."
if miningskill <= 1:
	q = q+"\n"+"##Does not have the arm strength to use a pickaxe all day."
if huntingskill <= 1:
	q = q+"\n"+"##Inner morales makes them believe killing animals is wrong."
if smithingskill > 5:
	q = q+"\n"+"##Very efficient at forging metal bars."
if combatskill > 5:
	q = q+"\n"+"##Very efficient at defending the camp."
if geologyskill > 5:
	q = q+"\n"+"##Very efficient at spotting unclaimed quarries."
if miningskill > 5:
	q = q+"\n"+"##Very efficient at mining metal ore."
if huntingskill > 5:
	q = q+"\n"+"##Very efficient at hunting prey for meat."
genderrand = randint(1,2)
if genderrand == 1:
	charname = names.get_full_name(gender = 'male')
	gender = "male" 
if genderrand == 2:
	charname = names.get_full_name(gender = 'female')
	gender = "female"
charname = charname + ".py"
name = open(charname, "w", 0)
if aa == 1:
	name.write('{0} {1}\n'.format("compskill=","True"))
	name.write('{0} {1}\n'.format("print","'This person is elligible for research dedication.'"))
name.write('{0} {1}\n'.format("##q","'%s'" % q ))
name.write('{0} {1}\n'.format("namecount =","'%s'" % charname ))
name.write('{0} {1}\n'.format("gender =","'%s'" % gender ))
name.write('{0} {1}\n'.format("huntingskill =","'%s'" % huntingskill ))
name.write('{0} {1}\n'.format("miningskill =","'%s'" % miningskill ))
name.write('{0} {1}\n'.format("geologyskill =","'%s'" % geologyskill ))
name.write('{0} {1}\n'.format("combatskill =","'%s'" % combatskill ))
name.write('{0} {1}\n'.format("smithingskill =","'%s'" % smithingskill ))
name.write('{0} {1}\n'.format("##q","'%s'" % q ))
name.write('{0} {1}\n'.format("##Height:","'%s'" % size))
name.write('{0} {1}\n'.format("##Hair Color:","'%s'" % haircolor ))
name.write('{0} {1}\n'.format("##Eye Color","'%s'" % eyecolor ))
name.write('{0} {1}\n'.format("print", "'Character Name: %s' % (charname)"))
name.write('{0} {1}\n'.format("print", "'Hunting Skill Level: %s' % (huntingskill)"))
name.write('{0} {1}\n'.format("print", "'Mining Skill Level: %s' % (miningskill)"))
name.write('{0} {1}\n'.format("print","'Geology Skill Level: %s' % (geologyskill)"))
name.write('{0} {1}\n'.format("print", "'Combat Skill Level: %s' % (combatskill"))
name.write('{0} {1}\n'.format("print", "'Smithing Skill Level: %s' % (smithingskill)"))
aa = randint(1,15)
q = ""
sys.stdout.flush()
name = open(charname, "r", 0)
src = "/home/runner/"+charname
dst = "/home/runner/charsheet/"+charname
os.renames(src, dst)