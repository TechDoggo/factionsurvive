import names
import os, glob
import shutil
import time
import sys
import random
from random import randint
huntingbonus = 0 
miningbonus = 0 
geologybonus = 0 
combatbonus = 0 
smithingbonus = 0  
a = "\n" * 100
print a 
pop = 0
print "Would you like to resume your game or make a new save?"
print "You cannot recover a deleted save!"
aa = raw_input("Type 'new' or 'resume':")
if aa == "new":
	os.remove("Savefile.py")
	print a 
	print("Save Deleted")
	time.sleep(1.5)
import time
from random import randint
a = "\n" * 100
print a 
print "Loading..."
time.sleep(.5)
print "Please be patient, this may take up to a few minutes."
1 == 1
if True:
	z = 2 
	namecount = "1"
	y = 0
	z == 2 
	q = ""
	while z == 2:
		y = y + 1
		print y
		if y >= 10:
			z = 1
		namecount = namecount +"1"
		huntingskill = randint(-1,10)
		huntingbonus = huntingbonus + huntingskill
		miningskill = randint(-1,10)
		miningbonus = miningbonus + miningskill
		geologyskill = randint(-1,10)
		geologybonus = geologybonus + geologyskill
		combatskill = randint(-1,10)
		combatbonus = combatbonus + combatskill
		smithingskill = randint(-1,10)
		smithingbonus = smithingbonus + smithingskill
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
		if eyecolor == 1:
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
		charname = str(charname)
		charname = charname + ".py"
		name = open(charname, "w", 0)
		pop = pop + 1 
		name.write('{0} {1}\n'.format("namecount =","'%s'" % charname ))
		name.write('{0} {1}\n'.format("gender =","'%s'" % gender ))
		name.write('{0} {1}\n'.format("huntingskill =","'%s'" % huntingskill ))
		name.write('{0} {1}\n'.format("miningskill =","'%s'" % miningskill ))
		name.write('{0} {1}\n'.format("geologyskill =","'%s'" % geologyskill ))
		name.write('{0} {1}\n'.format("combatskill =","'%s'" % combatskill ))
		name.write('{0} {1}\n'.format("smithingskill =","'%s'" % smithingskill ))
		name.write('{0} {1}\n'.format("##Height:","'%s'" % size))
		name.write('{0} {1}\n'.format("##Hair Color:","'%s'" % haircolor ))
		name.write('{0} {1}\n'.format("##Eye Color","'%s'" % eyecolor ))
		name.write('{0} {1}\n'.format("print", "'Character Name: %s' % (namecount)"))
		name.write('{0} {1}\n'.format("print", "'Hunting Skill Level: %s' % (huntingskill)"))
		name.write('{0} {1}\n'.format("print", "'Mining Skill Level: %s' % (miningskill)"))
		name.write('{0} {1}\n'.format("print","'Geology Skill Level: %s' % (geologyskill)"))
		name.write('{0} {1}\n'.format("print", "'Combat Skill Level: %s' % (combatskill)"))
		name.write('{0} {1}\n'.format("print", "'Smithing Skill Level: %s' % (smithingskill)"))
		aa = randint(1,10)
		if aa == 1:
			name.write('{0} {1}\n'.format("compskill=","True"))
			name.write('{0} {1}\n'.format("print","'This person is elligible for research dedication.'"))
		name.write('{0} {1}\n'.format("##q","'%s'" % q ))
		q = ""
		sys.stdout.flush()
		name = open(charname, "r", 0)
		src = "/home/runner/"+charname
		dst = "/home/runner/charsheet/"+charname
		os.renames(src, dst)
		print a
		print "Loading..."
		print "Please be patient, this may take up to 30 seconds."
ammo = 0
fear = 0
dealoffer = 0 
generator = 0 
power = False
sulfurmines = 0
namecount = "1"
tradeoffer = 0
q = ""
vault = 0
gen = 0
vaultprotect = 0 
farms = 0 
coalmines = 0 
metalmines = 0
walls = 0
quarrytot = 0
metalmineproduce = 0 
sulfurmineproduce = 0 
oildrillproduce = 0 
metalbonus = 0 
turnrotate = 0
coalmineproduce = 0
coal = 0 
customforge = 0 
oil = 0
totalhuntingloss = 0 
totalminingloss = 0 
totalgeologyloss = 0 
totalcombatloss = 0 
totalsmithingloss = 0
metalore = 0
raidedtimes = 0
quarry = 0 
sentpeople = 0
day = 0
camplog = 0
wood = 50
meat = 0
oildrills = 0
guns = 0
axe = 5
trademat = 1
meals = 10
sulfur = 0
gunpowder = 0
kitchen = 0
metal = 0
##newvars
radio = 0
print "Survive..."
try:
    execfile("Savefile.py")
except IOError:
    file = open("Savefile.py", 'w')
