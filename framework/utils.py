def camel_case(string):
    ss = string.split('_')
    return ss[0] + ''.join(s.title() for s in ss[1:])
