## Written by Jitesh Jain on 12/03/2021

import csv
import argparse
import pandas as pd

## Class storing the 5 attributes for all particles
class Particle:
    def __init__(self, obj1, E1, pt1, eta1, phi1):
        self.obj1 = obj1
        self.E1 = E1
        self.pt1 = pt1
        self.eta1 = eta1
        self.phi1 = phi1

    def __str__(self):
        return "{} {} {} {} {}".format(self.obj1, self.E1, self.pt1, self.eta1, self.phi1)

    def __iter__(self):
        return iter([self.obj1, self.E1, self.pt1, self.eta1, self.phi1])

def main(args):

    ## List to store all the particles detected during all the events
    particles = []

    ## Number of rows read
    count = 0
    with open(args.csv, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            count+=1

            ## Skip 1st row as it contains coulumn names
            if count == 1:
                continue

            for i in range(5,len(row)):

                ## Get a list of obj, E, pt, eta, phi
                attr = row[i].split(',')

                if len(attr) == 5: ## If there was no particle the length would be 1 
                    p = Particle(attr[0], attr[1], attr[2], attr[3], attr[4])
                    particles.append(p)

    ## Define lists for making a Pandas Dataframe later
    Es = []
    pts = []
    etas = []
    phis = []

    ## Store particles' attributes into the lists
    for p in particles:
        if p.obj1 == 'j':
            Es.append(float(p.E1))
            pts.append(float(p.pt1))
            etas.append(float(p.eta1))
            phis.append(float(p.phi1))


    ## Prepare a Pandas Dataframe
    df = pd.DataFrame(
        {'E': Es,
         'pt': pts,
         'eta': etas,
         'phi': phis
        })

    ## Store the Dataframe into a .pkl file
    df.to_pickle(args.pkl)

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="CSV_to_PKL")
    parser.add_argument("--csv", default='data/mod.csv',
    help="csv to read from")
    parser.add_argument("--pkl", default='data/jet_particles.pkl',
    help="pkl file to write to")
    
    args =  parser.parse_args()
    
    main(args)