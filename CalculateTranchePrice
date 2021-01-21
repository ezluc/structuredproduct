#Define basic values/inputs
LIBOR = 0.04
a=[[LIBOR + 0.0225, 30, 20000000, 0.04, 0.02, 0.2],
  [0.061, 30, 20000000, 0.06, 0.05, 0.1],
  [0.062, 40, 25000000, 0.06, 0.04, 0.2],
  [LIBOR + 0.025, 40, 20000000, 0.08, 0.01, 0.2],
  [LIBOR + 0.025, 40, 20000000, 0.04, 0.02, 0.2],
  [0.0645, 50, 20000000, 0.05, 0.03, 0.2],
  [0.0679, 50, 25000000, 0.05, 0.05, 0.4],
  [LIBOR + 0.0275, 50, 25000000, 0.04, 0.01, 0.2],
  [LIBOR + 0.0275, 50, 20000000, 0.06, 0.02, 0.2],
  [0.0722, 60, 20000000, 0.08, 0.05, 0.1],
  [LIBOR + 0.03, 60, 40000000, 0.08, 0.03, 0.5],
  [0.0754, 70, 40000000, 0.08, 0.05, 0.5],
  [LIBOR + 0.0325, 70, 20000000, 0.04, 0.02, 0.2],
  [0.0772, 80, 20000000, 0.04, 0.04, 0.2],
  [0.0791, 90, 20000000, 0.03, 0.05, 0.6],
  [LIBOR + 0.0335, 90, 20000000, 0.06, 0.03, 0.5],
  [LIBOR + 0.035, 100, 20000000, 0.08, 0.05, 0.4],
  [0.0812, 110, 25000000, 0.04, 0.03, 0.5],
  [LIBOR + 0.04, 120, 30000000, 0.06, 0.05, 0.5],
  [0.0856, 120, 50000000, 0.08, 0.05, 0.4]
  ]

#Genereat cash flows of interests
def bond_interestpmts(wac, wam, prcp, adr, apr):
    int_flows = []
    balance = prcp
    for quarters in range(120):
        if quarters <= wam:
            defaultedprcp = balance * adr / 4
            interest = balance * wac / 4
            prepaidprcp = balance * apr / 4
            int_flows.append(interest)
            balance = balance - prepaidprcp - defaultedprcp

        else:
            int_flows.append(0)
    return int_flows

individual_interest = 0
sum_interest = []
for t in range(120):
    for i in range(len(a)):
        individual_interest += bond_interestpmts(a[i][0],a[i][1],a[i][2],a[i][3],a[i][4])[t]
    sum_interest.append(individual_interest)
    individual_interest = 0

#Generate Cash flows of Principal
def bond_principalpmts(wam,prcp,adr,apr,lgd):
  balance = prcp
  recovery_rate = 1 - lgd
  prcp_flows = []
  for quarters in range(120):
    if quarters < wam - 1:
        defaulted_prcp = balance * adr / 4
        recovered_prcp = defaulted_prcp * recovery_rate
        prepaid_prcp = balance * apr/4
        total_prcp = prepaid_prcp + recovered_prcp
        prcp_flows.append(total_prcp)
        balance = balance - prepaid_prcp - defaulted_prcp


    elif quarters == wam - 1:

        defaulted_prcp = balance * adr / 4
        scheduled_prcp = balance - defaulted_prcp
        recovered_prcp = defaulted_prcp*(1-lgd)
        total_prcp = recovered_prcp + scheduled_prcp

        prcp_flows.append(total_prcp)

    else:
        prcp_flows.append(0)
  return prcp_flows

individual_prcp = 0                                           #calculate sum principal payments
sum_prcp = []
for t in range(120):
    for i in range(len(a)):
        individual_prcp += bond_principalpmts(a[i][1],a[i][2],a[i][3],a[i][4],a[i][5])[t]
    sum_prcp.append(individual_prcp)
    individual_prcp = 0

def starting_balances(wam, prcp, adr, apr):                   #calculate starting balances for OC test
    balance_flows = []
    balance = prcp
    for quarters in range(120):
        if quarters <= wam:
            defaultedprcp = balance * adr / 4
            prepaidprcp = balance * apr / 4
            balance_flows.append(balance)
            balance = balance - prepaidprcp - defaultedprcp

        else:
            balance_flows.append(0)
    return balance_flows

