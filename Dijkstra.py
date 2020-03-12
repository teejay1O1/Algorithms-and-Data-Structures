def Dijkstra(A, B, C):
        # A is num of nodes
        # B=[node1 node2 edge_weight]  this is very inefficient
        # therefor converted into this :
        dist=[[10e5 if _k!= _r else 0 for _k in range(A)] for _r in range(A)]
        for from_,to_,dist_  in B :     # this implementation is giving mle
            dist[from_][to_]=dist_
            dist[to_][from_]=dist_
        # C is source node
        
        ans=[10e5 for _ in range(A)]
        ans[C]=0
        q=[(0,C)]
        dist=[[10e5 if _k!= _r else 0 for _k in range(A)] for _r in range(A)]
        
        for from_,to_,dist_  in B :
            dist[from_][to_]=dist_
            dist[to_][from_]=dist_
        
        visited=[False for _ in range(A)]
        
        while q:
            shortestDist,shortestNode=heapq.heappop(q)
            #print(q)
            #print (shortestDist,shortestNode)
            if visited[shortestNode]:
                continue
            #print (dist[shortestNode])
            for adj_node,dist_ in enumerate(dist[shortestNode]):
                if dist_<10e5 :
                    new_dist=dist_+ans[shortestNode]
                    if new_dist < ans[adj_node] :
                        ans[adj_node]=new_dist
                        heapq.heappush(q,(new_dist,adj_node))
            visited[shortestNode]=True
        ans=[-1 if i==10e5 else i for i in ans]
        return ans
        