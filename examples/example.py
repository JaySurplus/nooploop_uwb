from nooploop_uwb import aoa

if __name__ == '__main__':
    # Create AOA Instance with config.json
    UWB_AOA = aoa.AOA('config.json')

    # or create instance by passing port, baudrate parameters.
    # UWB_AOA = aoa.AOA(port='/dev/ttyUSB1', baudrate=9216000)

    try:
        while True:

            # __str__ method.
            print(UWB_AOA)

            # Get data in JSON format.
            json_data = UWB_AOA.get_data_json()

            # Get data in dictionary format.
            dic_data = UWB_AOA.get_data()
            #print(dic_data)

    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
        UWB_AOA.terminate()