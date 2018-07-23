import re


def get_case_and_result(line):
    pattern = 'Case #(\d+):\s(.*)'
    match = re.match(pattern, line)
    return int(match.group(1)), [int(i) for i in match.group(2).split()]


def process_input(main_f, input_file, output_file=None):
    file = open(input_file)
    output_file = output_file or input_file + '.output'
    output = open(output_file, 'w')

    t = int(file.readline())
    for i in range(1, t+1):
        args = [int(i) for i in file.readline().split()]
        info = 'Case #{}: {}'.format(i, main_f(*args))
        print(info)
        output.write(info+'\n')


def small_input_validation(main_f, input_file, result_file):
    input_f = open(input_file)
    result_file = result_file or result_file + '.output'
    result_f = open(result_file)

    error_case = 0

    input_f.readline()

    for line, res in zip(input_f, result_f):
        arg = [int(i) for i in line.split()]
        case, result = get_case_and_result(res)
        if len(result) == 1: result = result[0]

        f_result = main_f(*arg)

        if f_result != result:
            print('case {} is wrong, except {} got {}'.format(case, result, f_result))
            print('\t\targs : {}'.format(arg))
            error_case += 1

    input_f.close()
    result_f.close()
    print('test finished, there are {} error[s]'.format(error_case))


assert get_case_and_result('Case #10: 10 20') == (10, [10, 20])
assert get_case_and_result('Case #9: 10 1') == (9, [10, 1])
assert get_case_and_result('Case #9: 10') == (9, [10])

