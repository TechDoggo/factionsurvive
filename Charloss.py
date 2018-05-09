import os 
import random
delpath = (random.choice(glob.glob("/home/runner/charsheet/*.py")))
delpath2 = delpath
sendpath = "/home/runner/Char_dump/"+delpath2
os.renames(delpath,"/home/runner/peel.py")
smithingskill = int(smithingskill)
combatskill = int(combatskill)
geologyskill = int(geologyskill)
miningskill = int(miningskill)
huntingskill = int(huntingskill)
huntingbonus = huntingbonus - huntingskill
smithingbonus = smithingbonus - smithingskill
combatbonus = combatbonus - combatskill
geologybonus = geologybonus - geologyskill
miningbonus = miningbonus - miningskill
os.renames("/home/runner/peel.py",sendpath)