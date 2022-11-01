def sound_morse(minput):
    from time import sleep
    from winsound import Beep
    from data import special_match
    import time
    vinput = special_match(minput)
    if vinput:
        start_time = time.time()
        for m in list(minput):
            print(m, sep=' ', end='', flush=True)
            if m == '.':
                Beep(2000, 500)
            elif m == '=':
                Beep(2000, 1000)
            else:
                sleep(1)
        app_time = time.time() - start_time
        app_time = format(app_time, '.1f')
        print("\nThis message put", app_time, "secondes")