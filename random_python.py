# ============================================================================== #
#                           Interesting Random Python                            #
#                                   Sean Wade                                    #
# ============================================================================== #

def sqlite():
    import sqlite3
    peopleValues = (
                 ('Ron', 'Obvious', 42),
                 ('Luigi', 'Vercotti', 43),
                 ('Arthur', 'Belling', 28)
               )
    with sqlite3.connect('test_database.db') as connection:
        c = connection.cursor()
        c.execute("DROP TABLE IF EXISTS People")
        c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)") 
        c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)
            # select all first and last names from people over age 30
        c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30") 
    for row in c.fetchall():
        print row

# --------------------------------------------------------------------------------

def stdin():
    ''' 
    Lets you type as much input as you want Ctrl-d to close
    '''
    import sys
    data = sys.stdin.readlines()
    print "Counted", len(data), "lines."

# --------------------------------------------------------------------------------

def optparse():
    import re
    import optparse

    parser = optparse.OptionParser("usage: -w <word> -f <file")
    parser.add_option('-w', dest='word', type='string', help='specify a word to search for')
    parser.add_option('-f', dest='fname', type='string', help='specify file to search')
    (options, args) = parser.parse_args()
    if (options.word == None) | (options.fname == None):
        print parser.usage
        exit(0)
    else:
        word = options.word
        fname = options.fname

    searchFile = open(fname)
    lineNum = 0

    for line in searchFile.readlines():
        line = line.strip('\n\r')
        lineNume += 1
        searchResult = re.search(word, line, re.M|re.I)
        if searchResult:
            print str(lineNum) + ': ' + line

# --------------------------------------------------------------------------------

def templates():
    from string import Template

    cart = []
    cart.append(dict(item='Coke',price=8,qty=2))
    cart.append(dict(item='Cake',price=8,qty=1))
    cart.append(dict(item='Fish',price=32,qty=4))

    t = Template("$qty x $item = $price")
    total = 0
    print "cart:"
    for data in cart:
        print t.substitute(data)
        total += data['price']
    print "Total: " + str(total)

# --------------------------------------------------------------------------------

def argparsing():
    import argparse

    def fib(n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a+b
        return a

    parser = argparse.ArgumentParser()
    parser.add_argument("num", help="The Fibonacci number " + \
            "you wish to calculate", type=int)
    args = parser.parse_args()

    result = fib(args.num)
    print "The" + str(args.num)+"th fib number is " + str(result)


if __name__ == '__main__':
    argparsing()
