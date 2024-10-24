from notes import Animal

#testing classes notes :3
def test_get_name():
    testanimal = Animal("bobbert", "snake", 999999999, "male" , "epic")
    name = testanimal.get_name()
    assert name == "bobbert"