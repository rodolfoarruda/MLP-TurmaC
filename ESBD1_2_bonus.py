from collections import deque   
import random
import uuid
import time


class Person(object):

    def __init__(self, uid, genre):
        self._uid = uid
        self._genre = genre

    def get_uid(self):
        return self._uid

    def get_genre(self):
        return self._genre


class FriendNetwork(object):

    def __init__(self, people_num, connections_num):
        self._people_num = people_num
        self._connections_num = connections_num
        self._graph = self._generate_graph()

    def _generate_graph(self):

        people = []
        for person_index in range(self._people_num):
            uid = str(uuid.uuid4())
            genre = 'female' if person_index % 2 else 'male'
            people.append(Person(uid, genre))

        conn_num = 0
        graph = {}
        graph_aux = {}  # criando um grafo auxiliar para agilizar algumas buscas

        # início - criando um caminho alternante
        person = people[conn_num]
        person_uid = person.get_uid()
        graph[person_uid] = {
            'this': person,
            'friends': []
        }
        graph_aux[person_uid] = {}

        while conn_num < self._people_num - 1:
            friend = people[conn_num + 1]
            friend_uid = friend.get_uid()
            graph[friend_uid] = {
                'this': friend,
                'friends': []
            }
            graph_aux[friend_uid] = {}

            graph[person_uid]['friends'].append(friend)
            graph[friend_uid]['friends'].append(person)
            graph_aux[person_uid][friend_uid] = True
            graph_aux[friend_uid][person_uid] = True
            conn_num += 1

            person = friend
            person_uid = friend_uid
        # fim - criando um caminho alternante

        while conn_num < self._connections_num:
            person, friend = random.sample(people, 2)
            person_uid = person.get_uid()
            friend_uid = friend.get_uid()

            if person_uid not in graph:
                graph[person_uid] = {
                    'this': person,
                    'friends': []
                }
                # criando um índice auxiliar para os vizinhos de cada vértice inserido no grafo
                graph_aux[person_uid] = {}

            if friend_uid not in graph:
                graph[friend_uid] = {
                    'this': friend,
                    'friends': []
                }
                # criando um índice auxiliar para os vizinhos de cada vértice inserido no grafo
                graph_aux[friend_uid] = {}

            # if person_uid == friend_uid or \
            #     friend in graph[person_uid]['friends']: # fazer essa verificação em um índice auxiliar
            #     continue
            if person_uid == friend_uid or \
                    friend_uid in graph_aux[person_uid]:
                continue

            graph[person_uid]['friends'].append(friend)
            graph[friend_uid]['friends'].append(person)
            # adicionar vizinho também nos índices do grafo auxiliar
            graph_aux[person_uid][friend_uid] = True
            graph_aux[friend_uid][person_uid] = True
            conn_num += 1

        # # remover vértices que não tem vizinhos do gênero oposto para aumentar conectividade
        # # Não é mais necessário pois temos um caminho alternante conectando todos os vértices
        # people_to_remove = []
        # for person_uid in graph:
        #     friends_types = [
        #         *map(lambda p: p.get_genre(), graph[person_uid]['friends'])]
        #     person_type = graph[person_uid]['this'].get_genre()
        #     if ('male' not in friends_types or 'female' not in friends_types) and person_type in friends_types:
        #         people_to_remove.append(
        #             {'person_uid': person_uid, 'remove_from': graph[person_uid]['friends']})

        # for person_props in people_to_remove:
        #     print("Removendo alguém")
        #     for friend in person_props['remove_from']:
        #         person_index = [*map(lambda friend: friend.get_uid(),
        #                              graph[friend.get_uid()]['friends'])].index(person_props['person_uid'])
        #         del graph[friend.get_uid()]['friends'][person_index]
        #     del graph[person_props['person_uid']]

        return graph

    def get_person_by_uid(self, uid):
        return self._graph[uid]['this']
    
    
    def _search_alternate(self, person_uid, friend_uid):
            visited = {person_uid}
            queue = deque([(person_uid, [], None)])
            current_genre = self._graph[person_uid]['this'].get_genre()
            
            while queue:
                vertex, path, genre = queue.popleft()
                if vertex == friend_uid:
                    return path + [vertex]
                
                for neighbor in self._graph[vertex]['friends']:
                    neighbor_genre = neighbor.get_genre()
                    if neighbor.get_uid() not in visited and neighbor_genre != genre:
                        visited.add(neighbor.get_uid())
                        if genre is None:
                            next_genre = neighbor_genre
                        else:
                            next_genre = 'male' if neighbor_genre == 'female' else 'female'
                        queue.append((neighbor.get_uid(), path + [vertex], next_genre))
            return None



    def get_separation_degree(self):

        total_paths_len = 0
        for _ in range(100):
            person_uid, friend_uid = random.sample([*self._graph.keys()], 2)
            path = self._search_alternate(person_uid, friend_uid)
            total_paths_len += len(path) - 1

        return total_paths_len / 100


if __name__ == '__main__':

    friend_network = FriendNetwork(100000, 31622777)

    s_time = time.time()
    separation_degree = friend_network.get_separation_degree()
    e_time = time.time()
    print(separation_degree)
    print("tempo =", e_time - s_time)
