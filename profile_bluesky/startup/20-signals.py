print(__file__)

"""other signals"""

# userCalcs = userCalcsDevice("ioc:", name="userCalcs")

import APS_BlueSky_tools.devices

scans = APS_BlueSky_tools.devices.sscanDevice("xxx:", name="scans")
calcs = APS_BlueSky_tools.devices.userCalcsDevice("xxx:", name="calcs")
calcs.enable.put("Enable")
calc1 = calcs.calc1


if False:       # demo & testing code
    
    def simulate_peak(swait, motor, profile=None, start=-1.5, stop=-0.5):
        if profile is not None:
            simulator = dict(
                gaussian = swait_setup_gaussian,
                lorentzian = swait_setup_lorentzian,
            )[profile]
            kw = dict(
                center = start + np.random.uniform()*(stop-start), 
                width = 0.002 + 0.1*np.random.uniform(), 
                scale = 100000 * np.random.uniform(), 
                noise = 0.05 + 0.1*np.random.uniform())
            simulator(swait, motor, **kw)
        else:
            swait_setup_random_number(swait)

    def both_peaks():
        simulate_peak(calc1, m1, profile="gaussian")
        yield from bp.scan([noisy,], m1, start, stop, 219)
        simulate_peak(calc1, m1, profile="lorentzian")
        yield from bp.scan([noisy,], m1, start, stop, 219)
    
    RE(both_peaks())
