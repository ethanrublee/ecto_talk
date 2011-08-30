fname = 'webcam_circles.txt'
hl = [((_('(detect = [^\)]+\))', green, bold)),
       (_("(detect\[['\w\s,]+\])+", green)))]

after = r'Plasm\(\)'
until = 'if __name__'