individual_balance = 0
sum_balance = []
for t in range(120):
    for i in range(len(a)):
        individual_balance += starting_balances(a[i][1], a[i][2], a[i][3], a[i][4])[t]
    sum_balance.append(individual_balance)
    individual_balance = 0

def IC_test(numerator,denominator,trigger):
    if numerator/denominator >= trigger:
        return True
    else:
        return False

def IC_cure(interest,prcpA,prcpB,prcpC,prcpD,rateA,rateB,rateC,rateD,trigger,level):
    if level == 0:
        cure_payment = prcpA - interest / trigger / rateA
        return cure_payment
    elif level == 1:
        Y = prcpA * rateA + prcpB * rateB - interest / trigger
        if Y <= prcpA * rateA:
            cure_payment = Y / rateA
        else:
            cure_payment = prcpA + prcpB - interest / trigger / rateB
        return cure_payment
    elif level == 2:
        Y = prcpA * rateA + prcpB * rateB + prcpC * rateC - interest / trigger
        if Y <= prcpA * rateA:
            cure_payment = Y / rateA
        elif Y <= prcpA * rateA + prcpB * rateB:
            cure_payment = prcpA + prcpB + prcpC * rateC / rateB - interest / trigger / rateB
        else:
            cure_payment = prcpA + prcpB + prcpC - interest / trigger / rateC
        return cure_payment
    else:
        Y = prcpA * rateA + prcpB * rateB + prcpC * rateC + prcpD * rateD - interest / trigger
        if Y <= prcpA * rateA:
            cure_payment = Y / rateA
        elif Y <= prcpA * rateA + prcpB * rateB:
            cure_payment = prcpA + prcpB + prcpC * rateC / rateB + prcpD * rateD - interest / trigger / rateB
        elif Y <= prcpA * rateA + prcpB * rateB + prcpC * rateC:
            cure_payment = prcpA + prcpB + prcpC + prcpD * rateD / rateC - interest / trigger / rateC
        else:
            cure_payment = prcpA + prcpB + prcpC + prcpD - interest / trigger / rateD
        return cure_payment

def OC_test(numerator, denominator, trigger):
    if numerator / denominator >= trigger:
        return True
    else:
        return False

def OC_cure(starting_bal, denominator,trigger):
    cure_payment = denominator - starting_bal/trigger
    return cure_payment


annual_rateA = LIBOR+0.0025
quarter_rateA = annual_rateA/4
annual_rateB = LIBOR+0.0075
quarter_rateB = annual_rateB/4
annual_rateC = LIBOR+0.0150
quarter_rateC = annual_rateC/4
annual_rateD = LIBOR+0.05
quarter_rateD = annual_rateD/4

Tranches = [["A",350000000,quarter_rateA,1.15,1.07],
            ["B",50000000,quarter_rateB,1.12,1.04],
            ["C",35000000,quarter_rateC,1.1,1.02],
            ["D",15000000,quarter_rateD,1.05,1.01],["Unrated",50000000,0.10]]

trancheA_prcp = Tranches[0][1]
trancheA_int = trancheA_prcp * Tranches[0][2]

trancheB_prcp = Tranches[1][1]
trancheB_int = trancheB_prcp * Tranches[1][2]

trancheC_prcp = Tranches[2][1]
trancheC_int = trancheA_prcp * Tranches[2][2]

trancheD_prcp = Tranches[3][1]
trancheD_int = trancheB_prcp * Tranches[3][2]

Principals = [350000000,50000000,35000000,15000000,50000000]

