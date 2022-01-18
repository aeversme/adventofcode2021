from ..input_handler import convert_input


def setup():
    with open('test-monad.txt') as m:
        m_raw = m.readlines()
    return m_raw


def test_convert_input():
    data_raw = setup()
    data = convert_input(data_raw)

    assert len(data) == 11
    assert data[4] == ['add', 'y', 'w']
