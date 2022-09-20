import math
import random
import uuid

from constants import MAX_T, SEED_SET_SIZE
from utils import maximum_degree, graph_length, graph_nodes


class Wolf(object):
    def __init__(self, *args, **kwargs):
        self._position = kwargs.get("position")
        self._seed_set = kwargs.get("seed_set")
        self._value = kwargs.get("value")
        self._history = []
        # self._position_history = {}
        self._id = uuid.uuid4().hex

    def __str__(self):
        return f"Wolf({self._id})"

    def random_position(self, graph):
        """
        generating random position list Xi for wolf i
        generating corresponding seed set i for wolf i
        based on algorithm 3 in article
        """
        xi = {}

        graph_len = graph_length(graph)
        nodes_list = graph_nodes(graph)
        max_degree = maximum_degree(graph)

        for j in range(0, graph_len):
            r = random.uniform(1, graph.degree(nodes_list[j]))
            xi[j] = r / max_degree

        self.X = xi
        return self.X

    def generate_corresponding_seed_set(self, graph):
        """
        calculating corresponding seed set based on
        K which is number of seed set
        and Xi position list for wolf i based on algorithm 3 in article
        """

        position_copy = dict(self.X)
        filtered_position = sorted(
            position_copy.items(), key=lambda item: item[1], reverse=True
        )[:SEED_SET_SIZE]

        filtered_position = dict(filtered_position)
        si = []
        nodes_list = graph_nodes(graph)
        for node_index in filtered_position.keys():
            si.append(nodes_list[node_index])

        self.S = si
        return self.S

    def update_position(self, alpha, beta, delta, iteration, graph):
        """
        update position list of wolf i based on alpha, beta, delta wolves
        based on algorithm 4 in article
        """
        a = 2 - 2 * (iteration / MAX_T)

        wolf_position = self.X
        new_position = dict(wolf_position)

        alpha_position = alpha.X
        beta_position = beta.X
        delta_position = delta.X
        graph_len = graph_length(graph)

        for j in range(0, graph_len):
            # Alpha
            r1 = random.random()
            r2 = random.random()
            alpha_A1 = (2 * a) * r1 - a
            alpha_C1 = 2 * r2
            daj = abs((alpha_C1 * alpha_position[j]) - wolf_position[j])
            y1 = alpha_position[j] - (alpha_A1 * daj)

            # Beta
            r1 = random.random()
            r2 = random.random()
            beta_A1 = (2 * a) * r1 - a
            beta_C1 = 2 * r2
            dbj = abs((beta_C1 * beta_position[j]) - wolf_position[j])
            y2 = beta_position[j] - (beta_A1 * dbj)

            # Delta
            r1 = random.random()
            r2 = random.random()
            delta_A1 = (2 * a) * r1 - a
            delta_C1 = 2 * r2
            ddj = abs((delta_C1 * delta_position[j]) - wolf_position[j])
            y3 = delta_position[j] - (delta_A1 * ddj)

            # new position for Jth entery
            new_position[j] = (y1 + y2 + y3) / 3

        self.X = new_position
        return new_position

    @property
    def X(self):
        return self._position

    @X.setter
    def X(self, value):
        self._position = value

    @property
    def S(self):
        return self._seed_set

    @S.setter
    def S(self, value):
        self._seed_set = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._history.append(value)
        self._value = value

    # def register_position_history(self, t):
    #     self._position_history[t] = self._position

    # def move(self, t, t_next):
    #     if self._position_history.get(t_next) and self._position_history.get(t):
    #         distance_moved = math.dist(
    #             self._position_history[t_next], self._position_history[t]
    #         )
    #     elif self._position_history.get(t):
    #         distance_moved = math.dist(
    #             [0] * len(self._position_history[t]), self._position_history[t]
    #         )
    #     else:
    #         distance_moved = 0

    #     return distance_moved
