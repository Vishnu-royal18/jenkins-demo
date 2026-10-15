from app import add

result = add(10, 20)

if result == 30:
    print("TEST PASSED")
else:
    raise Exception("TEST FAILED")
