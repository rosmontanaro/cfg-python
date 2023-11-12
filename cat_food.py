cats = 4
cans_for_cats = 3
day = 7
total_cans = cats * cans_for_cats * day

output= str(cats) + " cats eat " + str(total_cans) + " cans in " + str(day) + " days"
print(output)

output_2= '{} cats eat {} cans in {} days'.format(cats, total_cans, day)
print(output_2)

#this is a comment