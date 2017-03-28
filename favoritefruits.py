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