DEV_HOST = '0.0.0.0'
DEV_PORT = 5000

if __name__ == '__main__':

    import os
    from app import app, app_mode

    if app_mode == 'Development':
        extra_dirs = ['app/client/mock',]
        extra_files = extra_dirs[:]
        for extra_dir in extra_dirs:
            for dirname, dirs, files in os.walk(extra_dir):
                for filename in files:
                    filename = os.path.join(dirname, filename)
                    if os.path.isfile(filename):
                        extra_files.append(filename)

    app.run(host=DEV_HOST, port=DEV_PORT, extra_files=extra_files)
