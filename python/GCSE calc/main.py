#cd C:\Computing\Games\GCSE calc
import time

import GCSE_conversion
import grade_calc

input = input('Are you looking to convert grades (Convert), or find grades (Find) >> ')

if input == 'Convert':
    GCSE_conversion.run()
elif input == 'Find':
    grade_calc.run()
else:
    print("That isn't a valid option, please check your spelling.")
    time.sleep(100)