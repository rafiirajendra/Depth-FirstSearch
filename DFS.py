from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def dfs_with_target(self, start, target, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []
        
        visited.add(start)
        path.append(start)
        
        if start == target:
            print("\nTarget ditemukan! Jalur:", ' -> '.join(path))
            return True
        
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                if self.dfs_with_target(neighbor, target, visited, path):
                    return True
        
        path.pop()
        return False
    
    def print_graph(self):
        print("\nRepresentasi Graf (Adjacency List):")
        for node in self.graph:
            print(node, "->", " -> ".join(map(str, self.graph[node])))

def main():
    print("=== Program DFS dengan Pencarian Target ===")
    g = Graph()
    
    print("\nMasukkan edges graf (format: 'node1 node2' contoh: 'A B', ketik 'done' untuk selesai):")
    while True:
        edge = input().strip()
        if edge.lower() == 'done':
            break
        try:
            u, v = edge.split()
            g.add_edge(u, v)
        except:
            print("Format salah. Gunakan format: node1 node2")
    
    g.print_graph()
    
    while True:
        start = input("\nMasukkan node awal: ").strip()
        target = input("Masukkan node target: ").strip()
        
        if start not in g.graph and target not in g.graph:
            print("Node tidak valid!")
            continue
        
        print(f"\nMencari jalur dari {start} ke {target}...")
        if not g.dfs_with_target(start, target):
            print(f"Target {target} tidak dapat dicapai dari {start}!")
        
        lanjut = input("\nCari lagi? (y/n): ").strip().lower()
        if lanjut != 'y':
            print("Program selesai.")
            break

if __name__ == "__main__":
    main()