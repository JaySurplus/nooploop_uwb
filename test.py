import nooploop_uwb

uwb = nooploop_uwb.Nooploop_UWB_AOA('config.json')

count = 0
while count < 20000:
    data = uwb.get_data()
    #print(count,  data)
    count += 1

uwb.terminate()