print("HOLA SOY NAIJU")
print("SO WHAT KIND OF CAR YOU WANT TO BUY MATE")
num1=input("SEDAN " " SUV\n>")
if num1.upper()=='SEDAN':
    print("WHICH COMPANY DO YOU WANT TO BUY MATE:")
    num2 =input("HUNDAI " " MAHINDRA " " MARUTI SUZUKI " " TATA\n>")
    if num2.upper()=='HUNDAI':
        print("CAN YOU SPECIFY MODAL NAME MATE")
        num3=input("AURA " "VERNA " " ELANTRA\n>")
        if num3.upper()=='AURA':
            num4=input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
            print(num4,"LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
            print("https://www.cardekho.com/hyundai/aura")
        elif num3.upper()=='VERNA':
            num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
            print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
            print("https://www.cardekho.com/hyundai/verna")
        elif num3.upper()=='ELANTRA':
            num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
            print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
            print("https://www.cardekho.com/hyundai/elantra")
        else:
            print("sorry we don't have that information for ",num3)
            exit(0)
    elif num2.upper()=='MAHINDRA':
        print("CAN YOU SPECIFY MODAL NAME MATE")
        num3=input("VERITO " " LOGAN\n>")
        if num3.upper()=='VERITO':
            num4=input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
            print(num4,"LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
            print("https://www.cardekho.com/mahindra/verito")
        elif num3.upper()=='LOGAN':
            num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
            print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
            print("https://www.cardekho.com/hmahindra/logan")
        else:
            print("sorry we don't have that information for ",num3)
            exit(0)
    elif num2.upper()=='MARUTI SUZUKI':
        print("CAN YOU SPECIFY MODAL NAME MATE")
        num3=input("SWIFT " "SWIFT DZIRE " " CLAZ\n>")
        if num3.upper()=='SWIFT':
            num4=input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
            print(num4,"LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
            print("https://www.cardekho.com/maruti/swift")
        elif num3.upper()=='SWIFT DZIRE':
            num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
            print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
            print("https://www.cardekho.com/maruti/swift-dzire")
        elif num3.upper()=='CLAZ':
            num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
            print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
            print("https://www.cardekho.com/maruti/claz")
        else:
            print("sorry we don't have that information for ",num3)
            exit(0)
    elif num2.upper()=='TATA':
        print("CAN YOU SPECIFY MODAL NAME MATE")
        num3=input("TIAGO " "TIGOR " " ALTROZ\n>")
        if num3.upper()=='TIAGO':
            num4=input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
            print(num4,"LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
            print("https://www.cardekho.com/tata/tiago")
        elif num3.upper()=='TIGOR':
            num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
            print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
            print("https://www.cardekho.com/tata/tigor")
        elif num3.upper()=='ALTROZ':
            num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
            print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
            print("https://www.cardekho.com/tata/altroz")
        else:
            print("sorry we don't have that information for ",num3)
            exit(0)
    else:
        print("sorry we don't have that information for ",num2)
        exit(0)
elif num1.upper()=='SUV':
    print("WHICH COMPANY DO YOU WANT TO BUY MATE:")
    num2 = input("HUNDAI " " MAHINDRA " " MARUTI SUZUKI " " TATA " " KIA " " TOYOTA\n>")
    if num2.upper()=='HUNDAI':
            print("CAN YOU SPECIFY MODAL NAME MATE")
            num3 = input("CRETA " "VENUE " " TUSCON " " ALCAZAR\n>")
            if num3.upper() == 'CRETA':
                num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
                print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
                print("https://www.cardekho.com/hyundai/creta")
            elif num3.upper() == 'VENUE':
                num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
                print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
                print("https://www.cardekho.com/hyundai/venue")
            elif num3.upper() == 'TUSCON':
                num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
                print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
                print("https://www.cardekho.com/hyundai/tuscon")
            elif num3.upper() == 'ALCAZAR':
                num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
                print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
                print("https://www.cardekho.com/hyundai/alcazar")
            else:
                print("sorry we don't have that information for ", num3)
                exit(0)
    elif num2.upper()=='MAHINDRA':
            print("CAN YOU SPECIFY MODAL NAME MATE")
            num3 = input("XUV 700 " "XUV 500 " " XUV 300 " " THAR " " SCORPIO " " ALTURAS-G4 " " BOLERO NEO " " BOLERO " " MARAZZO " " KUV 300 NXT \n>")
            if num3.upper() == 'XUV 700':
                num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
                print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
                print("https://www.cardekho.com/mahindra/xuv700")
            elif num3.upper() == 'XUV 500':
                num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
                print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
                print("https://www.cardekho.com/mahindra/xuv500")
            elif num3.upper() == 'XUV 300':
                num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
                print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
                print("https://www.cardekho.com/mahindra/xuv300#leadForm")
            elif num3.upper() == 'THAR':
                num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
                print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
                print("https://www.cardekho.com/mahindra/thar")
            elif num3.upper() == 'SCORPIO':
                num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
                print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
                print("https://www.cardekho.com/mahindra/scorpio")
            elif num3.upper() == 'ALTURAS-G4':
                num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
                print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
                print("https://www.cardekho.com/mahindra/alturas-g4#leadForm")
            elif num3.upper() == 'BOLERO NEO':
                num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
                print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
                print("https://www.cardekho.com/mahindra/bolero-neo")
            elif num3.upper() == 'BOLERO':
                num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
                print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
                print("https://www.cardekho.com/mahindra/bolero-neo")
            elif num3.upper() == 'MARAZZO':
                num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
                print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
                print("https://www.cardekho.com/mahindra/marazzo")
            elif num3.upper() == 'KUV 300 NXT':
                num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
                print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
                print("https://www.cardekho.com/mahindra/kuv-100#leadForm")
            else:
                print("sorry we don't have that information for ", num3)
                exit(0)
    elif num2.upper()=='MARUTI SUZUKI':
                print("CAN YOU SPECIFY MODAL NAME MATE")
                num3 = input("ERTIGA " " VITARA-BREZZA " " S-PRESSO\n>")
                if num3.upper() == 'ERTIGA':
                    num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
                    print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
                    print("https://www.cardekho.com/maruti/ertiga")
                elif num3.upper() == 'VITARA-BREZZA':
                    num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
                    print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
                    print("https://www.cardekho.com/carmodels/Maruti/Maruti_Vitara_Brezza")
                elif num3.upper() == 'S-PRESSO':
                    num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
                    print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
                    print("https://www.cardekho.com/maruti/s_presso")
                else:
                    print("sorry we don't have that information for ", num3)
                    exit(0)
    elif num2.upper()=='TATA':
        print("CAN YOU SPECIFY MODAL NAME MATE")
        num3 = input("PUNCH " "NEXON " " HARRIER " " SAFARI\n>")
        if num3.upper() == 'PUNCH':
            num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
            print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
            print("https://www.cardekho.com/tata/punch")
        elif num3.upper() == 'NEXON':
            num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
            print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
            print("https://www.cardekho.com/tata/nexon")
        elif num3.upper() == 'HARRIER':
            num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
            print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
            print("https://www.cardekho.com/tata/harrier")
        elif num3.upper() == 'SAFARI':
            num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
            print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
            print("https://www.cardekho.com/tata/safarir")
        else:
            print("sorry we don't have that information for ", num3)
            exit(0)
    elif num2.upper()=='KIA':
        print("CAN YOU SPECIFY MODAL NAME MATE")
        num3 = input("SELTOS " " SONET " " CARENS\n>")
        if num3.upper() == 'SELTOS':
            num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
            print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
            print("https://www.cardekho.com/kia/seltos")
        elif num3.upper() == 'SONET':
            num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
            print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
            print("https://www.cardekho.com/kia/SONET")
        elif num3.upper() == 'CARENS':
            num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
            print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
            print("https://www.cardekho.com/kia/CARENS")
        else:
            print("sorry we don't have that information for ", num3)
            exit(0)
    elif num2.upper()=='TOYOTA':
        print("CAN YOU SPECIFY MODAL NAME MATE")
        num3 = input("URBAN CRUSIER " " FORTUNER " " INNOVA CRYSTA\n>")
        if num3.upper() == 'URBAN CRUSIER':
            num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
            print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
            print("https://www.cardekho.com/toyota/urban-cruiser")
        elif num3.upper() == 'FORTUNER':
            num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
            print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
            print("https://www.cardekho.com/toyota/fortuner")
        elif num3.upper() == 'INNOVA CRYSTA':
            num4 = input("HEY! PLEASE EXCUSE ME AND CAN YOU TELL ME YOUR NAME:")
            print(num4, "LINK OF HE CAR AS PER YOUR CHOICE IS GIVEN BELOW!")
            print("https://www.cardekho.com/toyota/innova-crysta")
        else:
            print("sorry we don't have that information for ", num3)
            exit(0)
    else:
        print("sorry we don't have that information for ",num2)
        exit(0)
else:
    print("sorry we don't have that information for ",num2)
    exit(0)
