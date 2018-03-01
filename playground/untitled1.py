import networkx as net
import matplotlib.pyplot as plt

o=net.Graph()

o.add_edge('Conrad','Mary')
o.add_edge('Conrad','Cindy')
o.add_edge('Conrad','Alice')
o.add_edge('Alice','Brad')
o.add_edge('Alice','Angie')
o.add_edge('Alice','Jim')
o.add_edge('Cindy','Samuel')
o.add_edge('Cindy','Dave')
o.add_edge('Cindy','Frida')

pos = net.fruchterman_reingold_layout(o)

#net.draw(o)

sizes_name = {}

for node in o.nodes:
    sizes_name[node] = 0
    for edge in o.edges:
        if node in edge:
            sizes_name[node] += 1
            

sizes = []
for item in sizes_name:
    sizes.append(sizes_name[item] * 100)

print(sizes)
 
#for edge in o.edges:
  #  print(edge)
#labels = net.get_edge_attributes(o,'weight')
#net.draw_networkx_edge_labels(o,,edge_labels=labels)

net.draw_networkx(o,pos,node_size=sizes)
plt.show()
#net.write_pajek(o,'ACME_orgchart.net')
