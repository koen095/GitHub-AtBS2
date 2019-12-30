
# Password string should be atleast 8 characters long
# Should contain both uppercase, lowercase and atleast one digit

passRegex = re.compile(r'''
    [a-zA-Z0-9]


    ''', re.VERBOSE)

password = input('input your preferred password')
