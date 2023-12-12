import random


class Enpal:
  def __init__(self, engineers, customers, quota):
    self.engineers = engineers
    self.customers = customers
    self.distance = []
    self.total_distance = []
    self.sequence_of_visits = []
    self.quota = quota

  def task_a(self):
    total = self.engineers + self.customers

    for i in range(total):
      self.distance.append(
        [0 if i == j else random.randint(1, 100) for j in range(total)]
      )
 
  def task_b(self):
    random_customers = \
      list(range(self.engineers, self.engineers + self.customers))
    random.shuffle(random_customers)

    visit_index = 0

    for i in range(self.engineers):
      self.sequence_of_visits.append(random_customers[visit_index: visit_index + self.quota[i]])

      visit_index += self.quota[i]

  def _calc_distance(self, eng_idx):
    total_distance = 0
    
    sequence_of_visits = self.sequence_of_visits[eng_idx]

    cur_loc = eng_idx

    for i in sequence_of_visits:
      total_distance += self.distance[cur_loc][i]

      cur_loc = i

    total_distance += self.distance[cur_loc][eng_idx]

    return total_distance


  def task_c(self):
    if len(self.distance) == 0:
      self.task_a()

    if len(self.sequence_of_visits) == 0:
      self.task_b()

    for i in range(self.engineers):
      self.total_distance.append(self._calc_distance(i))

  def _change_sequence(self, sequence_of_visits, route_change):
      new_sequence_of_visits = []

      origin, dest = route_change

      for k, v in enumerate(sequence_of_visits):
        if k == dest:
          new_sequence_of_visits.append(sequence_of_visits[origin]) 
        elif k == origin:
          new_sequence_of_visits.append(sequence_of_visits[dest]) 
        else:
          new_sequence_of_visits.append(v)

      return new_sequence_of_visits

  def task_d(self, route_change):
    if len(self.sequence_of_visits) == 0:
      self.task_b()

    for i in range(self.engineers):
      self.sequence_of_visits[i] = \
        self._change_sequence(
          self.sequence_of_visits[i],
          route_change[i]
        )


################################################################
# create Enpal class instance with following setting
# engineer: 2
# customer: 8
# engineer_0 visit 3 customers, engineer_1 visit 5 customers
################################################################
enpal = Enpal(2, 8, [3, 5])

###########################
# generate distance matrix
###########################
enpal.task_a()

print("\n# generated distance matrix")
print(enpal.distance)


##################################
# generate the sequence of visits
##################################
enpal.task_b()

print("\n# generated the sequence of visits")
print(enpal.sequence_of_visits)


####################################
# calculate the distance of travel
####################################
enpal.task_c()

print("\n# calculated distance of travel ")
print(enpal.total_distance)


################################
# change the sequence of visits
# engineer_0: switch 2nd visit and 3rd visit
# engineer_1: switch 5th visit and 1st visit
################################
enpal.task_d([[1, 2], [4, 0]])

print("\n# changed sequence of visits")
print("# engineer_0: switch 2nd visit and 3rd visit")
print("# engineer_1: switch 5th visit and 1st visit")
print(enpal.sequence_of_visits)
