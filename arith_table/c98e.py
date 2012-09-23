import argparse
parser = argparse.ArgumentParser(description='Output an arthmetic table.')
parser.add_argument('integer', metavar='N', type=int, help='The number of rows/columns')
parser.add_argument('operand', choices='+-*/', help='The operand to use')

args=parser.parse_args()

n = args.integer
op = args.operand

table = [[0]*(n+1) for i in range(n+1)]
div = ''
run = [i for i in range(n+1)]
for i in range (n+1):
	div += '----'
	for j in range(n+1):
		table[i][j] = eval('%d%s%d'%(i, op, j))
print op, '|', str(run).strip('[]').replace(',',' ')
print div
for i in run:
	print run[i], '|', str(table[i]).strip(',[]').replace(',',' ')
