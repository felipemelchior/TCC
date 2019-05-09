import sys

cont = 2000
for i in range(int(sys.argv[1])):
	print("MainRule \"str:{}teste\" \"msg: {}teste\" \"mz:ARGS|URL|BODY|$HEADERS_VAR:Cookie\" \"s:$XSS:8\" id:{};".format(cont,cont,cont))
	cont += 1
