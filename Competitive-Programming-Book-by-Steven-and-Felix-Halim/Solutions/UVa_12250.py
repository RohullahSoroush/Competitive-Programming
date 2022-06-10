# uva_12250
i = 0
while True:
    n = input()
    i += 1
    if n =="#":
        break
    else:
        if n=="HELLO":
            print("Case {0}: {1}".format(i, "ENGLISH"))
        elif n=="HOLA":
            print("Case {0}: {1}".format(i, "SPANISH"))
        elif n=="HALLO":
            print("Case {0}: {1}".format(i, "GERMAN"))
        elif n=="BONJOUR":
            print("Case {0}: {1}".format(i, "FRENCH"))
        elif n=="CIAO":
            print("Case {0}: {1}".format(i, "ITALIAN"))
        elif n=="ZDRAVSTVUJTE":
            print("Case {0}: {1}".format(i, "RUSSIAN"))
        else:
            print("Case {0}: {1}".format(i, "UNKNOWN"))