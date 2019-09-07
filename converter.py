def convertbase37(a):
  baselist = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ')
  i = []
  p = 0
  ending = 0
  for letter in a:
    let = baselist.index(letter)
    i.insert(0,let)
  for letter in i:
    ending = ending + (letter * (37 ** p))
    p += 1
  return ending

def convertbase10(a):
  base = 37
  baselist = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ')
  basedict = {'0' : 48, '1': 49, '2':50, '3':51, '4':52, '5':53, '6':54, '7':55, '8':56, '9':57, 'a':97,'b':98,'c':99,'d':100,'e':101,'f':102,'g':103,'h':104,'i':105,'j':106,'k':107,'l':108,'m':109,'n':110,'o':111,'p':112,'q':113,'r':114,'s':115,'t':116,'u':117,'v':118,'w':119,'x':120,'y':121,'z':122,' ':32}
  ending = ""
  try:
    int(a)
  except:
    print("INSERT A NUMBER IDIOT")
    return
  a = int(a)
  while a:
    b = a % base
    a = a // base
    b = baselist[b]
    ending = chr(basedict[b]) + ending
  return(ending)
