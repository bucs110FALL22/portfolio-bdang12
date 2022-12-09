
class Rectangle:

# init method
  def __init__(self, x, y, h, w):
    self.x = max(0, x)
    self.y = max(0, y)
    self.height = max(0, h)
    self.width = max(0, w)

#  str (self) method
  def __str__(self):
    r = "(x: {}, y: {}) width: {}, height: {}".format(self.x, self.y, self.width, self.height)
    return r

# defining surface class, 
class Surface:
  #instance variables
  # init method
  
  def __init__(self, filename, x, y, h, w):
    self.image = filename
    self.rect = Rectangle(x, y, h, w)

  # get rectangle method
  def getRect(self):
    return self.rect
def main():
  #Rectangle Test 

  r = Rectangle(10, 10, 10, 10)
  assert((r.x, r.y, r.height, r.width) == (10,10,10,10))
  r = Rectangle(-1, 1, 1, 1)
  assert((r.x, r.y, r.height, r.width) == (0,1,1,1))
  r = Rectangle(1, -1, 1, 1)
  assert((r.x, r.y, r.height, r.width) == (1,0,1,1))
  r = Rectangle(1, 1, -1, 1)
  assert((r.x, r.y, r.height, r.width) == (1,1,0,1))
  r = Rectangle(1, 1, 1, -1)
  assert((r.x, r.y, r.height, r.width) == (1,1,1,0))

  print(r)
  print("Test Complete!")

   #Surface Class Test
  
  s = Surface("myimage.png", 10, 10, 10, 10)
  assert((s.rect.x, s.rect.y, s.rect.height, s.rect.width)    == (10,10,10,10))
  srect = s.getRect()
  assert(srect.x,  s.getRect().y, srect.height,               srect.width) == (10,10,10,10)
  assert s.image 
 
  print("Test Complete!")

main()