import sys

cont = 1234
for i in range(int(sys.argv[1])):
	print("SecRule ARGS:wtfarg \"@contains {}test\" \"id:{},deny,log,status:403,msg:'Parametro wtfarg com valor {}teste'\"".format(cont,cont,cont))
	cont += 1