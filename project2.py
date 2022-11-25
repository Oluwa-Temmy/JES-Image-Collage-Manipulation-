#---------------------------------------------------------
def scale(pictIn, factor):
  pictOut = makeEmptyPicture(int(getWidth(pictIn) * factor), int(getHeight(pictIn) * factor))
  inX = 0
  for outX in range(0, int(getWidth(pictIn) * factor)):
    inY = 0
    for outY in range(0, int(getHeight(pictIn) * factor)):
      color = getColor(getPixel(pictIn, int(inX), int(inY)))
      setColor(getPixel(pictOut, outX, outY), color)
      inY = inY + 1.0 / factor
    inX = inX + 1.0 / factor
  return pictOut

#-------------------------------------------------------------   
def copy(source, srcXB, srcYB, srcXE, srcYE, target, targXB, targYB):
  #Based on Program 30 in Guzdial & Ericson text 
  targetX = targXB
  for sourceX in range(srcXB, srcXE):
    targetY = targYB
    for sourceY in range(srcYB, srcYE):
      srcPx = getPixel(source, sourceX, sourceY)
      targPx = getPixel(target, targetX, targetY)
      setColor(targPx, getColor(srcPx))
      targetY = targetY + 1
    targetX = targetX + 1
    
def copyQRT(picture,newpic,k,old_x,old_y,new_x,new_y):
  in_x = new_x
  for x in range(old_x, old_x + getWidth(picture) / k):
    in_y = new_y 
    for y in range(old_y, old_y + getHeight(picture) / k):
      pixel = getPixel(picture, x, y)
      newPixel = getPixel(newpic,in_x,in_y)
      setColor(newPixel, getColor(pixel))
      in_y = in_y + 1
    in_x = in_x + 1
#----------------------------------------------------------
def cynotype(picture):
  grayScale(picture)          
  for p in getPixels(picture):
    rV = getRed(p)       
    if red < 100:
      rV = rV * 2.5    
    elif rV < 192:
      rV = rV * .5  
    else: 
      rV = rV * 1.2  
    setRed(p,rV)      
    setBlue(p,getBlue(p) *.60)
    setGreen(p,getGreen(p) *.60)
    
def cynotypeA(picture):
  grayScale(picture)          
  for p in getPixels(picture):
    rV = getRed(p)       
    if red < 150:
      rV = rV * .5
    elif rV < 192:
      rV = rV * .5  
    else: 
      rV = rV * 1.2  
    setRed(p,rV)      
    setBlue(p,getBlue(p) *.20)
    setGreen(p,getGreen(p) *.20)
  #repaint(picture)
#-------------------------------------------------------------
def grayScale(picture):
  for p in getPixels(picture):
    intensity = (getRed(p)+getGreen(p)+getBlue(p))/3
    setColor(p,makeColor(intensity,intensity,intensity))
    
def grayScalet(picture):
  for p in getPixels(picture):
    intensity = (getRed(p)+getGreen(p)+getBlue(p))/2
    setColor(p,makeColor(intensity,intensity,intensity))
  #repaint(picture)
#------------------mod--------------------------------
def swap(picture):
  for p in getPixels(picture):
    redd = getRed(p)
    bluee = getBlue(p)
    greenn = getGreen(p)
    avr = (redd+bluee+greenn)/2
    if redd >= 100:
      setColor(p,makeColor(128,0,0))
    if bluee <= 40:
      setColor(p,makeColor(139,58,58))
    if greenn >= 100:
      setColor(p,makeColor(avr))
      
def swapRD(picture):
  for p in getPixels(picture):
    redd = getRed(p)
    bluee = getBlue(p)
    greenn = getGreen(p)
    avr = (redd+bluee+greenn)/7
    if redd >= 100:
      setColor(p,makeColor(128,0,0))
    if bluee <= 40:
      setColor(p,makeColor(28,28,28))
    if greenn >= 100:
      setColor(p,makeColor(avr))
  #repaint(picture)
#-----------------------------------------------------
def mirrorLeft(picture):
#program 66
  width = getWidth(picture)
  eMirror = width / 2
  for x in range(0, eMirror):
    for y in range(0, getHeight(picture)):
      leftPixels = getPixel(picture,width - x-1,y)
      rightPixels = getPixel(picture, x,y)
      setColor(rightPixels, getColor(leftPixels))
      
def mirrorRight(picture,f):
#program 66
  width = getWidth(picture)
  eMirror = width / f
  for x in range(0,eMirror):
    for y in range(0, getHeight(picture)):
      leftPixels = getPixel(picture,x,y)
      rightPixels = getPixel(picture, width - x-1,y)
      setColor(rightPixels, getColor(leftPixels))
#-------------------------------------------------------------
def luminance(pixel):
  r = getRed(pixel)
  g = getGreen(pixel)
  b = getBlue(pixel)
  return (r+g+b)/3

def edgeDetect(source,k):
  purple = makeColor(104,34,139)
  redd = makeColor(139,10,10)
  for px in getPixels(source):
    x = getX(px)
    y = getY(px)
    if y < getHeight(source)-1 and x < getWidth(source)-1:
      botrt = getPixel(source,x+1,y+1)
      thislum = luminance(px)
      brlum = luminance(botrt)
      if abs(brlum-thislum) > k:
        setColor(px,redd)
      if abs(brlum-thislum) <= k:
        setColor(px,black)
        
