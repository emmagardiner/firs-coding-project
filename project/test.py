i = 0

def testEqual(actual, expected, feedback = ""):
    global i
    i += 1
    print "--",
    if type(expected) != type(actual):
        print "Failed test %d: %s\n\ttype of expected and actual don't match" % (i, feedback)
        return False
    if type(expected) == type(1):
        # they're integers, so check if exactly the same
        if actual == expected:
            print'Pass test %d: %s'  % (i, feedback)
            return True
    elif type(expected) == type(1.11):
        # a float is expected, so just check if it's very close, to allow for
        # rounding errors
        if abs(actual-expected) < 0.00001:
            print'Pass test %d: %s'  % (i, feedback)
            return True
    elif type(expected) == type([]):
        if len (expected) != len(actual):
            print "Failed test %d: %s\n\tLengths don't match" % (i, feedback)
            return False
        else:
            for (x, y) in zip(expected, actual):
                if x != y:
                    print "Failed test %d: %s\n\titems in expected and actual do not match" % (i, feedback)
                    return False
            print'Pass test %d: %s'  % (i, feedback)
            return True
    else:
        # check if they are equal
        if actual == expected:
            print'Pass test %d: %s'  % (i, feedback)
            return True
    print 'Failed test %d: %s\n\texpected:\t%s\n\tgot:\t\t%s' % (i, feedback, expected, actual)
    return False

def testType(actual, typeName, feedback = ""):
    global i
    i = i+1
    print "--",
    types = {"string": type(""),
             "dictionary": type({}),
             "list": type([]),
             "int": type(1),
             "float": type(1.0),
             "None": type(None),
             "function": type(lambda x: x)
             }
    if typeName not in types.keys():     
        print('Failed test %d: %s\n\tunknown typeName %s specified.\n\tShould be one of %s' % (i, feedback, typeName, types.keys()))
        return False
    else:
        expected = types[typeName]
    if type(actual) == expected:
        print'Pass test %d: %s'  % (i, feedback)
        return True
    else:
        print('Failed test %d: %s\n\texpected type %s\n\tgot %s' % (i, feedback, expected, type(actual)))
        return False
