import 'pumpy'
import argparse
import time

print('welcome to the program \n')


parser = argparse.ArgumentParser()
subparsers=parser.add_subparsers()

chain = pumpy.Chain('COM1')

p11 = pumpy.Pump(chain,address=2) 

def infuse(args):
	p11.setdiameter(args.diameter)  # mm
	p11.setflowrate(args.flowrate)  ## microL/min
	p11.settargetvolume(args.volume)  ## microL
	p11.infuse()
#	p11.waituntiltarget()
#	p11.stop()

def withdraw(args):
	p11.withdraw()
	time.sleep(3)
	p11.stop()

def infuse_test(args):
	p11.setflowrate(600)
	p11.infuse()
	p11.stop()
	
def withdraw_test(args):
	p11.withdraw()
	p11.stop()

def stop(args):
	p11.stop()

def verbose(args):
	print("there are 5 functions you can use infuse,withdraw,infuse_test,withdraw_test,stop \n")
	print('the standard method of calling any function is the command \n "python infusion.py function -arg " \n')
	print('arguments for infusion function are : \n')
	print('infusion -d: diameter -f flowrate -v target volume \n')
	print('ex: python infusion.py -d 12 -f 200 -v 400 \n')
	print('for rest of the functions arguments are not required')

parser_infuse=subparsers.add_parser('infuse')
parser_infuse.add_argument('-d','--diameter', type=int)
parser_infuse.add_argument('-f', '--flowrate',type=int)
parser_infuse.add_argument('-v','--volume', type=int)
parser_infuse.set_defaults(func=infuse)

parser_withdraw=subparsers.add_parser('withdraw')
parser_withdraw.set_defaults(func=withdraw)

parser_withdraw=subparsers.add_parser('verbose')
parser_withdraw.set_defaults(func=verbose)

parser_infuse_test=subparsers.add_parser('infuse_test')
parser_infuse_test.set_defaults(func=infuse_test)

parser_withdraw_test=subparsers.add_parser('withdraw_test')
parser_withdraw_test.set_defaults(func=withdraw_test)

parser_stop=subparsers.add_parser('stop')
parser_stop.set_defaults(func=stop)

args=parser.parse_args()
args.func(args)