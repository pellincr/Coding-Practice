import time
#wait: func int -> func
#purpose: to execute the given function after n milliseconds
def wait(func,n):
    print("Function will take " + str(n/1000) + " seconds to complete")
    time.sleep(n/1000)
    return func

#test_wait(): ->
#purpose: to test the wait function
def test_wait():
    x = lambda a: a + 1
    assert wait(x(5), 5000) == 6

if __name__ == "__main__":
    test_wait()
    print("All tests have succeeded!")