from ATMMENU import menu
from ATMEXCEPT import DepositError,WithdrawError,InSuffFundError
from ATMOPERATIONS import deposit,withdraw,Balenq
import sys
while(True):
    menu()
    try:
        ch=int(input("enter your choice: "))
        match(ch):
            case 1:
                try:
                    deposit()
                except ValueError:
                    print("\t Don't enter alnums,symbols,str values")
                except DepositError:
                    print("\t Don't deposit negative and zero values")
            case 2:
                try:
                    withdraw()
                except ValueError:
                    print("\t Don't enter alnums,symbols,str values")
                except WithdrawError:
                    print("\t Don't withdraw negative and zero values ")
                except InSuffFundError:
                    print("\t your account xxxxxxxxx123 does not suff funds")
            case 3:
                Balenq()
            case 4:
                sys.exit()
            case _:
                print("your selection of operation is wrong")
    except ValueError:
        print("\t Don't enter alnums,symbols,str and floats as a choice")








