def add_string(str1):
    if str1.endswith('python'):
        return str1+'java'
    elif len(str1)<5:
        return str1+'php'
    else:
        return str1+'python'
result=add_string('python')
print(result)
        