def divide_states(height, weight):
    img=''
    standard_weight = (height-100)*0.85
    rate = round(weight/standard_weight*100,2)
    
    if rate <= 90: img = 'under'
    elif rate>90 and rate<=110: img = 'normal'
    elif rate>110 and rate<=120: img = 'over'
    else: img = 'obese'
        
    return img, rate