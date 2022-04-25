class Rectangle:

  def __init__ (self,x=0,y=0,h=0, w=0):
    self.x = x
    self.y = y
    self.height = h
    self.width = w
    if x < 0:
      self.x = 0
    elif y < 0:
      self.y = 0
    elif h < 0:
      self.height = 0
    elif w < 0:
      self.width = 0

  '''
  Sets up instance variables and sets those instance variables to 0 if they are less than 0.
  Args:
    x[int]: x-coordinate of the rectangle.
    y[int]: y-coordinate of the rectangle.
    h[int]: height of the rectangle.
    w[int]: width of the rectangle.
  Return: 
    None
  '''
	
	

  def __str__(self):
    return str("(x:"+ str(self.x)+ " y:"+  str(self.y)+ ")"+ " width:" + str(self.width)+ ", height:"+ str(self.height) )

  '''
  Returns the instance variables in a string.
  Args:
   None
  Return: 
    [str]: Returns the string that uses the instance variables that were set up in the init function.
  '''