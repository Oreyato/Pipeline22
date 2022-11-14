from shotgun_api3 import shotgun
from manager import conf

sg = None


def get_shotgun():
    global sg

    if sg is None:
        sg = shotgun.Shotgun(conf.sg_link,
                             login=conf.sg_login,
                             password=conf.sg_key)

    return sg


# v =============================================================╗
# v Tests                                                        ║

if __name__ == '__main__':
    sg = get_shotgun()
    print(sg)

    pass

# ^ Tests                                                        ║
# ^ =============================================================╝