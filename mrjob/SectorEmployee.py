from mrjob.job import MRJob

class sectorEmployee(MRJob):

    def mapper(self, _, line):
        idemp, sececon, salary, year = line.split(',')
        try:
            salary = float(salary)
        except ValueError:
            pass
        else:
            yield idemp, sececon


    def reducer (self, idemp, sectors):
        count =0
        for s in sectors:
            count += 1

        yield idemp, count


    

if __name__ == '__main__':
    sectorEmployee.run()
