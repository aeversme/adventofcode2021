from input_handler import convert_input

with open('test-monad.txt') as m:
    m_raw = m.readlines()

monad = convert_input(m_raw)
print(monad)
