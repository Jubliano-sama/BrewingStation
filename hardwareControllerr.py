import time

def pump(volume, direction):
    print('pumping', str(volume), 'ml' , direction)
    time.sleep(2)

def travelTo(pos):
    print('travel to', str(pos))
    time.sleep(2)