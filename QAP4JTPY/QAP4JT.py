#Author: Joey Thomas
#Date(s): Nov. 15 - Nov. 16, 2024
#Description: Program for 'One Stop Insurance Company' to enter and calculate new policy information.

#Required libraries.
import datetime as dt
import sys
import time

#Define constants.
const_file = "const.dat"
claim_file = "claimstorage.dat"


CON_LIS = []
with open(const_file) as file:
    for line in file:
        CON_LIS.append(line.strip())

POL_NUM = int(CON_LIS[0])
BAS_PRE = float(CON_LIS[1])

ADD_DISC_RATE = float(CON_LIS[2])
EXT_LIA_RATE = float(CON_LIS[3])
GLA_COV_RATE = float(CON_LIS[4])
CAR_LOA_RATE = float(CON_LIS[5])
HST_RATE = float(CON_LIS[6])

PRO_FEE = float(CON_LIS[7])

VAL_CHA = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-'")
VAL_CHA_CIT = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-'. ")
VAL_NUM = set("1234567890")
VAL_NUM_CLA = set("1234567890.")
VAL_PRO = ["NL", "NS", "NB", "PE", "QC", "ON", "MB", "SK", "AB", "BC", "NV", "YU", "NT"]
VAL_PAY = ["Full", "Monthly", "Down Pay"]

CUR_DAT = dt.datetime.now()

#Define functions.
def strintvalid(Usr):
    #This function will handle validating the address and postal code, since they both have to contain letters and numbers.
    Letters = 0
    Numbers = 0    
    canibreak = "Y"
    for i in Usr:
        if i in set(VAL_CHA):
            Letters += 1
        elif i in set(VAL_NUM):
            Numbers += 1
    if Letters == 0 or Numbers == 0:
        print("\n   Input Error: Field must contain both letters and numbers.\n")
        canibreak = "N"

    return canibreak


def dspdollar(Val):
    #This one takes the "Val" (int or float) and converts it into a presentable dollar value.
    Val = "${:,.2f}".format(Val)
    return Val


def dspshortdate(Dat):
    #This one formats "Dat" into the short date format of YYYY-MM-DD.
    Dat = dt.datetime.strftime(Dat, "%Y-%m-%d")
    return Dat

def yesnolitretuner(YoN):
    #Function that returns a literal for Yes or No and validates it at the same time.
    Status = "OK"
    if YoN == "":
        print("\n   Input Error: Choice cannot be empty.\n")
        Status = "BAD"
    elif YoN != "Y" and YoN != "N":
        print("\n   Input Error: Choice must be a Y or a N.\n")
        Status = "BAD"
    
    if YoN == "Y":
        YoNLit = "Yes"
    elif YoN == "N":
        YoNLit = "No" 
    else:
        YoNLit = ""
        Status = "BAD"

    return YoNLit, Status
    

def ProBar(iteration, total, prefix='', suffix='', length=30, fill='█'):
    #This function generates and displays a progress bar with % complete at the end.
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()
      
