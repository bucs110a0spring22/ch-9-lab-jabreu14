from Rectangle import Rectangle
class Surface:

  def __init__ (self, filename, x, y, h, w):
    self.image = filename
    self.rect = Rectangle(x,y,h,w)


  '''
  Sets up an instance variable for filename and creates a rectangle object that is used in other methods.
  Args:
    filename[str]: Name of the file that is being used.
    x[int]: x-coordinate of the rectangle.
    y[int]: y-coordinate of the rectangle.
    h[int]: height of the rectangle.
    w[int]: width of the rectangle.
  Return: 
    None
  '''
  
  def getRect(self):
    return self.rect

  '''
  Returns the rectangle object
  Args:
   None
  Return: 
    [str]: Returns the rectangle object that was created in the init function.
  '''