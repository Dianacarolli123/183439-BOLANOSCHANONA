import threading
import time

class Filosofo(threading.Thread):

  def __init__(self, numeros, tenedor):

      threading.Thread.__init__(self)
      self.tenedor = tenedor
      self.numeros = numeros
      self.temporaloral = (self.numeros + 1) % 5


  def come(self):

      print ("El FILOSOFO "+str(self.numeros)+" come")
      time.sleep(2)


  def piensa(self):

      print ("El FILOSOFO "+str(self.numeros)+" piensa")
      time.sleep(2)


  def obtieneTenIzq(self):

      print ("El FILOSOFO "+str(self.numeros)+" obtiene tenedor izquierdo")
      print ("obtiene el tenedor "+str(self.numeros))
      time.sleep(2)
      self.tenedor[self.numeros].acquire()


  def obtieneTenDer(self):

      print ("El FILOSOFO "+str(self.numeros)+" obtiene tenedor derecho")
      time.sleep(2)
      self.tenedor[self.temporaloral].acquire()


  def liberaTenDer(self):

      print ("El FILOSOFO "+str(self.numeros)+" libera tenedor derecho")
      time.sleep(2)
      self.tenedor[self.temporaloral].release()


  def liberaTenIzq(self):

      print ("El FILOSOFO "+str(self.numeros)+" libera tenedor izquierdo")
      time.sleep(2)
      self.tenedor[self.numeros].release()


  def run(self):

      while(True):
          self.piensa()
          self.obtieneTenIzq()
          self.obtieneTenDer()
          self.come()
          self.liberaTenDer()
          self.liberaTenIzq()


tenedor = [1,1,1,1,1]


for i in range(0, 5):

  tenedor[i] = threading.BoundedSemaphore(1)


for i in range(0, 5):

  t = Filosofo(i, tenedor)
  t.start()
  time.sleep(2)