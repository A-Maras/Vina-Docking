# Parsing PDB file for coordinates
def parsePDB(fname):
      
    f = open(fname)
    lines = f.read().split('\n')
    f.close()

    modelNum = 1
    multiModel = False
    d = {1:{}}
    for line in lines:
        fields = line.split()
        record = fields[0] if len(fields)> 0 else ''
        if record == "MODEL":
            if multiModel:
                modelNum += 1
                d[modelNum] = {}
            else:
                multiModel = True
        elif record == "ATOM":
            num = int(fields[1])
            atomDict = {}
            atomDict["atom"] = fields[2]
            atomDict["amino"] = fields[3]
            atomDict["chain"] = fields[4]
            atomDict["residue"] = int(fields[5])
            atomDict["xyz"] = (float(fields[6]),float(fields[7]),float(fields[8]))
            d[modelNum][num] = atomDict
    return d
  
def parse_dict(parsed_PDB, int_residue_num):
  for item in parsed_PDB:
    if parsed_PDB[item]['residue'] == int_residue_num: 
      return parsed_PDB[item]
    else:
      print('residue not found.')
      return None
  
