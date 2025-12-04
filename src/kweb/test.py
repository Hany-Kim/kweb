import klayout.db as db

layout = db.Layout()
layout.dbu = 0.001

top = layout.create_cell("TOP")
layer1 = layout.layer(db.LayerInfo(1, 0))
layer2 = layout.layer(db.LayerInfo(1, 1, 'layer2')) # @param 레이어 번호, 데이터타입 데이터 타입 수, 이름

box1 = db.Box(-5000, -2500, 5000, 2500)
box2 = db.Box(-25000, -50000, 25000, 50000)
box21 = db.Box(-50000, -25000, 50000, 25000)
top.shapes(layer1).insert(box1)
top.shapes(layer2).insert(box2)
top.shapes(layer2).insert(box21)

layout.write("C:\\gds\\test.gds")