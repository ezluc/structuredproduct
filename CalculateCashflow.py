#Goal of the project
  #calculate cashflows from interest and principal
  #run waterfall O/C I/C test.
  #repeat process with floating rates
#interest payment function
def interestpmt(WAC,WAM,Prcp,ADR,APR,LGD):
  n = 1
  Balance = Prcp
  Interest = 0
  principalsum=0
  Recoveryrate=1-LGD
  while (n<= WAM):
    Defaultedprcp = Balance * ADR/4
    totalinterest=Interest
    Interest=Balance*WAC/4
    if n == WAM:
      Scheduledprcp = Balance - Defaultedprcp
      Prepaidprcp = 0
    else:
      Scheduledprcp = 0
      Prepaidprcp = Balance * APR/4
    Balance = Balance - (Scheduledprcp + Prepaidprcp) - Defaultedprcp
    Principalpaid=Scheduledprcp+Prepaidprcp+(Defaultedprcp*Recoveryrate)
    Interest = Interest + totalinterest
    principalsum=principalsum+Principalpaid
    n=n+1
  else:
      return Interest


#principal payments function
def principalpmt(WAM,Prcp,ADR,APR,LGD):
  n = 1
  Balance = Prcp
  Interest = 0
  principalsum=0
  Recoveryrate=1-LGD
  while (n<= WAM):
    Defaultedprcp = Balance * ADR/4
    totalinterest=Interest
    if n == WAM:
      Scheduledprcp = Balance - Defaultedprcp
      Prepaidprcp = 0
    else:
      Scheduledprcp = 0
      Prepaidprcp = Balance * APR/4
    Balance = Balance - (Scheduledprcp + Prepaidprcp) - Defaultedprcp
    Principalpaid=Scheduledprcp+Prepaidprcp+(Defaultedprcp*Recoveryrate)
    Interest = Interest + totalinterest
    principalsum=principalsum+Principalpaid
    n=n+1
  else:
      return principalsum
    
#data input
LIBOR=0.04
a=[[LIBOR+0.0225,30,20000000,0.04,0.02,0.2],
   [0.061,30,20000000,0.06,0.05,0.1],
   [0.062,40,25000000,0.06,0.04,0.2],
   [LIBOR+0.025,40,20000000,0.08,0.01,0.2],
   [LIBOR+0.025,40,20000000,0.04,0.02,0.2],
   [0.0645,50,20000000,0.05,0.03,0.2],
   [0.0679,50,25000000,0.05,0.05,0.4],
   [LIBOR+0.0275,50,25000000,0.04,0.01,0.2],
   [LIBOR+0.0275,50,20000000,0.06,0.02,0.2],
   [0.0722,60,20000000,0.08,0.05,0.1],
   [LIBOR+0.03,60,40000000,0.08,0.03,0.5],
   [0.0754,70,40000000,0.08,0.05,0.5],
   [LIBOR+0.0325,70,20000000,0.04,0.02,0.2],
   [0.0772,80,20000000,0.04,0.04,0.2],
   [0.0791,90,20000000,0.03,0.05,0.6],
   [LIBOR+0.0335,90,20000000,0.06,0.03,0.5],
   [LIBOR+0.035,100,20000000,0.08,0.05,0.4],
   [0.0812,110,25000000,0.04,0.03,0.5],
   [LIBOR+0.04,120,30000000,0.06,0.05,0.5],
   [0.0856,120,50000000,0.08,0.05,0.4]
   ]
#main part
suminterestpayments=0
sumprincipalpayments=0
i=0
while i<20:
  interestpayments=interestpmt(a[i][0],a[i][1],a[i][2],a[i][3],a[i][4],a[i][5])
  principalpayments=principalpmt(a[i][1],a[i][2],a[i][3],a[i][4],a[i][5])
  suminterestpayments +=interestpayments
  sumprincipalpayments +=principalpayments
  i+= 1
else:
  print (suminterestpayments)
  print (sumprincipalpayments)
