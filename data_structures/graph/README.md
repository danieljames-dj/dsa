GRAPH
Graph is a data structure that consists of following two components:
1. A finite set of vertices also called as nodes.
2. A finite set of ordered pair of the form (u, v) called as edge. The pair is ordered because (u, v) is not same as (v, u) in case of directed graph(di-graph). The pair of form (u, v) indicates that there is an edge from vertex u to vertex v. The edges may contain weight/value/cost.
In graph theory, an incidence is a pair (u,e) where u is a vertex and e is an edge incident to u.

REPRESENTATION
Adjacency Matrix
Adjacency List

DEGREE (VALENCY)
It is the number of vertices adjacent to a vertex. Each vertex has an indegree and an outdegree in a directed graph.
An isolated vertex is a vertex with degree zero; that is, a vertex that is not an endpoint of any edge (the example image illustrates one isolated vertex). A leaf vertex (also pendant vertex) is a vertex with degree one.

USELESS TOPICS
Applications
1. Graphs are used to represent networks. The networks may include paths in a city or telephone network or circuit network.
2. Graphs are also used in social networks like linkedIn, facebook. For example, in facebook, each person is represented with a vertex(or node). Each node is a structure and contains information like person id, name, gender and locale.

Finite & Infinite graph: If the set of vertices and the set of edges of a graph are both finite, the graph is called finite, otherwise infinite. An infinite graph has infinitely many edges but possibly only finitely many vertices (e.g., two vertices can be connected by infinitely many edges.)

Null graph: An empty graph on nodes consists of isolated nodes with no edges.

Isomorphic graphs: Two graphs G1 and G2 are said to be isomorphic if their number of components (vertices and edges) are same and their edge connectivity is retained.

Subgraph: A subgraph S of a graph G is a graph whose set of vertices and set of edges are all subsets of G.

Walk: Finite alternating sequence of vertices and edges, beginning and ending with vertices, such that each edge is incident with the vertices preceding and following it. Edge won’t be repeated, but vertex will be repeated.

Path: An open walk in which no vertex appears more than once.

Circuit: A closed walk in which no vertex appears more than once.

Connected & disconnected graph: A graph is connected if there is at least one path between every pair of vertices. Else, it is disconnected graph.

Euler Graph: If some closed walk in a graph contains all the edges of a graph, then the walk is known as Euler line and the graph is known as Euler graph.


Problems:
1. https://www.geeksforgeeks.org/count-of-distinct-graphs-that-can-be-formed-with-n-vertices/
2. RoadsAndLibraries