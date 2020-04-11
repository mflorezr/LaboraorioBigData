from mrjob.job import MRJob

class averageSalarySE(MRJob):

    def mapper(self, _, line):
        idemp, sececon, salary, year = line.split(',')
        try:
            salary = float(salary)
        except ValueError:
            pass
        else:
            yield sececon, salary


    def reducer (self, sececon, salaries):
        sum_salary=0
        count =0
        for s in salaries:
            sum_salary += s
            count += 1

        yield sececon, sum_salary/count

if __name__ == '__main__':
    averageSalarySE.run()

