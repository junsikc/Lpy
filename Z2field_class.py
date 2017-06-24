import numpy as np

# NEEDS DOCUMENTATION ###
# PERHAPS BETTER IMPLEMINATION ###


class Z2Field:
    """Documentation for Z2Field

    """
    def __init__(self, lattice_shape, init):
        # super(Z2Field, self).__init__()
        # lattice_shape is tuple (Nx, Ny, Nz, Nt, .... Nj)
        size = 1
        for j in lattice_shape:
            size *= j
        
        field = -np.ones(size)
        value = [-1, 1]
        if init == "hot":
            for j in range(size):
                index = np.random.randint(2)
                field[j] = value[index]
            self.field = [field.reshape(lattice_shape)]
        if init == "cold":
            self.field = [field.reshape(lattice_shape)]

    def get_field_config(self, j):
        try:
            config = self.field[j]
            return config
        except IndexError:
            print "IndexError"
            print "Returning Last Field Configuration"
            config = self.field[-1]
            return config

    def get_M(self):
        Mag = []
        sigM = 0
        for configs in self.field:
            configs = configs.flatten()
            m = 0
            for spin in configs:
                m += spin
            m = float(m)/len(configs)
            Mag.append(m)
        Mag = np.asarray(Mag)
        M = Mag.mean()
        sigM = Mag.std()

        return M, sigM

    