tranches_interests = [[],[],[],[],[]]
tranche_paid_prcp =[[],[],[],[],[]]
tranche_ending_principal=[[],[],[],[],[]]
for t in range(120):#time loop
    start = []
    for n in range(5):                                              #define starting principal balance for each tranche.
        start_prcp = Principals[n]
        start.append(start_prcp)
    remained_int = sum_interest[t]
    int_cash_flow = sum_interest[t]
    starting_balance = sum_balance[t]
    prcp_cash_flow = sum_prcp[t]
    remained_prcp = sum_prcp[t]
    ic_test_denominator = 0
    oc_test_denominator = 0
    for tr in range(4):                                             #tranche loop
        if Principals[tr] > 0:                                  #if current tranche is not retired
            ic_test_denominator += Principals[tr] * Tranches[tr][2] # IC denomitor
            oc_test_denominator += Principals[tr]                   # OC denomitor
            if remained_int > Principals[tr] * Tranches[tr][2]:   #if remaining interest can pay current tranche required interest
                remained_int -= Principals[tr] * Tranches[tr][2]    #remained interest paid to trance principal.
                tranches_interests[tr].append(Principals[tr] * Tranches[tr][2])#record cashflow for current tranche in current quarter.
                if IC_test(int_cash_flow, ic_test_denominator, Tranches[tr][3]):#then we do IC test
                    remained_int = remained_int                 ##if IC pass, do nothing to the remaining interest and continue to OC test.
                    if OC_test(starting_balance, oc_test_denominator, Tranches[tr][4]):#OC test
                        remained_int = remained_int                 #if pass do nothing to the remaining interest and continue to next tranche.
                    else:                                       ##if OC failed
                        OC_cure_payment = OC_cure(starting_balance, oc_test_denominator, Tranches[tr][4])#calculate amount of cure required.
                        if remained_int > OC_cure_payment:          #if we have enough interest to cure OC
                            remained_int -= OC_cure_payment         #deduct cure amount from remaining interest
                            for i in range(tr+1):
                                if Principals[i] >= OC_cure_payment:#if current tranche principal larger than cure amount
                                    Principals[i] -= OC_cure_payment#deduct the cure from principal
                                    OC_cure_payment -= OC_cure_payment#OC cure amount disappeared.
                                else:
                                    OC_cure_payment -= Principals[i]#else, cure only the remaining principal of current tranche
                                    Principals[i] -= Principals[i]  #current tranche retired
                        else:                                       #if we do not have enough interest to cure OC
                            for i in range(tr+1):
                                if Principals[i] >= remained_int:   #then when current tranche principal larger than remaining interest
                                    Principals[i] -= remained_int   #pay whatever left in remaining interest to current tranche principal.
                                    remained_int -= remained_int    #remained interest disappeared.
                                else:                               #when current tranche principal smaller than remaining interest
                                    remained_int -= Principals[i]   #remaining interest pay whatever principal left.
                                    Principals[i] -= Principals[i]  #current tranche retired.
                else:                                           ##if IC failed
                    IC_cure_payment = IC_cure(int_cash_flow,trancheA_prcp, trancheB_prcp, trancheC_prcp, trancheD_prcp,
                                              Tranches[0][2],
                                              Tranches[1][2], Tranches[2][2], Tranches[3][2],
                                              Tranches[3][3],tr)    #calculate IC cure amount required.
                    if remained_int > IC_cure_payment:              #if we have enough interest to cure IC
                        remained_int -= IC_cure_payment             #deduct cure amount from remaining interest
                        for i in range(tr + 1):
                            if Principals[i] >= IC_cure_payment:    #if current tranche principal larger than cure amount
                                Principals[i] -= IC_cure_payment    #deduct the cure from principal
                                IC_cure_payment -= IC_cure_payment  #IC cure amount disappeared.
                            else:                                   #current tranche principal smaller than remaining interest
                                IC_cure_payment -= Principals[i]    #remaining interest pay whatever principal left.
                                Principals[i] -= Principals[i]      #current tranche principal disappeared.
                    else:                                           #if we do not have enough interest to cure IC.
                        for i in range(tr + 1):                     
                            if Principals[i] >= remained_int:       #then when current tranche principal larger than remaining interest
                                Principals[i] -= remained_int       #pay whatever left in remaining interest to current tranche principal.
                                remained_int -= remained_int        #remained interest disappeared.
                            else:                                   #when current tranche principal smaller than remaining interest
                                remained_int -= Principals[i]       #remaining interest pay whatever principal left.
                                Principals[i] -= Principals[i]      #current tranche retired.
                    if OC_test(starting_balance, oc_test_denominator, Tranches[tr][4]):#repeat OC test
                        remained_int = remained_int
                    else:
                        OC_cure_payment = OC_cure(starting_balance, oc_test_denominator, Tranches[tr][4])
                        if remained_int > OC_cure_payment:
                            remained_int -= OC_cure_payment
                            for i in range(tr + 1):
                                if Principals[i] >= OC_cure_payment:
                                    Principals[i] -= OC_cure_payment
                                    OC_cure_payment -= OC_cure_payment
                                else:
                                    OC_cure_payment -= Principals[i]
                                    Principals[i] -= Principals[i]
                        else:
                            for i in range(tr + 1):
                                if Principals[i] >= remained_int:
                                    Principals[i] -= remained_int
                                    remained_int -= remained_int
                                else:
                                    remained_int -= Principals[i]
                                    Principals[i] -= Principals[i]
            else:                                             #if remaining interest cannot pay current tranche required
                tranches_interests[tr].append(remained_int)     #record whatever remained interest left as cashflow
                remained_int -= remained_int                    #remaining interest disappeared.
        else:                                             #if current tranche is retired
            tranches_interests[tr].append(0)                    #record 0 as cashflow

    tranches_interests[4].append(remained_int)            #tranche E collect remaing interest after tests and cure, if any.

    for tr in range(4):
        if remained_prcp > Principals[tr]:
            remained_prcp -= Principals[tr]
            Principals[tr] -= Principals[tr]
        else:
            Principals[tr] -= remained_prcp
            remained_prcp -= remained_prcp
    tranche_paid_prcp[4].append(remained_prcp)
    for i in range(4):
        paid = start[i] - Principals[i]
        tranche_paid_prcp[i].append(paid)
        endbalance=Principals[i]
        tranche_ending_principal[i].append(endbalance)
    
    tranche_ending_principal[4].append(Principals[4])


