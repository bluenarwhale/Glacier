import csv
import matplotlib.pyplot as plt

from utils import check_id, check_lat_value, check_lon_value, check_unit, check_annual_value, check_year, haversine_distance


class Glacier:
    def __init__(self, glacier_id, name, unit, lat, lon, code):
        self.glacier_id = glacier_id
        self.name = name
        self.unit = unit
        self.lat = lat
        self.lon = lon
        self.code = code
        self.years = []
        self.mass_balances = []

    def print_glacier(self):
        print(self.glacier_id, self.name, self.unit, self.lat, self.lon, self.code, self.years, self.mass_balances)

    def add_mass_balance_measurement(self, year, mass_balance, is_partial):
        if year not in self.years:
            self.years.append(year)
            self.mass_balances.append(float(mass_balance))
        elif is_partial == True:
            sum_value = self.mass_balances[self.years.index(year)] + float(mass_balance)
            self.mass_balances[self.years.index(year)] = sum_value

    def plot_mass_balance(self, output_path):
        years = self.years
        mass_balance = self.mass_balances
        plt.plot(years, mass_balance)
        plt.xlabel("Year")
        plt.ylabel("Mass_balance")
        plt.show()
        plt.savefig(output_path)


class GlacierCollection:

    def __init__(self, file_path):
        self.collection = []
        with open(file_path, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(spamreader)
            for row in spamreader:
                if check_id(row[2]) and check_lat_value(row[5]) and check_lon_value(row[6]) and check_unit(row[0]):
                    glacier = Glacier(row[2], row[1], row[0], float(row[5]), float(row[6]),
                                      int(row[7] + row[8] + row[9]))
                    self.collection.append(glacier)

    def read_mass_balance_data(self, file_path):
        with open(file_path, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(spamreader)
            for row in spamreader:
                for glacier in self.collection:
                    if row[2] == glacier.glacier_id:
                        if check_annual_value(row[-3]) and check_year(row[3]):
                            if row[4] == '9999':
                                glacier.add_mass_balance_measurement(row[3], row[-3], False)
                            else:
                                glacier.add_mass_balance_measurement(row[3], row[-3], True)

    #                         else:
    #                             print('The annual value of glacier ',row[2],' in year ',row[3],' is not digit, it is ',row[-3] )

    def find_nearest(self, lat, lon, n=5):
        dis_list = []
        name_list = []
        top_name = []
        if check_lat_value(lat) and check_lon_value(lon):
            for glacier in self.collection:
                lon1 = glacier.lon
                lat1 = glacier.lat
                dis_list.append(haversine_distance(float(lat), float(lon), float(lat1), float(lon1)))
                name_list.append(glacier.name)
        dis_copy = dis_list.copy()
        dis_copy.sort()
        top_n = dis_copy[:n]
        i = 0
        for i in top_n:
            top_name.append(name_list[dis_list.index(i)])
        return top_name[:n]

    def filter_by_code(self, code_pattern):
        """Return the names of glaciers whose codes match the given pattern."""
        raise NotImplementedError

    def sort_by_latest_mass_balance(self, n=5, reverse=True):
        """Return the N glaciers with the highest area accumulated in the last measurement."""
        mass_balance_list = []
        name_list = []
        top_name = []

        for glacier in self.collection:
            if glacier.mass_balances == []:
                mass_balance = 0
            else:
                mass_balance = glacier.mass_balances[-1]
            mass_balance_list.append(mass_balance)
            name_list.append(glacier.name)
        dis_copy = mass_balance_list.copy()

        if reverse == True:
            dis_copy.sort(reverse=True)
        else:
            dis_copy.sort()

        top_n = dis_copy[:n]
        i = 0
        for i in top_n:
            top_name.append(name_list[mass_balance_list.index(i)])
        return top_name[:n]

    def summary(self):
        num_Glaciers = len(self.collection)

        years = []
        for glacier in self.collection:
            years.extend(glacier.years)

        earlist_recorded_year = min(years)

        shrunk_sum = 0
        glacier_sum = 0
        for i in self.collection:
            if i.mass_balances != []:
                glacier_sum = glacier_sum + 1
                if i.mass_balances[-1] < 0:
                    shrunk_sum = shrunk_sum + 1

        percentage_shrunk = int(shrunk_sum / glacier_sum * 100)

        print("This collection has", num_Glaciers, "glaciers.")
        print("The earliest measurement was in ", earlist_recorded_year, " .")
        print(percentage_shrunk, "% ", "of glaciers shrunk in their last measurement")

    def plot_extremes(self, output_path):
        raise NotImplementedError

