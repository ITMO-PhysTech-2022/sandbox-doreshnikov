tasks = {
    'data': {
        'caesar_encode': ['test_basic', 'test_cases'],
        'caesar_decode': ['test_all'],
        'compare': ['test_all'],
        'extract_each': ['test_basic', 'test_cyclic'],
        'merge': ['test_basic', 'test_recursive'],
        'translate_back': ['test_all'],
        'wordcount': ['test_basic', 'test_noise', 'test_large']
    },
    'functions': {
        'bind': ['test_all'],
        'count_calls_until': ['test_all'],
        'generate_json': ['test_all'],
        'mex': ['test_all'],
        'print_tree': ['test_all'],
        'replace_keys': ['test_all'],
        'useless_function': ['test_all'],
        'wtf': ['test_all']
    }
}

with open('template.yaml') as f:
    tmp = f.read()


def camel_case(name):
    words = name.split('_')
    for i in range(len(words)):
        words[i] = words[i][0].upper() + words[i][1:]
    return ''.join(words)


for root, subtasks in tasks.items():
    for fun, tests in subtasks.items():
        for test in tests:
            file = f'tasks/ab/{root}.py'
            test_file = f'test/ab/{root}/test_{fun}.py'
            config_file_name = f'{fun.replace("_", "-")}${test[5:]}.yaml'
            name = f'{root}.py::{fun}/{test}'
            pytest_cmd = f'{test_file}::Test{camel_case(fun)}::{test}'

            if fun == 'caesar_decode':
                test_file = test_file.replace('decode', 'encode')
                pytest_cmd = pytest_cmd.replace('caesar_decode', 'caesar_encode')

            with open(f'out/{config_file_name}', 'w') as cf:
                cf.write(tmp.format(file=file, test_file=test_file, config_file_name=config_file_name,
                                    name=name, pytest_cmd=pytest_cmd, job_name=test))
