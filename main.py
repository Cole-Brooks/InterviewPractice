from BalanceBraces.BalanceBraces import BalanceBraces
from BalanceBraces.Inputs import inputs as balance_braces_inputs

def main():
    verbose = False
    num_passed = 0

    braceBalancer = BalanceBraces()
    
    print("Running Balance Braces Tests:")
    print("----------------- Start Test -----------------")
    passed_all = True
    step_id = 0
    for test in balance_braces_inputs.test_cases:
        step_id += 1
        test_string = test[0]
        answer = braceBalancer.are_braces_balanced(test_string)
        expected_answer = test[1]
        passed = (expected_answer == answer)
        pass_string = "PASSED"
        if not passed:
            passed_all = False
            pass_string = "FAILED"
        else:
            num_passed += 1
        if verbose or not passed:
            print("STEP {}\ninput: {}\n    expected: {}\n    actual: {}\n    {}".format(step_id, test_string, expected_answer, answer, pass_string))
            print("-----------------")
    if passed_all:
        print("All tests passing!")
    else:
        print("FAILURES OCCURRED")
    print("Passed {} / {}".format(num_passed, len(balance_braces_inputs.test_cases)))
    print("----------------- End Test -----------------")

if __name__=="__main__":
    main()