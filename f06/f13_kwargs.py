def print_info(**kwargs):
    '''
    딕셔너리로 전달
    :param kwargs:
    :return:
    '''

    for key,value in kwargs.items():
        print(f'{key}:{value}')

print_info(name='이상무',age=21,city='Seoul')

# name:이상무
# age:21
# city:Seoul