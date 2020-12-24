
import time

Naat = '''\tAl-Mualim, We once had a Teacher, The Teacher of teachers, He changed the world for the better,
 And made us better creatures, Oh Allah we’ve shamed ourselves, We’ve strayed from Al-Mu’allim,
 Surely we’ve wronged ourselves, What will we say in front him?, Oh Mu’allim…'''.split(',')


def show_data(Naat):
    for i in range(len(Naat)):
        time.sleep(1)
        print(Naat[i])
    

def main():
    show_data(Naat)


if __name__ == '__main__':
    main()
