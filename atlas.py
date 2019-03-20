class Atlas:
    def __init__(self, gameset):
        self.nx = gameset.scr_width // gameset.cellsize
        self.ny = gameset.scr_height // gameset.cellsize
        self.atlas_reset()

    def evolve(self):
        for i in range(1, self.ny-1):
            for j in range(1, self.nx-1):
                count = 0
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        if not (dy == 0 and dx == 0):
                            count += self.matrix[i+dy][j+dx]
                if count == 2:
                    self.next_matrix[i][j] = self.matrix[i][j]
                elif count == 3:
                    self.next_matrix[i][j] = 1
                else:
                    self.next_matrix[i][j] = 0
        # self.matrix = self.next_matrix
        for i in range(self.ny):
            for j in range(self.nx):
                self.matrix[i][j] = self.next_matrix[i][j]

    def atlas_reset(self):
        self.matrix = []
        self.next_matrix = []
        # initializing the matrix, in which 1s mean alive and 0s mean dead.
        for i in range(self.ny):
            self.matrix.append([])
            for j in range(self.nx):
                self.matrix[i].append(0)

        for i in range(self.ny):
            self.next_matrix.append([])
            for j in range(self.nx):
                self.next_matrix[i].append(0)
