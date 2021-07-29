work_tuesday = False
work_thursday = False

tv_50 = work_tuesday and work_thursday
ice_cream = work_tuesday or work_thursday
tv_32 = work_tuesday != work_thursday
healthier = not ice_cream

print("Tv50={} Tv={} Ice Cream={} Healthier={}"
      .format(tv_50, tv_32, ice_cream, healthier))
