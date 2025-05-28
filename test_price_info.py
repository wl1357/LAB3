import price_info as h


def test_total_cost_shopping():
    result=h.total_cost_shopping()
    assert(result==46.75)


def test_cost_of_fruit():
    result=h.cost_of_fruits('apple',10)
    assert(result==12)