def edgeDetectTwo(source,k):
  purple = makeColor(128,0,0)
  for px in getPixels(source):
    Re = getRed(px)
    Bl = getBlue(px)
    Gr = getGreen(px)
    RBG = (Re+Bl+Gr)/10
    x = getX(px)
    y = getY(px)
    if y < getHeight(source)-1 and x < getWidth(source)-1:
      botrt = getPixel(source,x+1,y+1)
      thislum = luminance(px)
      brlum = luminance(botrt)
      if abs(brlum-thislum) > k:
        setColor(px,purple)
      if abs(brlum-thislum) <= k:
        setColor(px,makeColor(RBG))
#-----------------------------------------------------  
def border(source):
  bottom = getHeight(source)-5
  top = getWidth(source)-5
  for px in getPixels(source):
    color = makeColor(((getRed(px)/4)+(getBlue(px)/4)+(getGreen(px)/4))/4)
    y = getY(px)
    x = getX(px)
    if y < 5:
      setColor(px,color)
    if y > bottom:
      setColor(px,color)
    if x < 5:
      setColor(px,color)
    if x > top:
      setColor(px,color)

#------------------------------------------------------  
def dark(picture):
  for x in range(0, getWidth(picture)):
    for y in range(0, getHeight(picture)):
      pixel = getPixel(picture, x, y)
      setColor(pixel,makeDarker(getColor(pixel)))

#---------------------------------------------------
def addSignature(target, signature, toX, toY, color):
  toYStart = toY
  for x in range(0, getWidth(signature)):
    toY = toYStart
    for y in range(0,getHeight(signature)):
      p = getPixel(signature, x, y)
      if (getRed(p) < 225 and getGreen(p) < 225 and getBlue(p) < 225):
        setColor(getPixel(target, toX, toY), color)
      toY = toY + 1
    toX = toX + 1
  return target

#-----------------------------------------------

def collage():
  #Pictures
  setMediaPath("C:\Users\Zerchoel\OneDrive\Desktop\CS Labs\Project2")
  carti = makePicture(getMediaPath("carti_pons.jpg"))
  signature = makePicture(getMediaPath("signature.png"))
  height = getHeight(carti)
  width = getWidth(carti)
  sigW = getWidth(signature)
  sigH = getHeight(signature)
  canvas = makeEmptyPicture(getWidth(carti),getHeight(carti)) 
  
  border(carti)
  
  
  #~~~Orig_BG~~~#
  carti = scale(carti,1)
  copy(carti, 0, 0, getWidth(carti), getHeight(carti), canvas, 0, 0)
  
  #~~~EDGE_DETECT_BottomRight~~~#
  carti1 = scale(carti,0.35)
  widthone = getWidth(carti1)
  heightone = getHeight(carti1)
  edgeDetect(carti1,10)
  copy(carti1, 0, 0, getWidth(carti1), getHeight(carti1), canvas, width - getWidth(carti1)-4, height - getHeight(carti1)-4)
  
  #~~~CYNAOTYPE_TopRight~~~#
  cartifive = scale(carti,0.35)
  widthfive = getWidth(cartifive)
  heightfive = getHeight(cartifive)
  widthfiveL = widthfive/2
  heightfiveL = heightfive/2  
  cynotype(cartifive)
  copy(cartifive, 0, 0, getWidth(cartifive),getHeight(cartifive), canvas, width - getWidth(carti1)-4,4) 
  
   #~~~Light_TopRight~~~#
  carti3 = scale(carti,0.35)
  width3 = getWidth(carti3)
  height3 = getHeight(carti3)
  grayScalet(carti3)
  copy(carti3, 0, 0, getWidth(carti3), getHeight(carti3), canvas, 4,4)
  
  #~~~Cynotype_BottomLeft~~~#
  cartisix = scale(carti,0.35)
  cartsixW = getWidth(cartisix)
  cartisixL = getHeight(cartisix)
  cynotypeA(cartisix)
  copy(cartisix, 0, 0, getWidth(cartisix),getHeight(cartisix), canvas, 5,height - getHeight(carti1)-4)
  
  #~~~GRAYSCALE_BG2~~~#
  carti0 = scale(carti,0.6)
  widthz = getWidth(carti0)
  heightz = getHeight(carti0)
  grayScale(carti0)
  mirrorLeft(carti0)
  copy(carti0, 0, 0, getWidth(carti0),getHeight(carti0), canvas, width/5, height/5)
  
  #~~~SWAP1_TopLeft_BG2~~~#
  carti2 = scale(carti,0.6)
  swap(carti2)
  mirrorLeft(carti2)
  copy(carti2, 0, 0, getWidth(carti2)/2,getHeight(carti2)/2, canvas, width/5, height/5)
  
  #~~~SWAP2_BottomRight_BG2~~~#
  carti4 = scale(carti,.60)
  widthfour = getWidth(carti4)
  heightfour = getHeight(carti4)
  halfwidthfour = widthfour / 2
  halfheightfour = heightfour / 2
  swapRD(carti4)
  copyQRT(carti4,canvas,2,halfwidthfour,halfheightfour,382,365)
  
  #~~~SIGNATURE~~~#
  sigA = scale(signature,.69)
  #addSignature(canvas,sigA,154,333,black)
  copy(sigA, 0, 0, getWidth(sigA), getHeight(sigA), canvas, 154, 333)
  
  #~~~secret_sound~~~#
  #idk how to make it stop playing so just close the program when your done
  #wlr = makeSound(getMediaPath("wlr.wav"))
  #play(wlr)
  
  show(canvas)
  

