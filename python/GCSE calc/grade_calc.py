import time

subjects = [
                    'Biology',
                    'Business -- Coursework',
                    'Chemistry',
                    'Computer Science',
                    'DT Food/Textiles -- Coursework',
                    'Drama -- Practical',
                    'English Language',
                    'English Literature',
                    'Engineering -- Coursework',
                    'French',
                    'Geography',
                    'History',
                    'Mathematics',
                    'Music -- Coursework',
                    'Physical Education',
                    'Physics',
                    'Religious Studies',
                    'Science'
            ]

def run():
    subject = input('What subject (Subj for subject list) >> ')
    
    if subject == 'Subj':
        
        for i in subjects:
            print(i)

        run()

    elif subject == 'Biology':
        percentage = input('What percentage of Marks did you score correctly >> ')
        percentage = float(percentage) / 100
        level = input('Did you take the H or F exam >> ')
        marks = percentage * 200

        #Foundation Level
        if marks >= 122 and level == 'F':
            print("You recieved a Grade 5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 101 and level == 'F' and marks < 122:
            print("You recieved a Grade 4. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 72 and level == 'F' and marks < 101:
            print("You recieved a Grade 3. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 44 and level == 'F' and marks < 72:
            print("You recieved a Grade 2. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 16 and level == 'F':
            print("You recieved a Grade 1. If you want to check the A-U equivalent, see the conversion file.")

        #Higher level
        elif marks >= 131 and level == 'H':
            print("You recieved a Grade 9. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 116 and level == 'H' and marks < 131:
            print("You recieved a Grade 8. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 101 and level == 'H' and marks < 116:
            print("You recieved a Grade 7. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 82 and level == 'H' and marks < 101:
            print("You recieved a Grade 6. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 63 and level == 'H' and marks < 82:
            print("You recieved a Grade 5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 45 and level == 'H' and marks < 63:
            print("You recieved a Grade 4. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 36 and level == 'H' and marks < 45:
            print("You recieved a Grade 5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks < 36 and level == 'H':
            print("You did not recieved a Grade.")

    elif subject == 'Business':
        percentage = input('What percentage of Marks did you score correctly >> ')
        percentage = float(percentage) / 100
        marks = percentage * 180

        if marks >= 137:
            print("You recieved a Grade 9. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 127 and marks < 137:
            print("You recieved a Grade 8. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 117 and marks < 127:
            print("You recieved a Grade 7. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 102 and marks < 117:
            print("You recieved a Grade 6. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 88 and marks < 102:
            print("You recieved a Grade 5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 74 and marks < 88:
            print("You recieved a Grade 4. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 52 and marks < 74:
            print("You recieved a Grade 3. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 31 and marks < 52:
            print("You recieved a Grade 2. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 10 and marks < 31:
            print("You recieved a Grade 1. If you want to check the A-U equivalent, see the conversion file.")

    elif subject == 'Chemistry':
        percentage = input('What percentage of Marks did you score correctly >> ')
        percentage = float(percentage) / 100
        level = input('Did you take the H or F exam >> ')
        marks = percentage * 200

        #Foundation Level
        if marks >= 123 and level == 'F':
            print("You recieved a Grade 5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 98 and level == 'F' and marks < 123:
            print("You recieved a Grade 4. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 70 and level == 'F' and marks < 98:
            print("You recieved a Grade 3. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 42 and level == 'F' and marks < 70:
            print("You recieved a Grade 2. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 15 and level == 'F':
            print("You recieved a Grade 1. If you want to check the A-U equivalent, see the conversion file.")

        #Higher level
        elif marks >= 139 and level == 'H':
            print("You recieved a Grade 9. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 118 and level == 'H' and marks < 139:
            print("You recieved a Grade 8. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 98 and level == 'H' and marks < 118:
            print("You recieved a Grade 7. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 78 and level == 'H' and marks < 98:
            print("You recieved a Grade 6. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 58 and level == 'H' and marks < 78:
            print("You recieved a Grade 5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 38 and level == 'H' and marks < 58:
            print("You recieved a Grade 4. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 28 and level == 'H' and marks < 38:
            print("You recieved a Grade 5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks < 28 and level == 'H':
            print("You did not recieved a Grade.") 

    elif subject == 'Computer Science':
        percentage = input('What percentage of Marks did you score correctly >> ')
        percentage = float(percentage) / 100
        marks = percentage * 160

        if marks >= 135:
            print("You recieved a Grade 9. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 121 and marks < 135:
            print("You recieved a Grade 8. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 107 and marks < 121:
            print("You recieved a Grade 7. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 91 and marks < 107:
            print("You recieved a Grade 6. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 75 and marks < 91:
            print("You recieved a Grade 5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 59 and marks < 75:
            print("You recieved a Grade 4. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 44 and marks < 59:
            print("You recieved a Grade 3. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 29 and marks < 44:
            print("You recieved a Grade 2. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 15 and marks < 29:
            print("You recieved a Grade 1. If you want to check the A-U equivalent, see the conversion file.")

    elif subject == 'DT Food/Textiles':
        percentage = input('What percentage of Marks did you score correctly >> ')
        percentage = float(percentage) / 100
        marks = percentage * 100

        if marks >= 80:
            print("You recieved a Grade 9. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 71 and marks < 80:
            print("You recieved a Grade 8. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 62 and marks < 71:
            print("You recieved a Grade 7. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 52 and marks < 62:
            print("You recieved a Grade 6. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 43 and marks < 52:
            print("You recieved a Grade 5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 34 and marks < 43:
            print("You recieved a Grade 4. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 24 and marks < 34:
            print("You recieved a Grade 3. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 14 and marks < 24:
            print("You recieved a Grade 2. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 5 and marks < 14:
            print("You recieved a Grade 1. If you want to check the A-U equivalent, see the conversion file.")

    elif subject == 'Drama':
        percentage = input('What percentage of Marks did you score correctly >> ')
        percentage = float(percentage) / 100
        marks = percentage * 80

        if marks >= 60:
            print("You recieved a Grade 9. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 53 and marks < 60:
            print("You recieved a Grade 8. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 46 and marks < 53:
            print("You recieved a Grade 7. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 38 and marks < 46:
            print("You recieved a Grade 6. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 30 and marks < 38:
            print("You recieved a Grade 5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 23 and marks < 30:
            print("You recieved a Grade 4. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 18 and marks < 23:
            print("You recieved a Grade 3. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 13 and marks < 18:
            print("You recieved a Grade 2. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 8 and marks < 13:
            print("You recieved a Grade 1. If you want to check the A-U equivalent, see the conversion file.")

    elif subject == 'English Language':
        percentage = input('What percentage of Marks did you score correctly >> ')
        percentage = float(percentage) / 100
        marks = percentage * 160

        if marks >= 121:
            print("You recieved a Grade 9. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 111 and marks < 121:
            print("You recieved a Grade 8. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 101 and marks < 111:
            print("You recieved a Grade 7. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 90 and marks < 101:
            print("You recieved a Grade 6. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 79 and marks < 90:
            print("You recieved a Grade 5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 68 and marks < 79:
            print("You recieved a Grade 4. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 50 and marks < 68:
            print("You recieved a Grade 3. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 32 and marks < 50:
            print("You recieved a Grade 2. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 14 and marks < 32:
            print("You recieved a Grade 1. If you want to check the A-U equivalent, see the conversion file.")

    elif subject == 'English Language':
        percentage = input('What percentage of Marks did you score correctly >> ')
        percentage = float(percentage) / 100
        marks = percentage * 160

        if marks >= 138:
            print("You recieved a Grade 9. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 123 and marks < 138:
            print("You recieved a Grade 8. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 109 and marks < 123:
            print("You recieved a Grade 7. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 93 and marks < 109:
            print("You recieved a Grade 6. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 77 and marks < 93:
            print("You recieved a Grade 5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 61 and marks < 77:
            print("You recieved a Grade 4. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 43 and marks < 61:
            print("You recieved a Grade 3. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 26 and marks < 43:
            print("You recieved a Grade 2. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 9 and marks < 26:
            print("You recieved a Grade 1. If you want to check the A-U equivalent, see the conversion file.")

    elif subject == 'Engineering':
        percentage = input('What percentage of Marks did you score correctly >> ')
        percentage = float(percentage) / 100
        marks = percentage * 120

        if marks >= 96:
            print("You recieved a Grade 9. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 87 and marks < 96:
            print("You recieved a Grade 8. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 79 and marks < 87:
            print("You recieved a Grade 7. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 67 and marks < 79:
            print("You recieved a Grade 6. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 56 and marks < 67:
            print("You recieved a Grade 5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 45 and marks < 56:
            print("You recieved a Grade 4. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 32 and marks < 45:
            print("You recieved a Grade 3. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 19 and marks < 32:
            print("You recieved a Grade 2. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 6 and marks < 19:
            print("You recieved a Grade 1. If you want to check the A-U equivalent, see the conversion file.")

    elif subject == 'French':
        percentage = input('What percentage of Marks did you score correctly >> ')
        percentage = float(percentage) / 100
        level = input('Did you take the H or F exam >> ')
        marks = percentage * 180

        #Foundation Level
        if marks >= 116 and level == 'F':
            print("You recieved a Grade 5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 101 and level == 'F' and marks < 116:
            print("You recieved a Grade 4. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 71 and level == 'F' and marks < 101:
            print("You recieved a Grade 3. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 41 and level == 'F' and marks < 71:
            print("You recieved a Grade 2. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 12 and level == 'F':
            print("You recieved a Grade 1. If you want to check the A-U equivalent, see the conversion file.")

        #Higher level
        elif marks >= 139 and level == 'H':
            print("You recieved a Grade 9. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 122 and level == 'H' and marks < 139:
            print("You recieved a Grade 8. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 105 and level == 'H' and marks < 122:
            print("You recieved a Grade 7. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 91 and level == 'H' and marks < 105:
            print("You recieved a Grade 6. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 77 and level == 'H' and marks < 91:
            print("You recieved a Grade 5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 64 and level == 'H' and marks < 77:
            print("You recieved a Grade 4. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 57 and level == 'H' and marks < 64:
            print("You recieved a Grade 5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks < 57 and level == 'H':
            print("You did not recieved a Grade.")

    elif subject == 'Geography':
        percentage = input('What percentage of Marks did you score correctly >> ')
        percentage = float(percentage) / 100
        marks = percentage * 252

        if marks >= 175:
            print("You recieved a Grade 9. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 157 and marks < 175:
            print("You recieved a Grade 8. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 139 and marks < 157:
            print("You recieved a Grade 7. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 120 and marks < 139:
            print("You recieved a Grade 6. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 101 and marks < 120:
            print("You recieved a Grade 5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 82 and marks < 101:
            print("You recieved a Grade 4. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 60 and marks < 82:
            print("You recieved a Grade 3. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 38 and marks < 60:
            print("You recieved a Grade 2. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 10 and marks < 38:
            print("You recieved a Grade 1. If you want to check the A-U equivalent, see the conversion file.")

    elif subject == 'History':
        percentage = input('What percentage of Marks did you score correctly >> ')
        percentage = float(percentage) / 100
        marks = percentage * 168

        if marks >= 108:
            print("You recieved a Grade 9. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 95 and marks < 108:
            print("You recieved a Grade 8. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 82 and marks < 95:
            print("You recieved a Grade 7. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 69 and marks < 82:
            print("You recieved a Grade 6. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 56 and marks < 69:
            print("You recieved a Grade 5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 44 and marks < 56:
            print("You recieved a Grade 4. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 32 and marks < 44:
            print("You recieved a Grade 3. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 20 and marks < 32:
            print("You recieved a Grade 2. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 8 and marks < 20:
            print("You recieved a Grade 1. If you want to check the A-U equivalent, see the conversion file.")

    elif subject == 'French':
        percentage = input('What percentage of Marks did you score correctly >> ')
        percentage = float(percentage) / 100
        level = input('Did you take the H or F exam >> ')
        marks = percentage * 240

        #Foundation Level
        if marks >= 145 and level == 'F':
            print("You recieved a Grade 5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 108 and level == 'F' and marks < 145:
            print("You recieved a Grade 4. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 79 and level == 'F' and marks < 108:
            print("You recieved a Grade 3. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 51 and level == 'F' and marks < 79:
            print("You recieved a Grade 2. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 23 and level == 'F':
            print("You recieved a Grade 1. If you want to check the A-U equivalent, see the conversion file.")

        #Higher level
        elif marks >= 192 and level == 'H':
            print("You recieved a Grade 9. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 155 and level == 'H' and marks < 192:
            print("You recieved a Grade 8. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 119 and level == 'H' and marks < 155:
            print("You recieved a Grade 7. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 90 and level == 'H' and marks < 119:
            print("You recieved a Grade 6. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 62 and level == 'H' and marks < 90:
            print("You recieved a Grade 5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 34 and level == 'H' and marks < 62:
            print("You recieved a Grade 4. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 20 and level == 'H' and marks < 34:
            print("You recieved a Grade 5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks < 20 and level == 'H':
            print("You did not recieved a Grade.")

    elif subject == 'Music':
        percentage = input('What percentage of Marks did you score correctly >> ')
        percentage = float(percentage) / 100
        marks = percentage * 96

        if marks >= 62:
            print("You recieved a Grade 9. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 54 and marks < 62:
            print("You recieved a Grade 8. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 46 and marks < 54:
            print("You recieved a Grade 7. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 38 and marks < 46:
            print("You recieved a Grade 6. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 30 and marks < 38:
            print("You recieved a Grade 5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 22 and marks < 30:
            print("You recieved a Grade 4. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 16 and marks < 22:
            print("You recieved a Grade 3. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 10 and marks < 16:
            print("You recieved a Grade 2. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 5 and marks < 10:
            print("You recieved a Grade 1. If you want to check the A-U equivalent, see the conversion file.")

    elif subject == 'Physical Education' or 'PE':
        percentage = input('What percentage of Marks did you score correctly >> ')
        percentage = float(percentage) / 100
        marks = percentage * 156

        if marks >= 109:
            print("You recieved a Grade 9. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 100 and marks < 109:
            print("You recieved a Grade 8. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 92 and marks < 100:
            print("You recieved a Grade 7. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 79 and marks < 92:
            print("You recieved a Grade 6. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 67 and marks < 79:
            print("You recieved a Grade 5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 55 and marks < 67:
            print("You recieved a Grade 4. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 40 and marks < 55:
            print("You recieved a Grade 3. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 26 and marks < 40:
            print("You recieved a Grade 2. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 12 and marks < 26:
            print("You recieved a Grade 1. If you want to check the A-U equivalent, see the conversion file.")

    elif subject == 'Physics':
        percentage = input('What percentage of Marks did you score correctly >> ')
        percentage = float(percentage) / 100
        level = input('Did you take the H or F exam >> ')
        marks = percentage * 200

        #Foundation Level
        if marks >= 123 and level == 'F':
            print("You recieved a Grade 5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 98 and level == 'F' and marks < 123:
            print("You recieved a Grade 4. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 70 and level == 'F' and marks < 98:
            print("You recieved a Grade 3. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 43 and level == 'F' and marks < 70:
            print("You recieved a Grade 2. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 16 and level == 'F':
            print("You recieved a Grade 1. If you want to check the A-U equivalent, see the conversion file.")

        #Higher level
        elif marks >= 140 and level == 'H':
            print("You recieved a Grade 9. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 120 and level == 'H' and marks < 140:
            print("You recieved a Grade 8. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 101 and level == 'H' and marks < 120:
            print("You recieved a Grade 7. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 80 and level == 'H' and marks < 101:
            print("You recieved a Grade 6. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 60 and level == 'H' and marks < 80:
            print("You recieved a Grade 5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 40 and level == 'H' and marks < 60:
            print("You recieved a Grade 4. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 30 and level == 'H' and marks < 40:
            print("You recieved a Grade 5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks < 30 and level == 'H':
            print("You did not recieved a Grade.")

    elif subject == 'Religous Studies' or 'RS' or 'EPR' or 'RE':
        percentage = input('What percentage of Marks did you score correctly >> ')
        percentage = float(percentage) / 100
        marks = percentage * 102

        if marks >= 89:
            print("You recieved a Grade 9. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 81 and marks < 89:
            print("You recieved a Grade 8. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 74 and marks < 81:
            print("You recieved a Grade 7. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 63 and marks < 74:
            print("You recieved a Grade 6. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 53 and marks < 63:
            print("You recieved a Grade 5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 43 and marks < 53:
            print("You recieved a Grade 4. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 31 and marks < 43:
            print("You recieved a Grade 3. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 19 and marks < 31:
            print("You recieved a Grade 2. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 8 and marks < 19:
            print("You recieved a Grade 1. If you want to check the A-U equivalent, see the conversion file.")

    elif subject == 'Science' or 'Combined Science':
        percentage = input('What percentage of Marks did you score correctly >> ')
        percentage = float(percentage) / 100
        level = input('Did you take the H or F exam >> ')
        marks = percentage * 200

        #Foundation Level
        if marks >= 231 and level == 'F':
            print("You recieved a Grade 5-5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 208 and level == 'F' and marks < 231:
            print("You recieved a Grade 5-4. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 184 and level == 'F' and marks < 208:
            print("You recieved a Grade 4-4. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 160 and level == 'F' and marks < 184:
            print("You recieved a Grade 4-3. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 135 and level == 'F' and marks < 160:
            print("You recieved a Grade 3-3. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 110 and level == 'F' and marks < 135:
            print("You recieved a Grade 3-2. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 85 and level == 'F' and marks < 110:
            print("You recieved a Grade 2-2. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 60 and level == 'F' and marks < 85:
            print("You recieved a Grade 2-1. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 36 and level == 'F':
            print("You recieved a Grade 1-1. If you want to check the A-U equivalent, see the conversion file.")

        #Higher level
        elif marks >= 262 and level == 'H':
            print("You recieved a Grade 9-9. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 244 and level == 'H' and marks < 262:
            print("You recieved a Grade 9-8. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 226 and level == 'H' and marks < 244:
            print("You recieved a Grade 8-8. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 208 and level == 'H' and marks < 226:
            print("You recieved a Grade 8-7. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 190 and level == 'H' and marks < 208:
            print("You recieved a Grade 7-7. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 171 and level == 'H' and marks < 190:
            print("You recieved a Grade 7-6. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 153 and level == 'H' and marks < 171:
            print("You recieved a Grade 6-6. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 135 and level == 'H' and marks < 153:
            print("You recieved a Grade 6-5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 117 and level == 'H' and marks < 135:
            print("You recieved a Grade 5-5. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 99 and level == 'H' and marks < 117:
            print("You recieved a Grade 5-4. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 81 and level == 'H' and marks < 99:
            print("You recieved a Grade 4-4. If you want to check the A-U equivalent, see the conversion file.")
        elif marks >= 72 and level == 'H' and marks < 81:
            print("You recieved a Grade 4-3. If you want to check the A-U equivalent, see the conversion file.")
        elif marks < 72 and level == 'H':
            print("You did not recieved a Grade.")





#run()