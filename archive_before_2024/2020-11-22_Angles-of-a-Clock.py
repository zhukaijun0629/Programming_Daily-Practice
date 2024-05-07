"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

Given a time in the format of hour and minute, calculate the angle of the hour and minute hand on a clock.
"""
def calcAngle(h, m):
    # Fill this in.
    h_angle = (h+m/60)/12 * 360
    m_angle = m/60 * 360
    angle = abs(h_angle - m_angle)
    return angle if angle <= 180 else 360 - angle


print (calcAngle(3, 30))
# 75
print (calcAngle(12, 30))
# 165
