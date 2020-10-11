class LivingPeople:
    def __init__(self, people):
        self.people = people
        self.earliest_birth = self._get_earliest_birth()
        self.latest_death = self._get_latest_death()
        self.living_people_by_year = self._get_living_people_by_year()

    def get_year_with_most_people_alive(self):
        return self.living_people_by_year.index(max(self.living_people_by_year)) + self.earliest_birth

    def _get_living_people_by_year(self):
        living = [0] * (self.latest_death + 2 - self.earliest_birth)
        for start, end in self.people:
            self._add_birth(living, start)
            self._add_death(living, end)

        for i in range(1, len(living)):
            living[i] += living[i - 1]

        return living

    def _add_birth(self, living, year):
        birth_index = self._get_index_from_year(year, True)
        living[birth_index] += 1

    def _add_death(self, living, year):
        death_index = self._get_index_from_year(year, False)
        living[death_index] -= 1

    def _get_index_from_year(self, year, isBirthYear=True):
        index = year - self.earliest_birth
        return index if isBirthYear else index + 1

    def _get_latest_death(self):
        return max(self.people, key=lambda person: person[1])[1]
    
    def _get_earliest_birth(self):
        return min(self.people)[0]


if __name__ == '__main__':
    people = [
        (1900, 1947),
        (1910, 1957),
        (1922, 1980),
        (1932, 2000),
        (1941, 2015),
        (1950, 1957),
        (1958, 2020),
        (1973, 2001),
        (1979, 2045),
        (1992, 2092),
        (1996, 2021),
        (1998, 2010),
        (2000, 2080),
    ]
    lp = LivingPeople(people)
    print(lp.get_year_with_most_people_alive())