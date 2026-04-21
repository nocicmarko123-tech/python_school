import pygame as pg
pg.init()
prozor=pg.display.set_mode((400,400))
prozor.fill(pg.Color("White"))
pg.draw.rect(prozor, pg.Color("Yellow"), (100, 200,200,100))
tacke_krova = [(200, 100), (100, 200), (300, 200)]
pg.draw.polygon(prozor, pg.Color("Red"), tacke_krova, 4)
pg.display.update()
while pg.event.wait().type != pg.quit:
  pass
pg.quit()
