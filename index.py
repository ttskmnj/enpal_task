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

  def __calc_distance(self, eng_idx, sequence_of_visits):
    total_distance = 0

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
      self.total_distance.append(self.__calc_distance(i, self.sequence_of_visits[i]))

  def __change_sequence(self, sequence_of_visits, route_change):
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

    for k, v in enumerate(self.sequence_of_visits):
      self.sequence_of_visits[k] = \
        self.__change_sequence(
          v,
          route_change[k]
        )

  def __two_opt_swap(self, sequence_of_visits, route_change):
    point_0, point_1 = route_change
    reverse_sequence = sequence_of_visits[point_0: point_1]
    reverse_sequence.reverse()

    return sequence_of_visits[:point_0] + reverse_sequence + sequence_of_visits[point_1:]

  def task_e(self):
    if len(self.distance) == 0:
      self.task_a()

    if len(self.sequence_of_visits) == 0:
      self.task_b()

    if len(self.total_distance) == 0:
      self.task_c()

    for k, v in enumerate(self.sequence_of_visits):
      best_distance = self.total_distance[k]
      best_sequence_of_visits = v
      sequence_of_visits = v

      for i in range(len(v) - 1):
        for j in range(i, len(v)):
          changed_sequence = \
            self.__two_opt_swap(
              sequence_of_visits,
              [i, j]
            )

          new_distance = self.__calc_distance(k, changed_sequence)

          # update sequence of visit if distance is shorter
          if new_distance < best_distance:
            best_sequence_of_visits = changed_sequence
            best_distance = new_distance
        sequence_of_visits = best_sequence_of_visits
      self.sequence_of_visits[k] = sequence_of_visits
      self.total_distance[k] = best_distance


if __name__ == "__main__":
  ##############################################################
  # create Enpal class instance with following setting
  # engineer: 2
  # customer: 8
  # engineer_0 visit 5 customers, engineer_1 visit 3 customers
  ##############################################################
  enpal = Enpal(2, 8, [5, 3])

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


  #############################################
  # change the sequence of visits
  # engineer_0: switch 5th visit and 2nd visit
  # engineer_1: switch 2nd visit and 3rd visit
  #############################################
  enpal.task_d([[4, 1], [1, 2]])

  print("\n# changed sequence of visits")
  print("# engineer_0: switch 5th visit and 2nd visit")
  print("# engineer_1: switch 2nd visit and 3rd visit")
  print(enpal.sequence_of_visits)

  ##############################
  # Optimize sequence of visits 
  # with 2 opt algorithm
  ##############################
  enpal.task_e()
  print("\n# optimized sequence of visits")
  print(enpal.sequence_of_visits)
  print("# optimized total_distance")
  print(enpal.total_distance)
