seed_soil = [[0,13,20],[80,50,12]]
soil_fert = [[30,0,30],[70,85,10]]

def SeedtoFertilizer(seed):
    def soilId(seed):
        for x in seed_soil:
            if x[0] <= seed <= x[0]+x[2]-1: 
                soil = seed -x[0]+x[1]
                break
        else: soil = seed
        return soil 
    def fertId(soil):
        for x in soil_fert:
            if x[0] <= soil <= x[0]+x[2]-1: 
                fertilizer = soil -x[0]+x[1]
                break
            else: fertilizer = soil
        return fertilizer 

    soil=soilId(seed)
    fertilizer=fertId(soil)
    print('Seed dengan id', seed, 'menggunakan fertilizer dengan id', fertilizer)

SeedtoFertilizer(13)
SeedtoFertilizer(89)
SeedtoFertilizer(41)
SeedtoFertilizer(23)