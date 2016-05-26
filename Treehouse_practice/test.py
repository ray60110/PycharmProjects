def trytry():
    try:
        print(100/0)
        print('no exception')
    except:
        print('exception')
    else:
        print('else')
    finally:
        print('final')
    print('normal return')
    return 10

trytry()