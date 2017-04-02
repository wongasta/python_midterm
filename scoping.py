name = 'Simon'
host = 'yixin'

def print_names(n, h):
    local_var = 'Tina'
    print(n+' is a guest')
    print(h+' is a host')

    def organize_string(n, h):
        another_local_var = 'Agnes'
        print(local_var)
        return n + ' is staying at ' + h + ' house'
    print(organize_string(n, h))

# def print_relation(rv):
#     print(rv)

# returned_var = print_names(name, host)
# print(returned_var)
print(print_names(name, host))
# print_relation(returned_var)
# print(local_var)