import Savefile
while True:
	if generator == 1:
		if oil >= 1:
			oil = oil - 1 
			power = True
	if pop <= 0:
		print a 
		print "All members of your faction have died..."
		break
	if huntingskill < 0:
		huntingskill = 0 
	if combatskill < 0:
		combatskill = 0 
	if miningskill < 0:
		miningskill = 0 
	if geologyskill < 0:
		geologyskill = 0 
	if smithingskill < 0:
		smithingskill = 0 
	meat = meat + (farms*2)
	if kitchen >= 1:
		if meat >= 5:
			meals = meals + 10 
			meat = meat - 5
	vaultprotect = vault*25
	metalore = metalore + ((metalmines*metalmineproduce)+int((miningbonus/60)))
	sulfur = sulfur + (sulfurmines*sulfurmineproduce)
	coal = coal + (coalmines*coalmineproduce)
	oil = oil + (oildrills*oildrillproduce)
	if raidedtimes == 6:
		print a 
		print "Hint: Sulfur can be traded for if you discover other campouts."
		aaa = raw_input("Press ENTER to resume...")
	if raidedtimes == 5:
		print a 
		print "Hint: Guns and Ammunition will help you defend your Faction from being raided by others."
		aaaa = raw_input("Press ENTER to resume...")
		##randomevent
	randomevent = randint(0,15+walls)
	if randomevent == 4:
		raidchance = randint(0,walls)
		print raidchance
		if raidchance == 0:
			print a 
			print "A Faction has begun to raid you."
			time.sleep(1.5)
			randmulti = randint(1,3)
			factionpop = pop*randmulti
			faction = randint(1,factionpop)
			deathtoll = randint(0,faction)
			deathtoll = deathtoll + (combatbonus/50)
			if guns > 0:
				if ammo > 0:
					ammocap = deathtoll
					deathtoll = deathtoll + ammo 
					ammo = ammo - ammocap
					if ammo < 0:
						ammo = 0
			print deathtoll
			time.sleep(2)
			if deathtoll < pop:
				print a
				sulfursteal = randint(0,sulfur)
				woodsteal = randint(0,wood)
				mealssteal = randint(0, meals)
				ammosteal = randint(0,ammo)
				metalsteal = randint(0,metal)
				if metalsteal > metal:
					metal = 0
				if ammosteal > ammo:
					ammo = 0 
				if mealssteal > meals:
					meals = 0 
				if woodsteal > wood:
					wood = 0 
				if sulfursteal > sulfur:
					sulfur = 0 
				if metalsteal > metal:
					metalsteal = 0
				if vault > 0:
					metalsteal = metalsteal - vaultprotect
					if metalsteal < 0:
						metalsteal = 0 
					sulfursteal = sulfursteal - vaultprotect
					if sulfursteal < 0:
						sulfursteal = 0 
					woodsteal = woodsteal - vaultprotect
					if woodsteal < 0:
						woodsteal = 0 
					mealssteal = mealssteal - vaultprotect
					if mealssteal < 0:
						mealssteal = 0 
					ammosteal = ammosteal - vaultprotect
					if ammosteal < 0:
						ammosteal = 0
				print ammosteal
				print sulfursteal
				print woodsteal
				print metalsteal
				print mealssteal
				print "\n" * 100
				sulfur = sulfur - sulfursteal
				wood = wood - woodsteal
				meals = meals - mealssteal
				ammo = ammo - ammosteal
				metal = metal - metalsteal
				poploss = pop/2
				for i in range(poploss):
					execfile('Charloss.py')
					totalsmithingloss
					
				pop = pop - poploss
				pop = int(pop)
				print "The Faction raided you successfully."
				if walls > 0:
					wallbust = randint(1,3)
					if wallbust == 2:
						walls = walls - 1
						print a
						print "The Raiders destroyed one of your walls."
						time.sleep(1.5)
						wood = wood + 10 
						metal = metal + 1
				raidedtimes = raidedtimes + 1
				time.sleep(2)
				print a 
				print "They killed %s people in your camp." % (poploss)
				print "They stole:"
				print "Sulfur Stolen - %s" % (sulfursteal)
				print "Wood Stolen - %s" % (woodsteal)
				print "Meals Stolen - %s" % (mealssteal)
				print "Ammunition Stolen - %s" % (ammosteal)
				print "Metal Stolen - %s" % (metalsteal)
				print ""
				aaa = raw_input("Press ENTER to accept your loss...")
			elif deathtoll > pop:
				print a 
				gunsteal = randint(1,2)
				ammorob = randint(5,10)
				slave = randint(1,faction)
				print "The Faction was unsuccessful in their raid."
				if gunsteal == 1:
					gunmark = ""
				if gunsteal > 1:
					gunmark = "s"
				print "You've taken %s gun%s with %s rounds. You've also taken %s people as workers." % (gunsteal, gunmark, ammorob, slave)
				pop = pop + slave 
				for i in range(slave):
					execfile('chargen.py')
				guns = guns + gunsteal
				ammo = ammo + ammorob
				aaa = raw_input("Press ENTER to loot...")
	if randomevent == 3:
		loot = randint(1,3)
		if loot == 3:
			lootname = "meals"
			if meals < 0:
				print a 
				print "Raiders attempted to steal food, only to find you are starving as well."
				aaaa = raw_input("Press ENTER to resume...")
			if meals > 0:
				lootcount = randint(1,meals)
				print a 
				print "A Raiders Faction has stolen %s meals from you!" % (lootcount)
				aaaa = raw_input("Press ENTER to resume...")
				meals = meals - lootcount
			camplog = camplog + 1
		if loot == 2:
			lootname = "metal"
			if metal < 0:
				print "Raiders looked for metal, but found none in your camp!"
				aaaa = raw_input("Press ENTER to resume...")
			if metal > 0:
				lootcount = randint(1,metal)
				print a 
				print "A Raiders Faction has stolen %s metal from you!" % (lootcount)
				aaaaa = raw_input("Press ENTER to resume...")
				metal = metal - lootcount
			camplog = camplog + 1
		if loot == 1:
			lootname = "sulfur"
			if sulfur < 0:
				print a 
				print "A group of Raiders tried to steal sulfur, only to find none."
				aaaa = raw_input("Press ENTER to resume...")
			if sulfur > 0:
				lootcount = randint(1,sulfur)
				sulfur = sulfur - lootcount
			camplog = camplog + 1
	if randomevent == 1:
		if meals >= 10:
			print a
			print "A Faction will send you members if you send them resources."
			foodrand = randint(1,meals)
			print ""
			print "They are requesting %s meals." % (foodrand)
			aaaa = raw_input("'Yes' or 'No':")
			aaaa = aaaa.lower()
			if aaaa == "no":
				print a
				time.sleep(1)
				print a
				print "The Faction leader understands and leaves you in peace"
				aaaaaa = raw_input("Press ENTER to resume")
			if aaaa == "yes":
				if meals < foodrand:
					print a 
					print "You don't have enough food to share."
					aaaa = raw_input("Press ENTER to resume...")
				if meals >= foodrand:
					meals = meals - foodrand
					print a 
					groupjoin = randint(1,5)
					print "A group of %s has joined your party." % (groupjoin)
					pop = pop + groupjoin
					for i in range(groupjoin):
						execfile('chargen.py')
					aaaaaa = raw_input("Press ENTER to resume...")
	if randomevent == 10:
		print a 
		execfile("chargen.py")
		print a 
		pop = pop + 1
		charnamedisp = str(charname)
		charnamedisp = charnamedisp.replace(".py","")
		print "%s joined your Faction." % (charnamedisp)
		aaaa = raw_input("Press ENTER to resume...")
	turnrotate = turnrotate + 1 
	if turnrotate == 2:
		mealsconsume = (pop/6)
		if pop < 6:
			mealsconsume = 1
		mealsconsume = int(mealsconsume)
		meals = meals - mealsconsume
		turnrotate = turnrotate - 2 
	if meals <= 0:
		meals = 0 
		for i in range(1):
			execfile('Charloss.py')
		pop = pop - 1
		print a
		print "Members are beginning to starve... Find food fast!"
		time.sleep(2)
	print a
	print "Meals: %s" % (meals)
	print "Ammo: %s" % (ammo)
	print "Population: %s" % (pop)
	print "Day: %s" % (day)
	print ""
	## choices made here
	choice = raw_input("Type 'help' for a list of actions:")
	if choice == "people":
		print a 
		print "Names:"
		ree = os.listdir('/home/runner/charsheet/')
		ree = str(ree)
		ree = ree.replace(".py","")
		ree = ree.replace("[","")
		ree = ree.replace("]","")
		ree = ree.replace("'","")
		ree= ree.replace(",","""
""")
		print ree
		aa = raw_input("Type name to view, type 'manage' or press ENTER...")
		if aa == "manage":
			print a 
			print "Assign a group manager "
		if aa != "":
			aa = aa + ".py"
			print a
			aa = "/home/runner/charsheet/" + aa
			print aa
			print a 
			execfile(aa)
			q = raw_input("Press ENTER to resume...")
	if choice == "radio":
		if radio < 1:
			print a 
			print "You have not made a radio yet."
			aa = raw_input("Press ENTER to resume...")
		if radio >= 1:
			if generator < 1:
				print a 
				print "You don't have a generator."
			if generator >= 1:
				if power == False:
					print a
					print "You don't have power."
					aa = raw_input("Press ENTER to resume...")
				if power == True:
						print a 
						a = randint(1,4)
						if a == 1:
							print a 
							print "You have established connection with a survivor."
							pop = pop + 2 
							for i in range(2):
								execfile('chargen.py')
							aa = raw_input("Press ENTER to resume...")
	if choice == "quit":
		print a 
		Savefile = open("Savefile", "a")
		##savevars
		Savefile.write('{0} {1}\n'.format("ammo=", ammo))
		Savefile.write('{0} {1}\n'.format("generator=", generator))
		Savefile.write('{0} {1}\n'.format("power=", power))
		Savefile.write('{0} {1}\n'.format("fear=", fear))
		Savefile.write('{0} {1}\n'.format("dealoffer=", dealoffer))
		Savefile.write('{0} {1}\n'.format("sulfurmines=", sulfurmines))
		Savefile.write('{0} {1}\n'.format("tradeoffer=", tradeoffer))
		Savefile.write('{0} {1}\n'.format("vault=", vault))
		Savefile.write('{0} {1}\n'.format("vaultprotect=", vaultprotect))
		Savefile.write('{0} {1}\n'.format("farms=", farms))
		Savefile.write('{0} {1}\n'.format("coalmines=", coalmines))
		Savefile.write('{0} {1}\n'.format("metalmines=", metalmines))
		Savefile.write('{0} {1}\n'.format("walls=", walls))
		Savefile.write('{0} {1}\n'.format("quarrytot=", quarrytot))
		Savefile.write('{0} {1}\n'.format("metalmineproduce=", metalmineproduce))
		Savefile.write('{0} {1}\n'.format("sulfurmineproduce=", sulfurmineproduce))
		Savefile.write('{0} {1}\n'.format("oildrillproduce=", oildrillproduce))
		Savefile.write('{0} {1}\n'.format("turnrotate=", turnrotate))
		Savefile.write('{0} {1}\n'.format("coalmineproduce=", coalmineproduce))
		Savefile.write('{0} {1}\n'.format("coal=", coal))
		Savefile.write('{0} {1}\n'.format("oil=", oil))
		Savefile.write('{0} {1}\n'.format("customforge =","'%s'" % customforge))
		Savefile.write('{0} {1}\n'.format("metalore=", metalore))
		Savefile.write('{0} {1}\n'.format("raidedtimes=", raidedtimes))
		Savefile.write('{0} {1}\n'.format("quarry=", quarry))
		Savefile.write('{0} {1}\n'.format("sentpeople=", sentpeople))
		Savefile.write('{0} {1}\n'.format("day=", day))
		Savefile.write('{0} {1}\n'.format("camplog=", camplog))
		Savefile.write('{0} {1}\n'.format("wood=", wood))
		Savefile.write('{0} {1}\n'.format("meat=", meat))
		Savefile.write('{0} {1}\n'.format("oildrills=", oildrills))
		Savefile.write('{0} {1}\n'.format("guns=", guns))
		Savefile.write('{0} {1}\n'.format("axe=", axe))
		Savefile.write('{0} {1}\n'.format("trademat=", trademat))
		Savefile.write('{0} {1}\n'.format("meals=", meals))
		Savefile.write('{0} {1}\n'.format("pop=", pop))
		Savefile.write('{0} {1}\n'.format("sulfur=", sulfur))
		Savefile.write('{0} {1}\n'.format("gunpowder=", gunpowder))
		Savefile.write('{0} {1}\n'.format("metal=", metal))
		Savefile.write('{0} {1}\n'.format("kitchen=", kitchen))
		Savefile.write('{0} {1}\n'.format("radio=", radio))
		Savefile.write('{0} {1}\n'.format("gen=", gen))
		shutil.move('Savefile', 'Savefile.py')
		Savefile.close
		break
	if choice == "popboost":
		pop = pop * 2
	if choice == "manage":
		print a 
		quarrytot = coalmines + sulfurmines + metalmines + oildrills + quarry
		print "1. Quarry Manager: Quarries - %s" % (quarrytot)
		print "2. Campsite Manager"
		print "3. Defenses Manager"
		choice = raw_input("Type the number:")
		if choice == "3":
			print a 
			print "Walls: %s" % (walls)
			print ""
			aa = raw_input("Type 'build' to open build menu:")
			if aa == "build":
				print a 
				print "1. Wood Wall: 50 wood, 2 metal"
				print ""
				print "Max of 4 walls around camp. May need rebuilding over time."
				print ""
				aa = raw_input("Type number to build:")
				if aa == "1":
					print a 
					if wood < 50:
						print a 
						print "You don't have enough wood."
						aa = raw_input("Press ENTER to resume...")
					if wood >= 50:
						if metal < 2:
							print a 
							print "You don't have enough metal..."
							aa =raw_input("Press ENTER to resume...")
						if metal >= 2:
							if wall >= wall:
								print a
								print "You have enclosed your camp already."
								aa = raw_input("Press ENTER to resume...")
							if wall < 4:
								print a 
								time.sleep(1.5)
								print "1x Wall was constructed."
								wood = wood - 50 
								metal = metal - 2 
								wall = wall + 1 
		if choice == "2":
			print a
			print "Vaults: %s" % (vault)
			print "Farms: %s" % (farms)
			print "Kitchens: %s" % (kitchen)
			print "Advanced Furnaces: %s" % (customforge)
			print ""
			print ""
			print ""
			print ""
			print ""
			aa = raw_input("Type 'build' to open build menu:")
			if aa == "build":
				print a
				print "1. Vault: 25 metal, 10 wood. (Will protect 25 items.)"
				print "2. Farm: 25 wood, 1 metal. (Will produce meat.)"
				print "3. Kitchen: 30 wood, 1 metal. (Will cook meat if available.)"
				print "4. Advanced Furnace: 10 metal, 10 wood. (Will increase smithy happiness)"
				print ""
				aa= raw_input("Type the number to construct:")
				if aa == "4":
					if customforge >= 1:
						print a 
						print "You already have a forge constructed."
						aa = raw_input("Press ENTER to resume...")
					if customforge < 1:
						if metal < 10:
							print "You don't have enough metal."
							aa = raw_input("Press ENTER to resume...")
						if metal >= 10:
							if wood < 10:
								print "You don't have enough wood."
								aa = raw_input("Press ENTER to resume...")
							if wood >= 10:
								print a 
								time.sleep(.5)
								print "Advanced Furnace was crafted."
								metalbonus = metalbonus + 10 
				if aa == "3":
					if kitchen >= 1:
						print a
						print "You already have a kitchen."
						aa = raw_input("Press ENTER to resume...")
					if kitchen < 1:
						if wood < 30:
							print a 
							print "Not enough wood."
							aa = raw_input("Press ENTER to resume...")
						if wood >= 30:
							if metal < 1:
								print a 
								print "Not enough metal."
								aa = raw_input("Press ENTER to resume...")
							if metal >= 1:
								print a 
								metal = metal - 1 
								wood = wood - 30 
								kitchen = kitchen + 1 
								time.sleep(1.5)
								print "Kitchen was built."
								aa = raw_input("Press ENTER to resume...")
				if aa == "2":
					if wood < 25:
						print a 
						print "Not enough wood."
						aa =raw_input("Press ENTER to resume...")
					if wood >= 25:
						if metal < 1:
							print a 
							print "Not enough metal."
							aa = raw_input("Press ENTER to resume...")
						if metal >= 1:
							print a 
							metal = metal - 1 
							wood = wood - 25 
							farms = farms + 1 
							time.sleep(1.5)
							print "Farm was constructed"
				if aa == "1":
					if metal < 25:
						print a
						print "You don't have enough metal."
						aaa = raw_input("Press ENTER to resume...")
					if metal >= 25:
						if wood >= 10:
							metal = metal - 25 
							wood = wood - 10 
							vault = vault + 1 
							time.sleep(1)
							print a 
							print "Vault was made. (1x)"
							aaa = raw_input("Press ENTER to resume...")
						if wood < 10:
							print a 
							print "You don't have enough wood."
							aa = raw_input("Press ENTER to resume...")
		if choice == "1":
			print a
			print "Sulfur Mines: %s" % (sulfurmines)
			print "Metal Mines: %s" % (metalmines)
			print "Coal Mines: %s" % (coalmines)
			print "Oil Drills: %s" % (oildrills)
			print ""
			print "Unclaimed Quarries: %s" % (quarry)
			aaa = raw_input("Press ENTER or type 'claim' to claim a quarry:")
			if aaa == "claim":
				if quarry > 0:
					if metal >= 10:
						if wood < 50:
							print a 
							print "You'll need 50 wood to construct a shaft."
							aa = raw_input("Press ENTER to resume...")
						if wood >= 50:
							print a 
							quarrytype = randint(1,3)
							if quarrytype == 3:
								coalmines = coalmines + 1
								name = "coal"
								coalmineproduce = coalmineproduce+randint(5,10)
							if quarrytype == 2:
								metalmines = metalmines + 1 
								name = "metal"
								metalmineproduce = metalmineproduce+randint(3,6)
							if quarrytype == 1:
								sulfurmines = sulfurmines + 1 
								name = "sulfur"
								sulfur = sulfurmineproduce+randint(1,3)
							print "After claiming the quarry, you have discovered that it is a %s mine." % (name)
							quarry = quarry - 1 
							print ""
							time.sleep(1.5)
							print "Shaft was constructed, 50 wood and 10 metal were used."
							aaa = raw_input("Press ENTER to resume...")
					if metal < 10:
						print a 
						print "You'll need 10 metal to construct a shaft."
						aa = raw_input("Press ENTER to resume...")
	if choice == "vault":
		print a 
		print "Stockpile-"
		print ""
		print "Meat: %s" % (meat)
		print "Metal: %s" % (metal)
		print "Metal Ore: %s" % (metalore)
		print "Wood: %s" % (wood)
		print "Gunpowder: %s" % (gunpowder)
		print "Ammunition: %s" % (ammo)
		print "Sulfur: %s" % (sulfur)
		print "Axes: %s" % (axe)
		print "Guns: %s" % (guns)
		print "Logged Campsites: %s" % (camplog)
		print ""
		aaaa = raw_input("Press ENTER to resume...")
	if choice == "hunt":
		print a 
		if ammo <= 0:
			meatcount = randint(2,6)
			meat = meat + meatcount +int((huntingbonus/60))
		if ammo > 0:
			if guns > 0:
				ammo - 1 
				meatcount = randint(5,10)
				meat = meat + meatcount +int((huntingbonus/60))
		print "Your hunting party has harvested %s meat." % (meatcount)
		time.sleep(1)
	if choice == "mealsfree":
		meals = 99999999999
	if choice == "camplogfree":
		camplog = 1000
	if choice == "takestuff":
		sulfure = 0 
		wood = 0 
		##cheats
		metal = 0
	if choice == "givestuff":
		sulfur = sulfur + 10000000000
		wood = wood + 10000000000
		metal = metal + 10000000000
	if choice == "kill":
		pop = pop - 10000000000
		print a 
		print "All members have committed suicide..."
	if choice == "make":
		print a 
		print "Stockpile-"
		print "Meat: %s" % (meat)
		print "Metal: %s" % (metal)
		print "Metal Ore: %s" % (metalore)
		print "Wood: %s" % (wood)
		print "Gunpowder: %s" % (gunpowder)
		print "Ammunition: %s" % (ammo)
		print "Sulfur: %s" % (sulfur)
		print ""
		print ""
		print ""
		print "Crafting-"
		print """
1. 10x Ammunition: 2 gunpowder, 2 metal							8. Radioset: 2 metal, 5 wood (gen required)
2. 10x Gunpowder: 5 wood, 20 sulfur									9. Generator: 5 metal, 5 sulfur
3. Barricade: 10 metal, 5 wood
4. 15x meal: 5 meat, 1 wood													
5. Automatic Rifle: 10 metal, 10 Gunpowder, 5 wood	
6. 5x Metal: 10 metal ore, 10 wood									
7. 2x Wooden Axe: 10 wood														
		"""
		##crafting menu located here
		choice = raw_input("Type the number:")
		if choice == "9":
			if generator >= 1:
				print a 
				print "You already have a generator!"
			if generator < 1:
				if metal < 5:
					print "You don't have enough metal."
					aa = raw_input("Press ENTER to resume...")
				if metal >= 5:
					if sulfur < 5:
						print a 
						print "You don't have enough sulfur."
						aa = raw_input("Press ENTER to resume...")
					if sulfur >= 5:
						print a 
						time.sleep(.5)
						print "Generator was crafted."
						aa = raw_input("Press ENTER to resume...")
		if choice == "8":
			if radio >= 1:
				print a 
				print "You already have a comm system."
				aa = raw_input("Press ENTER to resume...")
			if radio < 1:
				if metal >= 2:
					if wood >= 5:
						wood = wood - 5 
						metal = metal - 2 
						radio = radio + 1
					if wood < 5:
						print a 
						print "Not enough wood."
						aa=raw_input("Press ENTER to resume...")
				if metal < 2:
					print a 
					print "Not enough metal."
					aa=raw_input("Press ENTER to resume...")
		if choice == "7":
			if wood <= 10:
				print a 
				print "Not enough wood."
				time.sleep(1)
			if wood > 10:
				wood = wood - 10 
				print a 
				time.sleep(2)
				axe = axe + 2
				print "Axe was crafted (2x)"
				aaa = raw_input("Press ENTER to resume...")
		if choice == "5":
			if metal <= 10:
				print a
				print "Not enough metal."
				time.sleep(1)
			if metal > 10:
				if gunpowder <= 10:
					print a 
					print "Not enough gunpowder."
					time.sleep(1)
				if gunpowder > 10:
					if wood <= 5:
						print a 
						print "Not enough wood."
						time.sleep(1)
					if wood > 5:
						print a 
						wood = wood - 5 
						metal = metal - 10 
						gunpowder = gunpowder - 10
						print a 
						time.sleep(2)
						print "Automatic Rifle was crafted. (1x)"
						aaa =raw_input("Press ENTER to resume...")
		if choice == "6":
			if metalore <= 0:
				print a 
				print "Not enough ore."
				time.sleep(1)
			if metalore >= 1:
				if wood <= 0:
					print a 
					print "Not enough wood."
					time.sleep(1)
				if wood >= 1:
					wood = wood - 10
					metalore = metalore - 10 
					metaladd = metal + 5 +int((metalbonus/60))
					metal = metal + metaladd
					print a
					time.sleep(2)
					print "Metal was made (%sx)" % (metaladd)
					aaa = raw_input("Press ENTER to resume...")
		if choice == "4":
			if meat <= 0:
				print a 
				print "Not enough meat."
				aaa = raw_input("Press ENTER to resume...")
			if meat >= 5:
				if wood <= 0:
					print a 
					print "Not enough lumber."
					time.sleep(1)
				if wood >= 1:
					wood = wood - 1 
					meat = meat - 5
					meals = meals + 15
					print a 
					time.sleep(2)
					print "Meals were cooked (15x)"
					aaa = raw_input("Press ENTER to resume...")
		if choice == "2":
			if sulfur <= 0:
				print a
				print "Not enough sulfur."
				time.sleep(1)
			if sulfur >= 20:
				if wood <= 0:
					print a
					print "Not enough lumber."
					time.sleep(1)
				if wood >= 5:
					wood = wood - 5
					sulfur = sulfur - 20
					gunpowder = gunpowder + 10
					print a 
					time.sleep(2)
					print "Gunpowder was crafted (10x)"
					aaa = raw_input("Press ENTER to resume...")
		if choice == "1":
			if gunpowder <= 0:
				print a 
				print "Not enough gunpowder."
				time.sleep(1)
			if gunpowder >= 2:
				if metal <= 0:
					print a 
					print "Not enough metal."
					time.sleep(1)
				if metal >= 2:
					metal = metal - 2
					gunpowder = gunpowder - 2
					ammo = ammo + 10
					print a
					time.sleep(2)
					print "Ammunition was crafted (10x)"
					aaa = raw_input("Press ENTER to resume...")
	if choice == "raid":
		print a 
		print ""
		if 1 == 1:
			if camplog <= 0:
				print a 
				print "Camps in Scouting Log: %s" % (camplog)
				print ""
				print ""
				print ""
				print "You don't have the location of any camps. Try searching for some."
				aaaaa = raw_input("Press ENTER to resume...")
			if camplog > 0:
				print a
				oil = randint(1,100)
				guns = randint(1,20)
				ammoloot = randint(1,100)
				camppop = randint(1,10)
				print "Camps in Scouting Log: %s" % (camplog)
				print ""
				print ""
				print ""
				print "Your crew has scouted out a survivor camp."
				print "Would you like to make a trade or attempt a raid?"
				option = raw_input("Type 't' or 'r' or press ENTER to quit:")
				if option == "r":
					print a
					if camplog < 1:
						print ""
					if camplog >= 1:
						print a 
						print "How many people are you going to return to the camp?"
						print ""
						print "Population: %s" % (pop)
						print ""
						sentpeople = raw_input("Type the number of people you want to send:")
						print a
						if sentpeople == "":
							sentpeople = 0
						raidname = raw_input("Name your raiding party, or press ENTER:")
						if raidname == "":
							raidname = "raiding party"
						camppop = randint(1,20)
						sentpeople = int(sentpeople)
						pop = int(pop)
						popcount = sentpeople * 2
						deathtoll = randint(0,popcount)
						weaponbreak = randint(1,10)
						if sentpeople == 0:
							print "Nobody was sent."
							deathtoll == 99999999999999
						if sentpeople > pop:
							print a 
							print "You tried to send more people than you have! Plan ahead better next time!"
							deathtoll = 99999999
						print deathtoll
						time.sleep(2)
						print a 
						if weaponbreak == 5:
							if guns > 0:
								guns = guns - 1
						loot = randint(1,5)
						print a 
						print "The radio is silent."
						time.sleep(1)
						if weaponbreak == 5:
							if guns > 0:
								if weaponbreak > guns:
									weaponbreak = guns
								print "They've reported a loss of %s guns." % (weaponbreak)
						time.sleep(2)
						if deathtoll >= sentpeople:
							print a 
							print "Your raid failed horribly, you've lost all members of the raiding party."
							raidloss = 0 
							while raidloss <= sentpeople:
								execfile("Charloss.py")
								raidloss = raidloss + 1
							pop = pop - sentpeople
							time.sleep(1)
							print "You've lost %s members of your faction." % (sentpeople)
							aaaa = raw_input("Press ENTER to resume...")
						if deathtoll < sentpeople:
							time.sleep(1)
							print a 
							time.sleep(1)
							print "The %s calls you over a radio. From what you can gather, it's gone well." % (raidname)
							time.sleep(2)
							print a 
							lootcount = randint(5, 50)
							loottable = randint(1,5)
							if loottable == 5:
								loot = "gunpowder"
								gunpowder = gunpowder + lootcount
							if loottable == 4:
								loot = "meals"
								meals = meals + lootcount
							if loottable == 3:
								loot = "metal"
								metal = metal + lootcount +int((miningbonus/60))
							if loottable == 2:
								loot = "wood"
								wood = wood + lootcount
							if loottable == 1:
								loot = "sulfur"
								sulfur = sulfur + lootcount
							print a 
							print "The %s aquired %s %s!" % (raidname, lootcount, loot)
							sentpeople = int(sentpeople)
							deathtoll2 = randint(1,sentpeople)
							pop = pop - deathtoll2
							raidloss = 0 
							while raidloss <= sentpeople:
								delpath = (random.choice(glob.glob("/home/runner/charsheet/*.py")))
								sendpath = "/home/runner/Char_dump/"+delpath
								os.renames(delpath,sendpath)
								raidloss = raidloss + 1
							camplog = camplog - 1
							print "In the heat of the battle you've lost %s members of %s" % (deathtoll2, raidname)
							aaaa = raw_input("Press ENTER to resume....")
				if option == "t":
					random = randint(1,3)
					if random == 1:
						print a 
						print "The camp politely rejected the trade."
						time.sleep(1)
					if random == 3:
						random = 2
					if random == 2:
						print a 
						print "The camp wants to make a deal."
						random = randint(1,5)
						if random == 5:
							tradeoffer = "sulfur"
						if random == 4:
							tradeoffer = "meals"
						if random == 3:
							tradeoffer = "gunpowder"
						if random == 2:
							tradeoffer = "metal"
						if random == 1:
							tradeoffer = "wood"
						print a 
						randomsell = randint(1,50)
						randomp = randint(1,5)
						randombuy = randint(1,50)
						if randomp == 5:
							dealoffer = "wood"
							give = wood
						if randomp == 4:
							dealoffer = "metal"
							give = metal
						if randomp == 3:
							dealoffer = "gunpowder"
							give = gunpowder
						if randomp == 2:
							dealoffer = "meals"
							give  = meals
						if randomp == 1:
							dealoffer = "sulfur"
							give = sulfur
						time.sleep(1)
						##camp deals center - loc campdeal
						print "The camp would like %s %s. They will give you %s %s" % (randomsell, tradeoffer, randombuy,dealoffer)
						time.sleep(1)
						print "You can only say one answer! Type 'yes' or 'no'"
						choice = raw_input("'yes' or 'no':")
						if tradeoffer == "sulfur":
							if sulfur >= randomsell:
								trademat = 0
						if tradeoffer == "meals":
							if meals >= randomsell:
								trademat = 0 
						if tradeoffer == "gunpowder":
							if gunpowder >= randomsell:
								trademat = 0
						if tradeoffer == "wood":
							if wood >= randomsell:
								trademat = 0
						if tradeoffer == "metal":
							if metal >= randomsell:
								trademat = 0
						if choice == "yes":
							if trademat != 0:
								print a 
								print "You don't have the required trade products."
								time.sleep(1)
								aaaa = raw_input("Press ENTER to resume...")
							if trademat == 0:
								print "You traded and aquired %s %s" % (randombuy, dealoffer)
								trademat = 1
								if tradeoffer == "wood":
									wood = wood - randomsell
								if tradeoffer == "metal":
									metal = metal - randomsell
								if tradeoffer == "gunpowder":
									gunpowder = gunpowder - randomsell
								if tradeoffer == "meals":
									meals = meals - randomsell
								if tradeoffer == "sulfur":
									sulfur = sulfur - randomsell
								if dealoffer == "sulfur":
									sulfur = sulfur + randombuy
								if dealoffer == "meals":
									meals = meals - randombuy
								if dealoffer == "gunpowder":
									gunpowder = gunpowder + randombuy
								if dealoffer == "wood":
									wood = wood + randombuy
								if dealoffer == "metal":
									metal = metal + randombuy
								time.sleep(1)
						if choice == "no":
							print a
							print "The camp leader leaves you in peace."
	if choice == "scout":
		print a 
		rand = randint(5,5)
		if rand == 9:
			print a
			print "The search party located some metal ore."
			metalore = metalore + (randint(2,5)+int((miningbonus/20)))
			aaaaa = raw_input("Press ENTER to resume")
		if rand == 8:
			print a 
			print "Your crew has discovered an unclaimed quarry."
			quarry = quarry + 1
			aaa = raw_input("Press ENTER to resume...")
		if rand == 6:
			print a
			print "The search party located some metal ore."
			metalore = metalore + randint(2,5)
			aaaaa = raw_input("Press ENTER to resume")
		if rand == 3:
			print a
			if axe <= 0:
				print "Your crew discovered a grove of trees, but you didn't have any axes!"
				aaa = raw_input("Press ENTER to resume...")
			if axe >= 1:
				print "Your crew discovered a grove of trees. Lumber has been gathered."
				axe = axe - 1
				wood = wood + 10
				aaa = raw_input("Press ENTER to resume...")
		if rand == 7:
			print a 
			print "Your searched party located a sulfur deposit, gaurded by another faction."
			print "Choose to fight them, or trade for sulfur?"
			aaa = raw_input("Type 'trade' or 'raid':")
			if aaa == "raid":
				print a 
				camppop = randint(1,20)
				sentpeople = int(sentpeople)
				popcount = pop
				deathtoll = randint(0,popcount)
				if guns > 0:
					ammocap = ammo 
					deathtoll = deathtoll - ammocap
				if deathtoll >= pop:
					lostpeople = randint(1,pop)
					raidloss = 0 
					for i in range(lostpeople):
						execfile('Charloss.py')
					print "The raiding crew failed, losing %s people..." % (lostpeople)
					pop = pop - lostpeople
				if deathtoll < pop:
					halfpop = pop/3
					lostpeople = randint(1,halfpop)
					lostpeople = int(lostpeople)
					pop = pop - lostpeople
					raidloss = 0 
					for i in range(lostpeople):
						execfile('Charloss.py')
					print "The raiding crew went well, you only lost %s people." % (lostpeople)
					sulfurstolen = randint(1,pop)
					print "You've also stolen %s sulfur from the camp!" % (sulfurstolen)
					sulfur = sulfur + sulfurstolen
					aaa = raw_input("Press ENTER to resume...")
			if aaa == "trade":
				print a 
				tradedeal = randint(1,3)
				sulfursell = randint(1,10)
				sulfurtrade = randint(5,20)
				if tradedeal == 3:
					trade = "ammunition"
					deal = ammo 
				if tradedeal == 2:
					trade = "metal"
					deal = metal
				if tradedeal == 1:
					trade = "meals"
					deal = meals
				print "The Faction requests %s %s in trade for %s sulfur." % (sulfurtrade,trade,sulfursell)
				aaa = raw_input("Type 'yes' or 'no':")
				if aaa == "yes":
					if deal < sulfurtrade:
						print "You don't have enough of the required resources."
						aaa = raw_input("Press ENTER to resume...")
					if deal >= sulfurtrade:
						print a
						sulfur = sulfur + sulfursell
						if trade == "meals":
							meals = meals - sulfurtrade
						if trade == "metal":
							metal = metal - sulfurtrade
						if trade == "ammunition":
							ammo = ammo - sulfurtrade
						print "The Faction leader hands over the sulfur and parts ways."
						aaa = raw_input("Press ENTER to resume...")
		if rand == 2:
			print a
			print "The search party located some metal ore."
			metalore = metalore + 2+(int(miningbonus/60))
			aaaaa = raw_input("Press ENTER to resume")
		if rand == 5:
			print a 
			if pop == 0:
				lostmembers = 1 
			if pop > 1:
				lostmembers = randint(1,(pop-1))
			fear = fear + randint(1,5)
			if lostmembers >= pop:
				lostmembers = pop
			dam = randint(1,1)
			print "Your crew was ambushed by another faction! You lost %s members in the fight." % (lostmembers)
			dadaddad = raw_input("Press ENTER to resume...")
			pop = pop - lostmembers
			raidloss = 0 
			for i in range(lostmembers):
				execfile('Charloss.py')
			print "The raiding crew failed, losing %s people..." % (lostmembers)
		if rand == 4:
			print a
			if axe <= 0:
				print "Your crew discovered a grove of trees, but you didn't have any axes!"
				aaa = raw_input("Press ENTER to resume...")
			if axe >= 1:
				print "Your crew discovered a grove of trees. Lumber has been gathered."
				axe = axe - 1
				wood = wood + 10
				aaa = raw_input("Press ENTER to resume...")
		if rand == 1:
			print a 
			camplog = camplog + 1
			print "Your scouting crew discovered a pillar of smoke in the distance. (Recorded in Scoutbook)"
			aaa = raw_input("Press ENTER to resume...")
	if choice == "help":
		print a
		##Options here -- Menu Commands
		print "quit: Exits the game. Don't worry, it saves."
		print ""
		print "hunt: This can be used to hunt animals. Using ammo will increase the amount of meat, but you can hunt without weapons for a lesser amount."
		print "scout: Use this command to scout the area for other survivors, resources, or camps"
		print "raid: Used to raid scouted out camps. Be aware of your resources however."
		print "make: This opens up the crafting menu."
		print "manage: This opens up quarries, camp, and defense manager."
		print "vault: Use this to check how many resources you have."
		print "radio: Used to check for survivors."
		print "people: Opens the people manager."
		choice = raw_input("Press ENTER to resume...")