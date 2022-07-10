import cpuinfo

print('CPU =', cpuinfo.get_cpu_info()['brand_raw'])