trancheA_interest = tranches_interests[0]
trancheB_interest = tranches_interests[1]
trancheC_interest = tranches_interests[2]
trancheD_interest = tranches_interests[3]
trancheE_interest = tranches_interests[4]

trancheA_principal = tranche_paid_prcp[0]
trancheB_principal = tranche_paid_prcp[1]
trancheC_principal = tranche_paid_prcp[2]
trancheD_principal = tranche_paid_prcp[3]
trancheE_principal = tranche_paid_prcp[4]

trancheA_ending_principal=tranche_ending_principal[0]
trancheB_ending_principal=tranche_ending_principal[1]
trancheC_ending_principal=tranche_ending_principal[2]
trancheD_ending_principal=tranche_ending_principal[3]
trancheE_ending_principal=tranche_ending_principal[4]

#print('Ending Balance of Tranche A:', trancheA_ending_principal)
#print('Ending Balance of Tranche B:', trancheB_ending_principal)
#print('Ending Balance of Tranche C:', trancheC_ending_principal)
#print('Ending Balance of Tranche D:', trancheD_ending_principal)
#print('Ending Balance of Tranche E:', trancheE_ending_principal)

#print("Interest of Tranche A:",trancheA_interest)
#print("Interest of Tranche B:",trancheB_interest)
#print("Interest of Tranche C:",trancheC_interest)
#print("Interest of Tranche D:",trancheD_interest)
#print("Interest of Tranche E:",trancheE_interest)

#print("Principal of Tranche A:",trancheA_principal)
#print("Principal of Tranche B:",trancheB_principal)
#print("Principal of Tranche C:",trancheC_principal)
#print("Principal of Tranche D:",trancheD_principal)
#print("Principal of Tranche E:",trancheE_principal)

#calculate sum of interest payments
trancheA_interest_sum=trancheB_interest_sum=trancheC_interest_sum=trancheD_interest_sum=trancheE_interest_sum=0
for i in range(120):
  trancheA_interest_sum=trancheA_interest_sum+trancheA_interest[i]
  trancheB_interest_sum=trancheB_interest_sum+trancheB_interest[i]
  trancheC_interest_sum=trancheC_interest_sum+trancheC_interest[i]
  trancheD_interest_sum=trancheD_interest_sum+trancheD_interest[i]
  trancheE_interest_sum=trancheE_interest_sum+trancheE_interest[i]

