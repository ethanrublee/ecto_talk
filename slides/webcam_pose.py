fname = 'webcam_pose.txt'
hl = [((_('((pose_calc|pose_draw|camera_info) = [^\)]+\))', green, bold)),
       (_("((pose_calc|pose_draw|camera_info)\[['\s\w,]+\])+", green)))]

after = r'Plasm\(\)'
until = 'if __name__'
