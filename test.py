import nooploop_uwb


if __name__ == '__main__':

    UWB_AOA = nooploop_uwb.Nooploop_UWB_AOA('config.json')

    try:
        while True:
            print(UWB_AOA)
    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
        UWB_AOA.terminate()