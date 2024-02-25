import time

NINETY_DEGREE_TIME = 0.33
DT = 0.5

def rotate_ccw_90_deg(m1, m2):
    m1.forward(1)
    m2.backward(1)
    time.sleep(NINETY_DEGREE_TIME)
    m1.stop()
    m2.stop()
    time.sleep(DT)

def rotate_cw_90_deg(m1, m2):
    m1.backward(1)
    m2.forward(1)
    time.sleep(NINETY_DEGREE_TIME)
    m1.stop()
    m2.stop()
    time.sleep(DT)

def rotate_ccw_120_deg(m1, m2):
    m1.forward(1)
    m2.backward(1)
    time.sleep(4*NINETY_DEGREE_TIME/3)
    m1.stop()
    m2.stop()
    time.sleep(DT)

def rotate_cw_120_deg(m1, m2):
    m1.backward(1)
    m2.forward(1)
    time.sleep(4*NINETY_DEGREE_TIME/3)
    m1.stop()
    m2.stop()
    time.sleep(DT)

def move_forward(m1, m2, run_time, s1=1, s2=1):
    m1.forward(s1)
    m2.forward(s2)
    time.sleep(run_time)
    m1.stop()
    m2.stop()
    time.sleep(DT)

def move_backward(m1, m2, run_time, s1=1, s2=1):
    m1.backward(s1)
    m2.backward(s2)
    time.sleep(run_time)
    m1.stop()
    m2.stop()
    time.sleep(DT)