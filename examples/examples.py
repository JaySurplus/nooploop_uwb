from nooploop_uwb import aoa


if __name__ == '__main__':

    UWB_AOA = aoa.AOA('config.json')
    try:
        while True:
            print(UWB_AOA)
    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
        UWB_AOA.terminate()