print('Sum of Undiscounted Interest Payments of Tranche A = ',trancheA_interest_sum)
print('Sum of Undiscounted Interest Payments of Tranche B = ',trancheB_interest_sum)
print('Sum of Undiscounted Interest Payments of Tranche C = ',trancheC_interest_sum)
print('Sum of Undiscounted Interest Payments of Tranche D = ',trancheD_interest_sum)
print('Sum of Undiscounted Interest Payments of Tranche E = ',trancheE_interest_sum)

#calculate sum of principal payments
trancheA_principal_sum=trancheB_principal_sum=trancheC_principal_sum=trancheD_principal_sum=trancheE_principal_sum=0
for i in range(120):
  trancheA_principal_sum=trancheA_principal_sum+trancheA_principal[i]
  trancheB_principal_sum=trancheB_principal_sum+trancheB_principal[i]
  trancheC_principal_sum=trancheC_principal_sum+trancheC_principal[i]
  trancheD_principal_sum=trancheD_principal_sum+trancheD_principal[i]
  trancheE_principal_sum=trancheE_principal_sum+trancheE_principal[i]

print('Sum of Undiscounted Principal Payments of Tranche A = ',trancheA_principal_sum)
print('Sum of Undiscounted Principal Payments of Tranche B = ',trancheB_principal_sum)
print('Sum of Undiscounted Principal Payments of Tranche C = ',trancheC_principal_sum)
print('Sum of Undiscounted Principal Payments of Tranche D = ',trancheD_principal_sum)
print('Sum of Undiscounted Principal Payments of Tranche E = ',trancheE_principal_sum)

#calculate average life 
x1=x2=x3=x4=x5=y1=y2=y3=y4=y5=0
for i in range(120):
  x1 = x1 + (i + 1) * trancheA_principal[i]
  x2 = x2 + (i + 1) * trancheB_principal[i]
  x3 = x3 + (i + 1) * trancheC_principal[i]
  x4 = x4 + (i + 1) * trancheD_principal[i]
  #x5 = x5 + (i + 1) * trancheE_principal[i]
  y1 = y1 + trancheA_principal[i]
  y2 = y2 + trancheB_principal[i]
  y3 = y3 + trancheC_principal[i]
  y4 = y4 + trancheD_principal[i]
  #y5 = y5 + trancheE_principal[i]

AVL_trancheA = x1 / y1
AVL_trancheB = x2 / y2
AVL_trancheC = x3 / y3
AVL_trancheD = x4 / y4
#AVL_trancheE = x5 / y5

print("Average Life of Tranche A (in Years):",AVL_trancheA/4)
print("Average Life of Tranche B (in Years):",AVL_trancheB/4)
print("Average Life of Tranche C (in Years):",AVL_trancheC/4)
print("Average Life of Tranche D (in Years):",AVL_trancheD/4)
#print("Average Life of Tranche E (in Years):",AVL_trancheE/4)

#calculate the price
pa=pb=pc=pd=pe=0
da=db=dc=dd=de=1
ya=(LIBOR+0.0125)/4
yb=(LIBOR+0.0250)/4
yc=(LIBOR+0.0350)/4
yd=(LIBOR+0.1)/4
ye=0.2/4
incre=0
for i in range(120):
  da=da*(1+ya)
  pa = pa + (trancheA_interest[i]+trancheA_principal[i])/da
  ya=ya+incre
  
  db=db*(1+yb)
  pb = pb + (trancheB_interest[i]+trancheB_principal[i])/db
  yb=yb+incre
  
  dc=dc*(1+yc)
  pc = pc + (trancheC_interest[i]+trancheC_principal[i])/dc
  yc=yc+incre

  dd=dd*(1+yd)
  pd = pd + (trancheD_interest[i]+trancheD_principal[i])/dd
  yd=yd+incre
  
  de=de*(1+ye)
  pe = pe + (trancheE_interest[i]+trancheE_principal[i])/de

#show precentage  
print('The price of note tranche A is', (pa/Tranches[0][1])*100,'%')
print('The price of note tranche B is', (pb/Tranches[1][1])*100,'%')
print('The price of note tranche C is', (pc/Tranches[2][1])*100,'%')
print('The price of note tranche D is', (pd/Tranches[3][1])*100,'%')
print('The price of note tranche E is', (pe/Tranches[4][1])*100,'%')
