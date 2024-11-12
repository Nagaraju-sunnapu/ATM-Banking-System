from ATMEXCEPT import DepositError,WithdrawError,InSuffFundError
bal=500.00 # global variable
def deposit():
    damt=float(input("enter the deposit amount: ")) # implicitly raises ValueError in the case of alnums,str and symbols
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("ur account xxxxxxxxx123 credited with INR:{}".format(damt))
        print("Now ur  account xxxxxxxxx123 current bal in INR:{}".format(bal))
def withdraw():
    global bal
    wamt = float(input("enter the withdraw amount: "))  # implicitly raises ValueError in the case of alnums,str and symbols
    if(wamt<=0):
        raise WithdrawError
    elif(bal<(wamt+500)):
        raise InSuffFundError
    else:
        bal=bal-wamt
        print("ur account xxxxxxxxx123 debited with INR:{}".format(wamt))
        print("Now ur account xxxxxxxxx123 current bal in INR:{}".format(bal))
def Balenq():
    print("Now ur account xxxxxxxxx123 current bal in INR:{}".format(bal))








