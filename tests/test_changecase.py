from namespace.package import lowercased, uppercased


def test_uppercased():
    assert uppercased("uppercased") == "UPPERCASED"


def test_lowercased():
    assert lowercased("LOWERCASED") == "lowercased"
