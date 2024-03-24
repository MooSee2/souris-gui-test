from souris_gui_test.components import data_layer as dl


def test_make_dropdown_options():
    input_data = {
        ("Long Creek near Estevan", "05NB001", "Rivers"),
        ("Souris River below Rafterty", "05NB036", "Rivers"),
        ("Yellowgrass Ditch", "05NB011", "Rivers"),
    }

    expected = [
        {"label": "Long Creek near Estevan", "value": "05NB001", "group": "Rivers"},
        {"label": "Souris River below Rafterty", "value": "05NB036", "group": "Rivers"},
        {"label": "Yellowgrass Ditch", "value": "05NB011", "group": "Rivers"},
    ]

    output = dl.make_dropdown_options(input_data)
    assert output == expected
