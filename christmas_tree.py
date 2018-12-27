# Sorry I'm not so good at explaning but gonna try

_author = 'Adebayo Ojo Ayowamide'

###################################################

tree = [i*'x' for i in range(30)]   # list of x multiply from 0 to 29
add = len(tree)


def first_half():
    """ First half of Christmas tree"""
    global add
    for i in range(len(tree)):
        half_tree = ((' ' * add) + ('*' * i))  # spaces multiply from 30 to 0 then plus 'x' multiply from 29 to 0
        yield half_tree           # generate full output, if return was used you'll get only the last value
        add -= 1


def second_half():
    """ Second half of Christmas tree"""
    for i in range(len(tree)):
        half_tree = ('*' * i)   # same as what was done in line 1 but not in list
        yield half_tree


def full_tree():
    """ Full christmas tree"""
    first, second = list(first_half()), list(second_half())   # use list to generate output
    for i in range(len(first)):
        a = first[i]            # index first_half value from 0 to 29
        b = second[i]           # index second_half value from 0 to 29
        print(a+b)              # then get them married :)


def leg():
    for i in range(3):
        print(' ' * (len(tree[29]) - 2) + '||')  # half of last tree output multiply with spaces to put the leg exactly
                                                 # in  the middle


if __name__  == '__main__':
    full_tree()
    leg()
