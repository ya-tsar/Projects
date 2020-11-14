# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 
         'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 
         'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 
          'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 
          'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], 
                  ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], 
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], 
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], 
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], 
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], 
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], 
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], 
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], 
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], 
                  ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], 
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], 
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', 
           '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', 
           '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# update damages function:
def update_damages(damages):
    upd_damages = []
    for damage in damages:
        if damage == "Damages not recorded":
            damage = "Damages not recorded"
        elif 'M' in damage:
            damage = damage.replace('M', '')
            damage = float(damage) * 10**6
        elif 'B' in damage:
            damage = damage.replace('B', '')
            damage = float(damage) * 10**9
        upd_damages.append(damage)
    return upd_damages

upd_damages = update_damages(damages)
print(upd_damages)

# write your construct hurricane dictionary function here:
def construct_hurricane_dictionary_name(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    zipped_info = zip(names, months, years, max_sustained_winds, areas_affected, update_damages(damages), deaths)
    hurricane_dictionary = {name:{'Name': name, 'Month': month, 'Year': year, 'Max Sustained Wind': max_sustained_wind, 
                                  'Areas Affected': area_affected, 'Damage': damage, 'Deaths': death} for name, month, year, max_sustained_wind, 
                            area_affected, damage, death in zipped_info}
    return hurricane_dictionary

# write your construct hurricane by year dictionary function here:
def construct_hurricane_dictionary_year(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    hurricane_dictionary = {}
    damages = update_damages(damages)
    hurricane_dictionary = {year:list() for year in years}
    for i, year in enumerate(years):
        hurricane_dictionary[year].append({'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 
                                           'Areas Affected': areas_affected[i], 'Damage': damages[i], 'Deaths': deaths[i]})
    return hurricane_dictionary

hurricane_dictionary = construct_hurricane_dictionary_name(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
# print(hurricane_dictionary)

# write your count affected areas function here:
def count_affected_areas(areas_affected):
    areas_list = []
    for i in areas_affected:
        for k in i:
            areas_list.append(k)
    affected_areas = {area: areas_list.count(area) for area in areas_list}
    return affected_areas

#print(count_affected_areas(areas_affected))

# write your find most affected area function here:
def find_most_affected_area(areas_affected):
    count = count_affected_areas(areas_affected)
    most_affected_val = 0
    for key, value in count.items():
        if value >= most_affected_val:
            most_affected_val = value
            most_affected_area = key
    return f'The most affected area is {most_affected_area} with {most_affected_val} hits'

# print(find_most_affected_area(areas_affected))

# write your greatest number of deaths function here:
def greatest_number_deaths(hurricane_dictionary):
    max_death = 0
    for name, value in hurricane_dictionary.items():
        if value['Deaths'] >= max_death:
            max_death = value['Deaths']
            hurricane_name = name
    return f'The hurricane that caused the greatest number of deaths is {hurricane_name} with {max_death} deaths.'
            
# print(greatest_number_deaths(hurricane_dictionary))            
        
# write your catgeorize by mortality function here:
def catgeorize_mortality(hurricane_dictionary):
    mortality_scale = {0: 0,
                       1: 100,
                       2: 500,
                       3: 1000,
                       4: 10000}
    mortality_ratings = {i:[] for i in range(6)}
    for value in hurricane_dictionary.values():
        for raiting, death in mortality_scale.items():
            if value['Deaths'] > death:
                hur_raiting = raiting + 1
        mortality_ratings[hur_raiting].append(value)
    return mortality_ratings
            
# print(catgeorize_mortality(hurricane_dictionary))        

# write your greatest damage function here:
def greatest_damage(hurricane_dictionary):
    greatest_damage = 0
    for name, value in hurricane_dictionary.items():
        if (value['Damage'] != 'Damages not recorded') and (value['Damage'] >= greatest_damage):
            greatest_damage = value['Damage']
            hur_name = name
    return f'The hurricane that caused the greatest damage is {hur_name}, it was costly {greatest_damage}'

# print(greatest_damage(hurricane_dictionary))      

# write your catgeorize by damage function here:
def catgeorize_damage(hurricane_dictionary):
    damage_scale = {0: 0,
    1: 100000000,
    2: 1000000000,
    3: 10000000000,
    4: 50000000000}
    damage_raiting = {i:[] for i in range(6)}
    for value in hurricane_dictionary.values():
        for raiting, damage in damage_scale.items():
            if value['Damage'] == 'Damages not recorded':
                hur_raiting = 0
            elif value['Damage'] >= damage:
                hur_raiting = raiting + 1
        damage_raiting[hur_raiting].append(value)
    return damage_raiting

print(catgeorize_damage(hurricane_dictionary))