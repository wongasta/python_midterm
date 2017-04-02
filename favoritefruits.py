import sys, getopt

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "f:", ["fruit="])
    except getopt.GetoptError:
        print ('failed')
        sys.exit(2)
    #print(opts)
    for opt, arg in opts:
        if opt in ('-f', '--fruit'):
            if arg in ('Orange', 'Grape'):
                print(arg + ' is my favorite fruite')
            else:
                print(arg + ' isn\'t my favorite you know')

if __name__ == "__main__":
    main(sys.argv[1:])

#fruit = 'Apple'

#lucky_numbers = [lucky_number, another_lucky_number, one_more_lucky_number]

#print(lucky_numbers)

#print(lucky_numbers['Yixin'])

# for value in unlucky_numbers:
#     print(str(value) + ' is an unlucky number')


# name = 'yixin'
# #season = 'winter'
# if fruit=='Orange':
#     #and name =='yixin') or season=='summer'):
#     print('My favorite!')
# elif name =='yixin':
#     print('My favorite!')
# else:
#     print('I hate it!')





# unlucky_numbers = [14, 24, 92]
# lucky_number = 78
# another_lucky_number = 42
# one_more_lucky_number = 13
# lucky_numbers = {
#     'Yixin': lucky_number,
#     'Simon': another_lucky_number,
#     'Tina': one_more_lucky_number
# }
# for key, value in lucky_numbers.items():
#     print(str(value)+' is lucky number'+' for '+key)
#
# for value in unlucky_numbers:
#     print(str(value) + ' is unlucky number')