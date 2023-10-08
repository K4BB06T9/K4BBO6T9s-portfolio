print("""
 List Of Planets :
earth(1),jupiter(2),mars(3)
""")

wgt=float(input("""Pls inform us of ur weight:"""))

planet=float(input("""
Pls select which plant u wanna go:  """))

if planet==1:
   print(wgt*1)
  
elif planet==2:
   print(wgt*2.5270)
  
elif planet==3:
   print(wgt*0.38) 
else:
  print("ur desired planet wasnt included in the list")