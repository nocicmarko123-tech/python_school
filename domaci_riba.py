import pygame as pg
pg.init()
prozor=pg.display.set_mode((400,400))
prozor.fill(pg.Color("White"))
trougao = pg.draw.polygon(prozor,pg.Color("Yellow"),[(200,100),(200,200),(300,200)])
trougao1 = pg.draw.polygon(prozor,pg.Color("Yellow"),[(200,200),(233,233),(166,233)])
pg.display.update()
while pg.event.wait().type != pg.QUIT:
  pass
pg.QUIT()