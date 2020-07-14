from challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_multi_bracket_validation_exist():
    assert multi_bracket_validation


def test_multi_bracket_validation1():
    assert multi_bracket_validation('{}{Code}[Fellows](())')


def test_multi_bracket_validation2():
    assert not multi_bracket_validation('{]{]()')


def test_multi_bracket_validation3():
    assert multi_bracket_validation('({[({[{{}}]})]})[]{()}{}[][]()')


def test_multi_bracket_validation4():
    assert multi_bracket_validation('(aa{b[d(e{   [d{ 55 {66} 78} .fdsgs  ]fs}sdfg)dsf]})fg[sfg]{fth56(h)}6564{h6546h}j[g]vfdd[]dd()')


def test_multi_bracket_validation5():
    assert not multi_bracket_validation('{[(]}')


def test_multi_bracket_validation6():
    assert not multi_bracket_validation('{]{][({test})]')


def test_multi_bracket_validation7():
    assert not multi_bracket_validation('({[}])')
