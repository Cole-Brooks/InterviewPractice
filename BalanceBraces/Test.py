# test list generated via chatgpt.
import BalanceBraces

test_cases = [
    ("()", True),
    ("(", False),
    ("([{}])", True),
    ("([{})", False),
    ("Hello (world)!", True),
    ("({)} Extra ) text (", False),
    ("({[)]}", False),
    ("", True),
    ("()", True),
    ("[]", True),
    ("{}", True),
    ("()[]{}", True),
    ("(()())", True),
    ("[[]]", True),
    ("{{{{}}}}", True),
    (")(", False),
    (")()(", False),
    ("]]", False),
    ("[[", False),
    ("{{}", False),
    ("{[}]", False),
    ("[({})]", True),
    ("[({)}]", False),
    ("()()()()()", True),
    ("[[]][]", True),
    ("{}{}{}", True),
    ("[()[]{}]", True),
    ("(()){{}}[[]]", True),
    ("()()()()())", False),
    ("[[]][]]", False),
    ("{}{}{}}", False),
    ("[()[]{}]]", False),
    ("[({[", False),
    ("[({[]})", False),
    ("[({]})", False),
    ("[)", False),
    ("]", False),
    ("{", False),
    ("{}", True),
    ("{[", False),
    ("{[}", False),
    ("{[]}", True),
    ("[{}]", True),
    ("{()}", True),
    ("(){}", True),
    ("({[()]})", True),
    ("({[()]", False),
    ("([)]", False),
    ("({}[)", False),
    ("[{{{{{{}}}}}}]", True),
    ("[[[[[[]]]]]]", True),
    ("{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}", True),
    ("[[]][][[[[]]]]", True),
    ("[({[()()]})]", True),
    ("[({[()()]})]", True),
    ("[({[()()]})](", False),
    ("[({[()()]})]()", False),
    ("[({[()()]})]()", True),
    ("[({[()()]})]()()", True),
    ("()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()", True),
    ("()()()()()()()()()()()()()()()()()()()()()()()()()()()()()())", False),
    ("[[]][][[]][][[]][][[]][][[]][][[]][][[]][][[]][][[]][][[]][][[]][]", True),
    ("[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()", True),
    ("[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()[({[()()]})]()", False),
    ("[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()[({[()()]})]()(", False),
    ("[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()[({[()()]})]()())", False),
    ("[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()](", False),
    ("[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()]", True),
    ("[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()]()", True),
    ("[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()]())", False),
    ("[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()]()](", False),
    ("[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()]()]()", True),
    ("[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()]()]())", False),
    ("[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()]()]()](", False),
    ("[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()]()]()]()", True),
    ("[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()]()]()]())", False),
    ("[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()]()]()]()](", False),
    ("[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()]()]()]()]()", True),
    ("[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()]()]()]()]())", False),
    ("[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()]()]()]()]()](", False),
    ("[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()]()]()]()]()]()", True),
    ("[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()]()]()]()]()]())", False),
    ("[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()]()]()]()]()]()](", False),
    ("[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()]()]()]()]()]()]()]()", True),
    ("[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()]()]()]()]()]()]()]())", False),
    ("[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()]()]()]()]()]()]()]()](", False),
    ("[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()]()]()]()]()]()]()]()]()]()", True),
    ("[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()[({[()()]})]()()]()]()]()]()]()]()]()]()]()]())", False)
]

def main():
    verbose = True
    num_passed = 0

    braceBalancer = BalanceBraces.BraceBalancer()
    
    print("Running Tests:")
    print("----------------- Start Test -----------------")
    passed_all = True
    for test in test_cases:
        test_string = test[0]
        answer = braceBalancer.areBracesBalanced(test_string)
        expected_answer = test[1]
        passed = True if expected_answer == answer else False
        pass_string = "PASSED"
        if not passed:
            passed_all = False
            pass_string = "FAILED"
        else:
            num_passed += 1
        if verbose:
            print("input: {}\n    expected: {}\n    actual: {}\n    {}".format(test_string, expected_answer, answer, pass_string))
    print("----------------- End Test -----------------")
    if passed_all:
        print("All tests passing!")
    else:
        print("FAILURES OCCURRED")
    print("Passed {} / {}".format(num_passed, len(test_cases)))

if __name__=="__main__":
    main()