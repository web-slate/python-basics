failures = 0

def flag_failure():
    global failures
    failures = (failures or 0) + 1

def failure_count():
    return failures

def solution_title(title):
    print('=' * 70)
    print(f'>>> {title}')
    print('=' * 70)

def print_and_assert(function_name, param, expected):
    try:
        assert function_name(param) == expected
        print(f'✅ Pass: {function_name.__name__}({param}) is returning {expected} as expected')
    except AssertionError:
        flag_failure()
        print(f'❌ AssertionError: {function_name.__name__}({param}) is returning {function_name(param)} but `{expected}` is expected')

def print_and_assert_new(function_name, *params, expected):
    try:
        assert function_name(*params) == expected
        print(f'✅ Pass: {function_name.__name__}{params} is returning {expected} as expected')
    except AssertionError:
        flag_failure()
        print(f'❌ AssertionError: {function_name.__name__}{params} is returning {function_name(*params)} but `{expected}` is expected')
     
def getTestResult(testName):
    if (failure_count() > 0):
        print(f"{failure_count()} Failure in {testName} tests")
    else:
        print(f"{testName} tests are passed!")