#Main program start.
while True:
    print()
   #User input.
    while True:
        CusFir = input("Enter Customer First Name: ").title()
        if CusFir == "":
            print("\n   Input Error: First name cannot be empty.\n")
        elif set(CusFir).issubset(VAL_CHA) == False:
            print("\n   Input Error: First name cannot contain invalid characters.\n")
        else:
            break

    while True:
        CusLas = input("Enter Customer Last Name: ").title()
        if CusLas == "":
            print("\n   Input Error: Last name cannot be empty.\n")
        elif set(CusLas).issubset(VAL_CHA) == False:
            print("\n   Input Error: Last name cannot contain invalid characters.\n")
        else:
            break

    print()
    CusFul = f"{CusFir} {CusLas}"

    while True:
        CusAdd = input("Enter Customer's Address: ").title()
        if CusAdd == "":
            print("\n   Input Error: Address cannot be empty.\n")
        elif strintvalid(CusAdd) == "Y":
            break

    while True:
        CusCit = input("Enter Customer's Residing City: ").title()
        if CusCit == "":
            print("\n   Input Error: City cannot be empty.\n")
        elif set(CusCit).issubset(VAL_CHA_CIT) != True:
            print("\n   Input Error: City cannot contain invalid characters.\n")
        else:
            break

    while True:
        CusPro = input("Enter Customer's Residing Province (XX): ").upper()
        if CusPro == "":
            print("\n   Input Error: Customer province cannot be empty.\n")
        elif CusPro not in VAL_PRO:
            print("\n   Input Error: Customer province cannot be invalid.\n")
        else:
            break
    
    while True:
        CusPos = input("Enter Customer Postal Code (X#X#X#): ").upper()
        if CusPos == "":
            print("\n   Input Error: Customer postal code cannot be empty.\n")
        elif len(CusPos) != 6:
            print("\n   Input Error: Customer postal code must be 6 characters.\n")
        elif CusPos[0] not in VAL_CHA or CusPos[1] not in VAL_NUM or CusPos[2] not in VAL_CHA or CusPos[3] not in VAL_NUM or CusPos[4] not in VAL_CHA or CusPos[5] not in VAL_NUM:
            print("\n   Input Error: Customer postal code must follow the format provided.\n")
        elif strintvalid(CusPos) == "Y":
            break

    while True:
        CusPho = input("Enter Customer Phone Number (##########): ")
        if CusPho == "":
            print("\n   Input Error: Customer phone number cannot be empty.\n")
        elif len(CusPho) != 10:
            print("\n   Input Error: Customer phone number must be 10 digits.\n")
        elif set(CusPho).issubset(VAL_NUM) != True:
            print("\n   Input Error: Customer phone number can only contain numbers.\n")
        else:
            CusPho = f"({CusPho[0:3]}) {CusPho[3:6]}-{CusPho[6:10]}"
            break
    
    print()
    CusFulAdd = f"{CusAdd} {CusCit}, {CusPro} {CusPos}"

    while True:
        try:
            NumCar = int(input("Enter # of Cars Being Insured: "))
        except:
            print("\n   Input Error: Number of cars cannot be invalid.\n")
        else:
            break

    while True:
        ExtLia = input("Would you like extra liability up to $1,000,000? (Y/N): ").upper()
        LiaValid = yesnolitretuner(ExtLia)
        LiaValidNo1 = LiaValid[0]
        LiaValidNo2 = LiaValid[1]
        if LiaValidNo2 == "BAD":
            continue
        else:
            break

    while True:
        GlaCov = input("Would you like optional glass coverage? (Y/N): ").upper()
        GlaValid = yesnolitretuner(GlaCov)
        GlaValidNo1 = GlaValid[0]
        GlaValidNo2 = GlaValid[1]
        if GlaValidNo2 == "BAD":
            continue
        else:
            break

    while True:
        LoaCar = input("Would you like an optional loaner car? (Y/N): ").upper()
        LoaValid = yesnolitretuner(LoaCar)
        LoaValidNo1 = LoaValid[0]
        LoaValidNo2 = LoaValid[1]
        if LoaValidNo2 == "BAD":
            continue
        else:
            break

    print()

    while True:
        PayMet = input("Would you like to pay in Full, Monthly or Down Pay?: ").title()
        if PayMet not in VAL_PAY:
            print("\n   Input Error: Payment method must be Full, Monthly, or Down Pay.\n")
        else:
            DowPayAmt = 0
            break

    if PayMet == "Down Pay":
        while True:
            try:
                DowPayAmt = float(input("Enter The Down Payment Desired: "))
            except:
                print("\n   Input Error: Down Payment amount cannot be an invalid value.\n")
            else:
                break

    print("\n-----------------------")
    print("| Previous Claim Info |")
    print("-----------------------\n")

    while True:
        #Claim loop.
        while True:
            ClaNum = input("Enter The Claim Number (#####): ")
            if ClaNum == "":
                print("\n   Input Error: Claim number cannot be empty.\n")
            elif len(ClaNum) != 5:
                print("\n   Input Error: Claim number must be 5 digits long.\n")
            elif set(ClaNum).issubset(VAL_NUM) != True:
                print("\n   Input Error: Claim number must only contain numbers.\n")
            else:
                break

        while True:
            try:
                ClaDat = input("Enter The Date of Claim (YYYY-MM-DD): ")
            except:
                print("\n   Input Error: Claim date cannot be invalid, please use the format provided.\n")
            else:
                ClaDat = dt.datetime.strptime(ClaDat, "%Y-%m-%d")
                ClaDat = dspshortdate(ClaDat)
                break

        while True:
            ClaPre = input("Enter The Amount of Previous Claim (####.##): ")
            if ClaPre == "":
                print("\n   Input Error: Previous claim field cannot be empty.\n")
            elif set(ClaPre).issubset(VAL_NUM_CLA) != True:
                print("\n   Input Error: Previous claim field must be only numbers.\n")
            else:
                ClaPre = float(ClaPre)
                ClaPre = dspdollar(ClaPre)
                break

        #Save info to claim_file.
        ClaLis = [ClaNum, " ", str(ClaDat), " ", ClaPre, " "]
        with open(claim_file, "a+") as Storage:
            Iterations = 0
            for Ite in ClaLis: 
                Storage.write(Ite)
                Iterations += 1
                if Iterations == 5:
                    ClaLis.append("\n")

        #Display saving message.
        print()
        TotalIterations = 30
        Message = "Saving Previous Claim Data..."
    
        for i in range(TotalIterations + 1):
            time.sleep(0.1)
            ProBar(i, TotalIterations, prefix=Message, suffix='Complete', length=50)
        print()
    
        Con = input("\nWould you like to enter more data? (Y/N): ").upper()
        if Con != "Y":
            break

    #Processing.
    if ExtLia == "Y":
        LiaCos = EXT_LIA_RATE * NumCar
    else:
        LiaCos = 0

    
    if GlaCov == "Y":
        GlaCos = GLA_COV_RATE * NumCar
    else:
        GlaCos = 0

    if LoaCar == "Y":
        LoaCos = CAR_LOA_RATE * NumCar
    else:
        LoaCos = 0

    ExtCos = LiaCos + GlaCos + LoaCos

    if NumCar > 1:
        CarInsPre = ((NumCar - 1) * (BAS_PRE * ADD_DISC_RATE)) + BAS_PRE
    else:
        CarInsPre = BAS_PRE

    TotInsPre = ExtCos + CarInsPre
    TaxInsPre = TotInsPre * HST_RATE
    TotCos = TotInsPre + TaxInsPre

    if DowPayAmt == 0:
        MonPay = (TotCos + PRO_FEE) / 8
    else:
        MonPay = ((TotCos - DowPayAmt) + PRO_FEE ) / 8

    try:
        PayDat = dt.date(CUR_DAT.year, CUR_DAT.month + 1, 1)
    except:
        if (CUR_DAT.month + 1) > 12:
            PayDat = dt.date(CUR_DAT.year + 1, 1, 1) 
    PayDat = PayDat.strftime("%Y-%m-%d")

    #Output.
    print()
    print()
    print(f"------------------------------------------------------------------------")
    print(f"One Stop Insurance Company -                    Invoice Date: {dspshortdate(CUR_DAT):>10s}")
    print(f"Customer Policy Information                     Policy No:          {POL_NUM:>4d}")
    print(f"------------------------------------------------------------------------")

    print(f" Customer Name: {CusFul:<20s}     Customer Phone: {CusPho:<10s}")
    print(f" Customer Address: {CusFulAdd:<30s}")
    print()
    print(f" # of Cars Insured: {NumCar:>2d}")
    print(f" Extra Liability?:   {LiaValidNo1:<3s}                     Glass Coverage?:       {GlaValidNo1:<3s}")
    print(f" Loaner Car?:        {LoaValidNo1:<3s}                     Payment Method:  {PayMet:>9s}")
    print(f"------------------------------------------------------------------------")
    print(f" Extra Costs:                                                {dspdollar(ExtCos):>10s}")
    print(f" Car Insurance Premium:                                      {dspdollar(CarInsPre):>10s}")
    print(f"                                                             ----------")
    print(f" Subtotal:                                                   {dspdollar(TotInsPre):>10s}")
    print(f" HST @ {HST_RATE:.0%}:                                                  {dspdollar(TaxInsPre):>10s}")
    print(f"                                                             ----------")
    print(f" Total:                                                      {dspdollar(TotCos):>10s}")
    print()
    print(f" Monthly Payment:                                            {dspdollar(MonPay):>10s}")
    print(f" First Payment Date:                                         {PayDat:>10s}")
    print(f"------------------------------------------------------------------------")

    #Display previous claims in a table.
    print(f" Claim #                       Claim Date                        Amount")
    print(f" ----------------------------------------------------------------------")
    with open(claim_file, "r") as Storage:
        for Line in Storage:
            PreCla = Line.split(" ")
            PreCla.__delitem__(3)
            print(f" {PreCla[0]:>5s}                         {PreCla[1]:>10s}                    {PreCla[2]:>10s}")
    print(f" ----------------------------------------------------------------------")
    print()

    #Ask the user if they'd like to continue.
    while True:
        UseCho = input("Would you like to process more policy info? (Y/N): ").upper()
        if UseCho == "":
            print("   Input Error: User choice cannot be empty.")
        elif UseCho != "Y" and UseCho != "N":
            print("   Input Error: User choice must be a Y or a N.")
        else:
            break
        
    if UseCho == "N":
        break
    else:
        continue

#Housekeeping.
print("\nThank you for using my program! Have a great day!\n")