from .res_sample import mount as mount_sample


def rest_route(api):
    for mount_res in [
        mount_sample
    ]:
        mount_res(api)
