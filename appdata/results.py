# (scientific interest, cost, risk)

ratings = {
    'earth': (4.5, 2, 1),
    'mars': (5, 3, 2.5),
    'jupiter': (3.5, 4, 4),
    'moon': (5, 2.5, 2.5),
    'sun': (4, 3, 3.5),
    'saturn': (3.5, 4, 3.5),
    'kbos': (2, 5, 3.5),
    'venus': (2, 3, 3),
    'asteroids':(5, 3.5, 3.5),
    'dwarf': (3, 5, 5),
    'mercury': (2, 3, 3),
    'neptune': (3, 3.5, 3),
    'beyond': (5, 5, 4.5),
    'titan': (4.5, 4, 3.5),
    'halley': (4, 4, 4),
    'uranus': (3, 4, 3),
    
    'earth_obs': (5, None, 1), 
    'cel_body_obs': (5, None, 2),
    'deep_space_obs': (5, None, 2.5),
    'atm_analysis': (5, None, 2),
    'sample_collect': (5, None, 5),
    'telecom': (1.5, None, 1),
    

    'opt_sensor': (None, 3, None),
    'laser_alt': (None, 3, None),
    'radio_sensor': (None, 3, None),
    'microwave': (None, 3, None),
    'infrared': (None, 3, None),
    'ultraviolet': (None, 3, None),
    'x_rays': (None, 3, None),
    'gamma_rays': (None, 3, None),
    'plasma': (None, 4, None),
    'mag': (None, 4, None),
    'grav': (None, 4, None),
    'particles': (None, 4, None),
    'probe': (None, 5, None),
    'amplifier': (None, 3, None),
    'photopolarimeter': (None, 3, None),

    'therm_active': (None, 4, None),
    'therm_passive': (None, 2, None),
    'pow_prim_panels': (None, 2.5, None),
    'pow_prim_rtg': (None, 4, None),
    'pow_sec_batt': (None, 2, None),
    'pow_sec_fc': (None, 2, None),
    'comm_mono': (None, 3.5, None),
    'comm_omni': (None, 2.5, None),
    'aodcs_robust': (None, 5, None),
    'aodcs_simple': (None, 3, None),
    'prop_electr': (None, 4.5, None),
    'prop_chem': (None, 3, None),
    'cdh_standard': (None, 3, None),
    'cdh_optim': (None, 5, None),
    'struct_stand': (None, 3.5, None),
    'struct_high_resist': (None, 5, None),
}

levels = {
    'interest': [None, None, 'You are missing that little huge detail to make it to the next level.',
                 'Nice idea. But other missions could be nicer.', 'Very good! It\'s worth a shot!',
                'Wow! That\'s cool! Better call NASA!'],
    'cost': [None, 'Wow! That\'s convenient... Maybe too much though...',
             'Nice deal!', 'Seems fair.', 'It\'s expensive: I hope we get what we are paying for.',
             'You\'d better bring back some GOOOOOD results for all that money!'],
    'risk': [None, 'Very low-risk... Maybe you should risk more.',
             'Low-risk is good, but it doesn\'t always pay back.',
             'It seems acceptable.',
             'That\'s quite risky, but maybe it is interesting as well.',
             'Wow! That\'s an endeavour!']
}