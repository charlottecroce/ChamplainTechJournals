import importlib

if input('1. Manual\n2. Auto-Test\n') == '2':
    import pytest
    pytest.main(['--tb=line','-v','-rN'])
else:
    choice = input('Which part do you want to run?\n')
    try:
        if 0 < int(choice) < 15:
            print(f'Running part{choice}:')
            try:
                importlib.import_module(f'part{choice}')
            except Exception as e:
                print('Error in part', choice)
                print(e)
    except:
        print('Choice not recognized')
