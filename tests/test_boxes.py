from src.souris.core.boxes import Boxes


def test_boxes_round():
    boxes = Boxes(box_1=1.5, box_2=2.5, box_3=2.4, box_4=2.6, box_5a=2, box_6=3.5)
    boxes.round_boxes(0)

    assert boxes.box_1 == 2
    assert boxes.box_2 == 2
    assert boxes.box_3 == 2
    assert boxes.box_4 == 3
    assert boxes.box_5a == 2
    assert boxes.box_6 == 4
