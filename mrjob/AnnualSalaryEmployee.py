from mrjob.job import MRJob

class averageSalaryEmployee(MRJob):

    def mapper(self, _, line):
        idemp, sececon, salary, year = line.split(',')
        try:
            salary = float(salary)
        except ValueError:
            pass
        else:
            yield idemp, salary


    def reducer (self, idemp, salaries):
        sum_salary=0
        count =0
        for s in salaries:
            sum_salary += s
            count += 1

        yield idemp, sum_salary/count

if __name__ == '__main__':
    averageSalaryEmployee.run()
