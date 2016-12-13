
    def rec_solve(self,data,i, moves):
        if moves > 100:
            return 0
        if self.done(data):
            self.num_moves.append(moves)
            print moves
            return 0
        state = self.get_state(data)
        if state in self.prev_states:
            return 0
        else:
            self.prev_states.append(state)

        items = data[i][:]

        #print state
        targets = []

        targets = [j for j in (i-1,i+1) if j in range(len(data))] 
    
        for item in items:
            for item2 in items:
                for j in targets:
                    data[j].append(data[i].pop(data[i].index(item)))
                    if item!=item2:
                        data[j].append(data[i].pop(data[i].index(item2)))
                    if self.check_validity(data[j]):
                        self.rec_solve(data, j, moves+1)
                    data[i].append(data[j].pop(data[j].index(item)))
                    if item!=item2:
                        data[i].append(data[j].pop(data[j].index(item2)))


