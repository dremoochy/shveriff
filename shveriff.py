from argparse import *
import hashlib as h
parser = ArgumentParser(
    prog="python3 mdverify.py",
    description="A simple python script to verify the integrity of a file",
    epilog="Coded by dremoochy"
)
parser.add_argument('-hm','--hashmode',action="store_true",help='compare blank hashes of two files')
parser.add_argument('-fh','--filemode',action="store_true",help='compare file to blank hash')
parser.add_argument('-m','--mode',help='choose the hashing mode (default hashing mode is md5)', choices=h.algorithms_available,default="md5")
parser.add_argument('hashOne')
parser.add_argument('hashTwo')
args = parser.parse_args()
print("Calculating...")
if not(args.hashmode and args.filemode):
    TrueFlag = 0
    if args.hashmode :
        print("First selected hash (using {0}) : {1}".format(args.mode,args.hashOne))
        print("Second selected hash : (using {0}) : {1}".format(args.mode,args.hashTwo))
        TrueFlag = args.hashOne == args.hashTwo
    elif args.filemode:
        with open(args.hashOne,'rb') as first:
            hm = h.file_digest(first, args.mode)
            print("First file hash (using {0}) : {1}".format(args.mode,hm.hexdigest()))
            print("Selected hash : (using {0}) : {1}".format(args.mode,args.hashTwo))
            TrueFlag = hm.hexdigest() == args.hashTwo
    else : 
        with open(args.hashOne,'rb') as first, open(args.hashTwo,'rb') as second:
            hm1 = h.file_digest(first, args.mode)
            hm2 = h.file_digest(second, args.mode)
            print("First file hash (using {0}) : {1}".format(args.mode,hm1.hexdigest()))
            print("Second file hash (using {0}) : {1}".format(args.mode,hm2.hexdigest()))
            TrueFlag = hm1.hexdigest() == hm2.hexdigest()
    print("Hash values are identical!") if TrueFlag else print("Hash values are NOT identical!")
else: print("You must only use -fh or -hm but not -fh and -hm")